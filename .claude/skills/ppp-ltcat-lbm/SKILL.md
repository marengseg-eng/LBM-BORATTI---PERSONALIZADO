---
name: ppp-ltcat-lbm
description: >-
  Gera e revisa PPP (Perfil Profissiográfico Previdenciário, Anexo XV) e LTCAT
  (Laudo Técnico das Condições Ambientais do Trabalho) para a LBM BORATTI
  Consultoria em SST, em Word (.docx) e PDF A4. Use SEMPRE que o usuário
  mencionar: PPP, LTCAT, perfil profissiográfico, laudo de condições ambientais,
  aposentadoria especial, agente nocivo, enquadramento previdenciário, campo 15,
  fator de risco no PPP, inserir/revisar risco (físico, químico, biológico,
  ergonômico) em PPP ou LTCAT, coerência PPP x LTCAT, ou enviar um PPP/LTCAT
  para corrigir, inserir agente, ajustar enquadramento (NR-15/anexos) ou gerar o
  PDF. Acionar também quando descrever uma função (vaqueiro, soldador, operador,
  etc.) e pedir para montar/atualizar o PPP ou o LTCAT do segurado, mesmo sem
  usar a sigla. NÃO usar para PGR/inventário de riscos de setor (é outro escopo),
  perícia trabalhista (skill pericia-trabalhista-pro) ou AET (skill aet-premium).
---

# PPP e LTCAT — LBM BORATTI

Cria do zero **e** revisa PPP e LTCAT, entregando **Word (.docx)** editável e
**PDF A4** otimizado. Segue a metodologia técnica e as regras normativas da LBM
BORATTI, com foco em conformidade previdenciária e coerência entre os documentos.

## Fluxo obrigatório (nunca pular)

Ao pedir um PPP ou LTCAT — novo ou revisão — **não gere o arquivo final de
imediato**. A ordem é sempre:

1. **Eco dos dados e das lacunas.** Repita os dados recebidos (segurado, empresa,
   CAEPF/CNAE, função + CBO, período, setor, agentes, intensidades, técnica,
   EPC/EPI/CA) e liste objetivamente o que falta.
2. **Briefing.** Objetivo do documento, estrutura, dados necessários e **pontos
   de atenção técnica e normativa** — em especial o enquadramento (grau/critério),
   a técnica de avaliação por agente e a coerência PPP↔LTCAT.
3. **Aguardar a validação, correção ou complementação do usuário.**
4. **Só então gerar** o Word e, se solicitado, o PDF A4.

Exceção: se o usuário já disser explicitamente "gera o arquivo" com dados
suficientes, pule para a geração — mas ainda faça o eco em 2-3 linhas antes.

## Antes de gerar/revisar: leia as referências

- `references/guia_ppp_ltcat.md` — campos do PPP (Anexo XV), estrutura do LTCAT,
  coerência a conferir e a mecânica de tabelas. **Leia sempre** ao mexer na
  estrutura ou ao inserir/mover agentes.
- `references/enquadramento_agentes.md` — técnica de avaliação por agente e o
  enquadramento de agente biológico (NR-15, Anexo 14, grau médio x máximo).
  **Leia ao decidir grau/técnica de qualquer agente.**
- PDFs bundlados (fontes primárias de aposentadoria especial): resumo do
  **Decreto 10.410/2020** e **IN PRES/INSS nº 128**. Consulte-os para localizar o
  dispositivo exato — **não cite número de artigo de memória**.

## Regras normativas (obrigatórias)

- O documento vigente de gerenciamento de riscos é o **PGR**; nunca trate PPRA
  como vigente.
- Não invente número de item, artigo, anexo, prazo, CA ou exigência. Cite só com
  segurança; na dúvida, sinalize a incerteza e recomende a fonte oficial.
- Diferencie **obrigação legal**, **boa prática técnica** e **recomendação
  consultiva**.
- Não afirme "EPI eficaz = S" sem o número do **CA** correspondente.
- Ruído/calor → avaliação **quantitativa** (NHO/NR-15). Agente biológico →
  **qualitativa** (NR-15, Anexo 14). Ver tabela em `enquadramento_agentes.md`.

## Gerar do zero

1. Faça o eco + briefing e valide (fluxo obrigatório).
2. Parta dos modelos: `assets/templates/PPP_modelo.docx` e
   `assets/templates/LTCAT_modelo.docx`. Eles já trazem o formulário Anexo XV do
   PPP (com as mesclagens corretas) e a estrutura completa do LTCAT LBM. Copie o
   modelo e **preencha/substitua** os dados — não recrie o formulário do zero.
3. Preencha os campos administrativos, profissiografia, e uma **linha por agente**
   no campo 15 do PPP e na tabela-resumo do item 6 do LTCAT (mais o subtópico
   textual correspondente e o item 10.1 quando o agente muda o enquadramento).
4. Garanta a coerência PPP↔LTCAT (função/CBO, período, agentes, intensidades).
5. Aplique os cuidados de paginação (seção "Paginação") e gere as saídas.

## Revisar / inserir agente em documento existente

1. Leia o documento (se for `.doc` antigo, converta:
   `libreoffice --headless --convert-to docx arquivo.doc --outdir <dir>`).
2. Localize a tabela de riscos e **mapeie a linha-modelo** antes de tocar nela:

   ```python
   from docx import Document
   import sys; sys.path.append("scripts")
   import lib_docx as L
   doc = Document("PPP.docx")
   tab = doc.tables[0]
   idx = L.indice_linha_por_texto(tab, "Ruído")   # linha de um agente já existente
   print(L.mapear_linha(tab, idx))                 # veja os índices de célula a preencher
   ```

3. Clone essa linha para inserir o novo agente, preservando mesclagens:

   ```python
   L.clonar_linha_risco(tab, idx, {
       1: "Biológico",
       2: "Agentes biológicos (bactérias, vírus, fungos e parasitas) - contato "
          "permanente com bovinos, secreções e dejetos em currais/estábulos",
       3: "Qualitativo",
       4: "Qualitativa - NR-15, Anexo 14",
       5: "NA", 6: "N", 7: "NI",
   }, cant_split=True)   # cant_split evita a linha se partir entre páginas
   doc.save("PPP.docx")
   ```

   Os índices são a **ordem das células** da linha-modelo (não o número do campo);
   por isso o `mapear_linha` acima. No LTCAT, atualize **os dois lugares**: o
   subtópico textual do item 6 e a tabela-resumo, e complemente o item 10.1
   quando o enquadramento muda.
4. **Não altere a estrutura** salvo pedido: acrescente conteúdo, não renumere nem
   redesenhe o layout.
5. Confira a coerência PPP↔LTCAT e aplique os cuidados de paginação.

## Paginação (evita corte e sobreposição no PDF)

Dois defeitos recorrentes e como preveni-los, sempre, antes de gerar o PDF:

- **Linha de tabela se parte entre páginas** → trave com `cant_split=True`
  (já embutido no `clonar_linha_risco`) ou `L.set_cant_split(row._tr)`.
- **Bloco de assinatura se separa** (nome numa página, CREA no topo da seguinte,
  colado no cabeçalho) → `L.travar_assinatura(doc, ["Marcelo Luis Boratti Melo",
  "CREA"])` e, se necessário,
  `L.remover_paragrafos_vazios_excedentes(doc, "Considerações", manter=2)`.

## Gerar as saídas

- **Word:** o próprio `.docx` editado/preenchido é a entrega editável.
- **PDF A4:** `python scripts/gerar_pdf_a4.py entrada.docx saida.pdf`
  (LibreOffice + normalização A4 por PyMuPDF; margem 0 por padrão).
- **Sempre valide renderizando** as páginas críticas (linha do agente, assinatura)
  e confirme A4 real (595.276 x 841.890 pt), sem corte nem sobreposição, antes de
  entregar. Se houver defeito, é paginação no `.docx` — corrija na origem e
  regenere; a etapa A4 não conserta fluxo de texto.

## Identidade e assinatura (LBM BORATTI)

Cores: azul principal **#1a2f4e**, laranja de destaque **#e67e22**. Layout limpo,
técnico, pronto para cliente. Ortografia em pt-BR.

Assinatura técnica padrão (ajuste conforme o profissional responsável no documento):

```
Marcelo Luis Boratti Melo
Engenheiro de Segurança do Trabalho
Fisioterapeuta e Ergonomista
CREA-SP 5069572947
CREFITO-3 209468-F
LBM BORATTI
E-mail: marengseg@gmail.com
```

## Entrega

Entregue o `.docx` e o `.pdf` ao usuário e feche com um resumo curto do que foi
feito e dos **pontos em aberto** (dados faltantes, CA de EPI, enquadramento a
confirmar). Ofereça ajustar o que depender de dado que só o usuário tem.
