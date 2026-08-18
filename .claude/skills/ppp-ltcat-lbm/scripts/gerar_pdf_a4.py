#!/usr/bin/env python3
"""
gerar_pdf_a4.py — converte um .docx em PDF e normaliza para ISO A4, sem cortes
nem sobreposição. Autossuficiente (não depende de outra skill).

Etapas:
  1) LibreOffice headless converte .docx -> .pdf (preserva layout/tabelas);
  2) PyMuPDF re-monta cada página numa folha A4 limpa (595.276 x 841.890 pt),
     modo 'contain' (preserva proporção, nunca corta), margem configurável.

Uso:
    python gerar_pdf_a4.py entrada.docx saida.pdf [--margem-mm 0]

Requisitos: libreoffice no PATH; pip install pymupdf
Dica: se o texto estiver sendo empurrado e quebrando feio, o problema é de
paginação no .docx (use lib_docx.travar_assinatura / cant_split) — a etapa A4
normaliza o tamanho da folha, não conserta fluxo de texto mal resolvido.
"""

import argparse
import os
import subprocess
import sys
import tempfile

A4_W, A4_H = 595.276, 841.890  # pontos


def docx_para_pdf(docx_path, out_dir):
    subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "pdf",
         docx_path, "--outdir", out_dir],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    base = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
    return os.path.join(out_dir, base)


def normalizar_a4(pdf_in, pdf_out, margem_mm=0.0):
    import fitz  # PyMuPDF
    margem = margem_mm * 72.0 / 25.4
    src = fitz.open(pdf_in)
    dst = fitz.open()
    for page in src:
        nova = dst.new_page(width=A4_W, height=A4_H)
        alvo = fitz.Rect(margem, margem, A4_W - margem, A4_H - margem)
        r = page.rect
        esc = min(alvo.width / r.width, alvo.height / r.height)
        larg, alt = r.width * esc, r.height * esc
        x0 = alvo.x0 + (alvo.width - larg) / 2
        y0 = alvo.y0 + (alvo.height - alt) / 2
        nova.show_pdf_page(fitz.Rect(x0, y0, x0 + larg, y0 + alt), src, page.number)
    dst.save(pdf_out, deflate=True, garbage=4)
    dst.close()
    src.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("saida_pdf")
    ap.add_argument("--margem-mm", type=float, default=0.0)
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        pdf_bruto = docx_para_pdf(args.docx, tmp)
        normalizar_a4(pdf_bruto, args.saida_pdf, args.margem_mm)
    print(f"OK: {args.saida_pdf}")


if __name__ == "__main__":
    sys.exit(main())
