# Exemplos de Uso — resumo-psicossocial

## Exemplo 1: PDF fornecido

**Input do usuário:**
> "Gera uma folha-resumo desse laudo aqui pra eu entregar pro cliente"
> [anexa PDF do laudo]

**Ação esperada:**
- Ler dados do PDF
- Extrair: empresa, índice, fatores, ações
- Gerar HTML one-pager sem perguntas adicionais

---

## Exemplo 2: Dados parciais

**Input do usuário:**
> "Faz o resumo do psicossocial da CIVITAS — deu 34% na média, 2 fatores em atenção"

**Ação esperada:**
- Iniciar extração
- Perguntar: lista dos fatores com scores, ações propostas, nº do documento
- Gerar após receber respostas

---

## Exemplo 3: Referência direta ao one-pager

**Input do usuário:**
> "One-pager do laudo RPS-84-H4SUP do Lar Vila Vicentini"

**Ação esperada:**
- Identificar que é um resumo executivo
- Se laudo estiver em contexto, extrair e gerar
- Se não, perguntar dados chave

---

## Exemplo 4: Vários clientes

**Input do usuário:**
> "Tenho 3 laudos psicossociais pra resumir: ALLGE (21%), GR (45%), RGA (67%)"

**Ação esperada:**
- Gerar 3 arquivos HTML separados
- Cada um com visual de veredicto correspondente (verde / laranja / vermelho)
- Nomes: resumo-psicossocial-allge.html, resumo-psicossocial-gr.html, resumo-psicossocial-rga.html

---

## Triggers que DEVEM acionar esta skill

- "resumo do laudo psicossocial"
- "folha-resumo psicossocial"
- "one-pager psicossocial"
- "versão simples pra cliente"
- "síntese do relatório psicossocial"
- "página única avaliação psicossocial"
- "sumário executivo psicossocial"
- "condensar o laudo"
- [PDF de avaliação psicossocial] + qualquer pedido de resumo

## Triggers que NÃO devem acionar esta skill

- Pedido de laudo COMPLETO → usar `psicossocial-nr01`
- Pedido de questionário → usar `psicossocial-nr01`
- Pedido de PGR → usar `gestao-sst-completa`
- Pedido de DDS sobre saúde mental → usar `dds-sst`
