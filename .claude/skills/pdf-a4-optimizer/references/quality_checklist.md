# Checklist de qualidade para PDF A4 profissional

Use este checklist para entregas formais, impressao, documentos de cliente, treinamentos, laudos, propostas, apostilas e relatorios.

## 1. Enquadramento

Classificar a finalidade do PDF antes de otimizar:

- Impressao simples: priorizar A4 real, margem segura e legibilidade.
- Entrega formal ao cliente: priorizar acabamento visual, padronizacao e validacao em render.
- Assinatura digital: evitar rasterizar quando a assinatura/certificacao ja existir; se precisar rasterizar, avisar que recursos interativos podem ser perdidos.
- Material com QR code, escala grafica ou desenho tecnico: evitar `stretch`; preservar proporcao.
- Formulario/editavel: evitar `--flatten` se o usuario precisa editar campos depois.

## 2. Base tecnica

Verificar no arquivo final:

1. Tamanho da pagina
   - A4 retrato: 595.276 x 841.890 pt.
   - A4 paisagem: 841.890 x 595.276 pt.

2. Ocupacao da folha
   - Conteudo deve ocupar a maior area util possivel.
   - Se a proporcao original nao for A4, aceitar faixas brancas no modo `contain` para evitar corte.
   - Se o usuario exigir preenchimento absoluto, usar `stretch` e registrar a distorcao.

3. Integridade visual
   - Sem texto cortado.
   - Sem rodape/cabecalho cortado.
   - Sem tabelas invadindo outras areas.
   - Sem imagem, assinatura, carimbo ou logo sobreposto indevidamente.
   - Sem paginas em branco indevidas.
   - Sem rotacao errada.

4. Compatibilidade
   - Abrir/renderizar em pelo menos um motor confiavel.
   - Para PDFs problematicos, comparar render antes/depois.
   - Para formulários, assinaturas, carimbos ou transparencia, considerar verificacao em dois leitores/renderizadores.

## 3. Recomendacao

Padrao recomendado para documentos tecnicos:

```bash
python scripts/optimize_pdf_a4.py input.pdf output_a4.pdf --mode contain --orientation auto --margin-mm 0 --check-dir check_renders --report report.json
```

Padrao recomendado para documentos com risco de corte em bordas:

```bash
python scripts/optimize_pdf_a4.py input.pdf output_a4.pdf --mode contain --orientation auto --margin-mm 3 --check-dir check_renders --report report.json
```

Padrao recomendado para PDF visualmente instavel:

```bash
python scripts/optimize_pdf_a4.py input.pdf output_a4_flat.pdf --mode contain --orientation auto --margin-mm 3 --flatten --raster-dpi 220 --jpeg-quality 92 --check-dir check_renders --report report.json
```

Nao prometer "perfeito" sem validacao visual. Preferir dizer "otimizado e validado visualmente" quando o render final foi conferido.
