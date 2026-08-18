# Módulo de saída — arquivos LBM BORATTI (HTML · Word · PDF · Excel)

Leia este arquivo apenas ao receber `GERAR HTML`, `GERAR WORD`, `GERAR PDF` ou `GERAR XLSX`, e somente depois que a APR ou o POP já estiver gerado em texto e validado pelo usuário. Estes comandos nunca disparam sozinhos. O conteúdo técnico vem do que foi aprovado — aqui só se formata. **Não altere o conteúdo técnico**: reproduza fielmente a APR (tabela) ou o POP (11 seções) e apenas aplique a identidade visual.

## Pré-requisito do ambiente

A geração de arquivos depende de a capacidade de execução de código / criação de arquivos estar ativa na conta (Configurações → Capacidades; em algumas contas o controle de saída vem desativado). Se a geração falhar, oriente o usuário a verificar isso antes de tentar de novo.

## Identidade visual

- Azul principal `#1a2f4e` · Laranja de destaque `#e67e22`.
- Documento **claro** (fundo branco), layout limpo, hierarquia clara de títulos, tabelas organizadas, ortografia PT-BR.
- APR/POP são documentos técnicos defensáveis (perícia/auditoria). Use a identidade com sobriedade — sem excesso de efeito visual.

## Logo (asset da própria skill)

Arquivo: `assets/logo-lbm-base64.txt` — 3 versões em data URI base64 (rótulos no arquivo):
- `LOGO_FULL` (900×294) — hero da capa / topo da página 1, altura ~130px.
- `LOGO_HEADER` (360×117) — cabeçalho interno das páginas 2+, altura ~32px.
- `LOGO_SIG` (600×196) — opcional, junto à assinatura/rodapé.

Extraia o data URI da versão desejada e embuta direto (base64); não dependa de arquivo externo. No Word, decodifique o base64 para um arquivo de imagem e embuta via `ImageRun(type:"jpg")`.

## Assinatura técnica (rodapé / fim do documento)

Marcelo Luis Boratti Melo — Engenheiro de Segurança do Trabalho · Fisioterapeuta e Ergonomista — CREA-SP 5069572947 · CREFITO-3 209468-F — LBM BORATTI · marengseg@gmail.com

## Cores das faixas de risco (iguais em todos os formatos)

Baixo `#d4edda` · Moderado `#fff3cd` · Alto `#fce4d6` · Crítico `#f8d7da` (preenchimentos claros, texto preto legível). Cabeçalho de tabela em navy `#1a2f4e` com texto branco.

---

## HTML — `GERAR HTML`

Documento premium imprimível, para o cliente abrir no navegador e salvar em PDF.

- Folha A4: **APR em paisagem** (a matriz tem 8 colunas e fica ilegível em retrato); **POP em retrato**. Um arquivo por entregável.
- Topo: `LOGO_FULL` centralizado (~130px) com glow laranja (`filter: drop-shadow(0 0 11px rgba(230,126,34,.6))`) — efeito exclusivo do HTML.
- Título do documento em navy, com filete laranja embaixo; subtítulo (atividade).
- Campos editáveis: marque metadados e células com `contenteditable="true"` para ajuste fino antes de imprimir.
- Matriz APR: cabeçalho navy/branco; células de **Nível** e **Risco Residual** coloridas por faixa; legenda com chips das faixas.
- POP: 11 seções, títulos navy com filete laranja; passos do item 8 numerados.
- Toolbar no topo (classe `.toolbar`/`.no-print`) com botão “Imprimir / Salvar em PDF” (`onclick="window.print()"`).
- Rodapé com a assinatura técnica.
- CSS de impressão (padrão definitivo): `@page { size: A4 landscape|portrait; margin: 9–11mm }`; `@media print` esconde a toolbar; `*{ -webkit-print-color-adjust:exact; print-color-adjust:exact }`; `thead{ display:table-header-group }` (repete o cabeçalho da matriz nas páginas); `tr{ page-break-inside:avoid }`.

## Word — .docx — `GERAR WORD`

Antes de gerar, **leia `/mnt/skills/public/docx/SKILL.md`** e siga-o (docx-js, A4, fonte Arial, tabelas com largura dupla `columnWidths`+`width`, nunca bullets manuais).

- A4: **APR em paisagem**, **POP em retrato** (no docx-js, passe dimensões retrato + `orientation: PageOrientation.LANDSCAPE`).
- `titlePage: true`: página 1 com `LOGO_FULL` (~130px, hero centralizado) no corpo; páginas 2+ com `LOGO_HEADER` (~32px) no cabeçalho à direita + filete navy. Glow não existe no Word — o banner já traz o filete laranja.
- Título navy + filete laranja; matriz com cabeçalho navy e células de Nível/Risco Residual coloridas por faixa (`ShadingType.CLEAR`); cabeçalho da matriz com `tableHeader: true` para repetir entre páginas.
- Bloco de assinatura ao fim; rodapé com “LBM BORATTI — Consultoria em SST” + número de página (use `footers.first` e `footers.default` quando `titlePage:true`, para o rodapé sair em todas as páginas).

## PDF — `GERAR PDF`

Duas vias, ambas válidas:
1. **Preferencial — print do HTML premium:** o usuário abre o HTML e usa “Imprimir / Salvar em PDF” (sai com glow e estilo de tela).
2. **Servidor:** (a) gere uma **variante print** do HTML — sem toolbar e com a folha em largura cheia, porque o `wkhtmltopdf` ignora `@media print` — e rode `wkhtmltopdf --page-size A4 --orientation Landscape|Portrait --margin-* 9–11`; ou (b) converta o `.docx` via LibreOffice (`soffice --headless --convert-to pdf`).
- Atenção (wkhtmltopdf): listas `<ol>` com 2 dígitos (10–13) cortam o marcador. Para os passos do POP, prefira **número em elemento estilizado** (token/círculo) em vez de marcador de `<ol>`, ou aumente o `padding-left` da lista (~34px).

## Excel — .xlsx — `GERAR XLSX` (aplica-se à APR)

Antes de gerar, **leia `/mnt/skills/public/xlsx/SKILL.md`** e siga-o. Use a matriz da APR já validada.

- Aba **“APR”**: colunas Etapa da Tarefa | Perigo (classe) | Risco/Dano | Severidade | Probabilidade | Nível | Medidas de Controle | Risco Residual. Cabeçalho navy/branco, linha congelada.
- **Severidade × Probabilidade por fórmula** (`=col_sev*col_prob`) para recalcular se o usuário ajustar; **Nível** e **Risco Residual** com preenchimento por faixa (formatação condicional nas mesmas cores).
- Aba **“Legenda”**: faixas de nível + escala 1–5 de severidade e probabilidade.
- Aba opcional **“Plano de Ação” (5W2H)** ligada às etapas de maior risco — inclua apenas se fizer sentido ao caso.
- O XLSX não usa o banner; identifique o documento no cabeçalho (texto “LBM BORATTI” + título + assinatura numa aba/rodapé).

## Entrega

Salve em `/mnt/user-data/outputs/` e apresente para download via present_files. O conteúdo técnico deve permanecer idêntico ao validado em texto.
