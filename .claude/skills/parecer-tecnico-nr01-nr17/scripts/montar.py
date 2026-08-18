#!/usr/bin/env python3
"""
Preenche assets/template-parecer.html com os dados do parecer.

    python3 montar.py dados.json parecer.html
    python3 montar.py --exemplo parecer.html

O JSON aceita os campos de calcular.py mais os de identificacao. Campos derivados
(indice global, ranking, donut, veredicto, data de reavaliacao) sao calculados aqui —
nao devem vir no JSON.
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calcular import calcular  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(BASE, "assets", "template-parecer.html")
LOGO = os.path.join(BASE, "assets", "logo_lbm_base64.txt")

ICONE = {"FAVORAVEL": "&#10003;", "FAVORAVEL COM RESSALVAS": "!", "DESFAVORAVEL": "&#10007;"}
ROTULO = {"FAVORAVEL": "FAVORÁVEL",
          "FAVORAVEL COM RESSALVAS": "FAVORÁVEL<br>COM RESSALVAS",
          "DESFAVORAVEL": "DESFAVORÁVEL"}
TARJA1 = {"FAVORAVEL": ("PARECER FAVORÁVEL", "background:#eefaf4;border-color:#a5dfc6;color:#12a37a"),
          "FAVORAVEL COM RESSALVAS": ("PARECER COM RESSALVAS",
                                      "background:#fff6ec;border-color:#f0c69a;color:#e67e22"),
          "DESFAVORAVEL": ("PARECER DESFAVORÁVEL",
                           "background:#fdeeee;border-color:#e79a9a;color:#c0392b")}
SELO = {"concluida": "AET CONCLUÍDA", "em elaboracao": "AET EM ELABORAÇÃO",
        "nao iniciada": "AET PENDENTE", "nao exigida": "AET NÃO EXIGIDA"}
ETAPA_AET = {"concluida": "ELABORADA E CONCLUÍDA", "em elaboracao": "EM ELABORAÇÃO",
             "nao iniciada": "NÃO INICIADA", "nao exigida": "NÃO EXIGIDA"}

E = lambda s: html.escape(str(s), quote=False)


def donut(ranking):
    return "\n            ".join(
        f'<circle cx="60" cy="60" r="54" stroke="{f["cor"]}" '
        f'stroke-dasharray="{f["dash"]}" stroke-dashoffset="{f["dashoffset"]}"/>'
        for f in ranking)


def linhas_ranking(ranking):
    out = []
    for f in ranking:
        out.append(
            f'<div class="row">'
            f'<span class="chip" style="background:{f["cor"]}"></span>'
            f'<span class="pos">{f["rotulo_pos"]}</span>'
            f'<span class="nome">{E(f["nome"])}</span>'
            f'<span class="trilha"><span class="fill" style="width:{f["escore_exibido"]}%;'
            f'background:{f["cor"]}"></span></span>'
            f'<span class="pct" style="color:{f["cor"]}">{f["escore_exibido"]}%</span>'
            f'<span class="tag" style="color:{f["cor_badge"]};background:{f["fundo"]};'
            f'border-color:{f["borda"]}">{f["badge"]}</span>'
            f'</div>')
    return "\n        ".join(out)


def linhas_prov(provs):
    out = []
    for i, p in enumerate(provs, 1):
        nat = p["natureza"].upper()
        cls = "obrig" if nat.startswith("OBRIG") else "recom"
        out.append(
            f'<tr><td class="num">{i}</td><td>{E(p["providencia"])}</td>'
            f'<td class="nat {cls}">{E(nat)}</td>'
            f'<td class="resp">{E(p["responsavel"])}</td>'
            f'<td class="prazo">{E(p["prazo"])}</td></tr>')
    return "\n        ".join(out)


def montar(d):
    r = calcular(d)
    if any(a.startswith(("INCONSISTENCIA", "DIVERGENCIA")) for a in r["alertas"]):
        raise SystemExit("Nao gerar o documento. Corrija antes:\n  - "
                         + "\n  - ".join(r["alertas"]))

    aet = (d.get("aet") or "").lower().replace("_", " ")
    ver = r["veredicto"]
    tarja1_txt, tarja1_css = TARJA1[ver]
    ciclo_ok = ver == "FAVORAVEL"

    if aet != "concluida" and "conclu" in d.get("texto_ciclo", "").lower():
        r["alertas"].append(
            "texto_ciclo fala em AET concluida, mas o status informado e "
            f"'{aet}'. Reescreva o paragrafo antes de emitir.")

    logo = open(LOGO, encoding="utf-8").read().strip()
    tpl = open(TEMPLATE, encoding="utf-8").read()

    fontes = "\n        ".join(
        f'<div><span class="lk">{i}.</span> {E(t)}</div>'
        for i, t in enumerate(d["fontes"], 1))

    val = {
        "LOGO_BASE64": logo,
        "REVISAO": d["revisao"],
        "N_FATORES": r["n_fatores"],
        "EMPRESA": E(d["empresa"]).upper(),
        "EMPRESA_CURTA": E(d.get("empresa_curta", d["empresa"])),
        "CNPJ": E(d["cnpj"]),
        "DATA_AVALIACAO": d["data_avaliacao"],
        "DATA_EMISSAO": d["data_emissao"],
        "TRABALHADORES": E(d["trabalhadores"]),
        "INDICE_GLOBAL": r["indice_global"],
        "CONFORMES": r["conformes"],
        "STATUS_AET_KPI": E(ETAPA_AET.get(aet, aet).upper()),
        "BASE_VISUAL": r["base_visual"],
        "DONUT_SEGMENTOS": donut(r["ranking"]),
        "RANKING_LINHAS": linhas_ranking(r["ranking"]),
        "RESUMO_CLASSIFICACAO": E(d.get("resumo_classificacao",
                                        "TODOS CLASSIFICADOS COMO CONFORME" if ciclo_ok
                                        else "VER CLASSIFICAÇÃO POR FATOR NO RANKING")),
        "LEITURA_TECNICA": E(d["leitura_tecnica"]),
        "AEP_TOTAL": d["aep"]["total"],
        "AEP_BAIXA": d["aep"]["baixa"],
        "AEP_PIOR": d["aep"]["media_ou_pior"],
        "STATUS_RODAPE": E(d.get("status_rodape",
                                 "AEP registrada · AET concluída · monitoramento mantido")),
        "CODIGO_PARECER": d["codigo_parecer"],
        "STATUS_AET_SUB": E({"concluida": "AET concluída", "em elaboracao": "AET em elaboração",
                             "nao iniciada": "AET pendente",
                             "nao exigida": "AET não exigida"}.get(aet, "AET")),
        "VEREDICTO": ROTULO[ver],
        "COR_VEREDICTO": r["cor_veredicto"],
        "ICONE_VEREDICTO": ICONE[ver],
        "SELO_AET": E(SELO.get(aet, "AET")),
        "CICLO_STATUS": "CICLO AVALIATIVO CONCLUÍDO" if ciclo_ok else "CICLO AVALIATIVO EM ANDAMENTO",
        "TEXTO_CICLO": E(d["texto_ciclo"]),
        "ETAPA_AEP": E(d.get("etapa_aep", "CONCLUÍDA E REGISTRADA")),
        "ETAPA_AET": E(ETAPA_AET.get(aet, aet).upper()),
        "CLASSE_TABELA": " compacta" if len(d["providencias"]) > 4 else "",
        "PROVIDENCIAS_LINHAS": linhas_prov(d["providencias"]),
        "TITULO_REGISTRO_AET": E(d.get("titulo_registro_aet", "Registro de conclusão da AET")),
        "REGISTRO_AET": E(d["registro_aet"]),
        "TARJA_1": tarja1_txt,
        "ESTILO_TARJA_1": tarja1_css,
        "TARJA_2": "CICLO AVALIATIVO CONCLUÍDO" if ciclo_ok else "CICLO AVALIATIVO EM ANDAMENTO",
        "TARJA_3": "NR-01 + NR-17",
        "CONCLUSAO_TEXTO": d["conclusao_texto"],   # aceita <span> de destaque
        "DOC_BASE": E(d["doc_base"]),
        "COD_LAUDO": E(d["cod_laudo"]),
        "FONTES": fontes,
    }

    for k, v in val.items():
        tpl = tpl.replace("{{" + k + "}}", str(v))

    faltando = set(__import__("re").findall(r"\{\{([A-Z_0-9]+)\}\}", tpl))
    if faltando:
        raise SystemExit(f"Tokens nao preenchidos: {sorted(faltando)}")

    return tpl, r


def main():
    if sys.argv[1] == "--exemplo":
        dados = json.load(open(os.path.join(BASE, "assets", "exemplo-dados.json"), encoding="utf-8"))
        saida = sys.argv[2]
    else:
        dados = json.load(open(sys.argv[1], encoding="utf-8"))
        saida = sys.argv[2]

    doc, r = montar(dados)
    open(saida, "w", encoding="utf-8").write(doc)
    print(f"Gerado: {saida}")
    print(f"  veredicto ....... {r['veredicto']}")
    print(f"  indice global ... {r['indice_global']}%  (base visual {r['base_visual']})")
    print(f"  conformes ....... {r['conformes']}")
    print(f"  reavaliar ate ... {r['data_reavaliacao']}")
    for a in r["alertas"]:
        print(f"  ALERTA: {a}")


if __name__ == "__main__":
    main()
