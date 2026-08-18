# Examples — relatorio-inspecao-sst

Casos de uso reais extraídos das conversas de origem (mai/dez 2025).

---

## Caso 1 — Pedido direto com dados completos

**Usuário:**
> "Gera um relatório de inspeção para a Empresa FASS, inspeção realizada em 10/12/2025, área: escadas metálicas externas NR-35, inspeção programada."

**Comportamento esperado:**
1. NÃO perguntar nada — dados suficientes estão presentes
2. Inferir modo: MODO 2 — Inspeção Modular NR-35
3. Como NÃO há fotos nem achados relatados: gerar HTML como **relatório-modelo**,
   com itens típicos de escada metálica (corrosão, guarda-corpo, ancoragem) rotulados
   `[MODELO — editar conforme observado]` e aviso de versão-modelo no sumário
4. NÃO atribuir criticidade como constatada — os cards-modelo trazem a criticidade
   típica sugerida, confirmável na edição em campo (KPIs zerados até confirmação)

---

## Caso 2 — Envio de fotos de campo

**Usuário:**
> [envia 3 fotos] "Analisa essas fotos da inspeção de hoje na linha de produção, cliente Alfa Laval."

**Comportamento esperado:**
1. Analisar cada foto e extrair achados (ato inseguro × condição insegura)
2. Classificar criticidade por foto
3. Citar NR pertinente por achado
4. Perguntar apenas: empresa completa, data, tipo de inspeção
5. Gerar HTML com fotos base64 embutidas nos cards

---

## Caso 3 — Pedido vago (modo rotina)

**Usuário:**
> "Cria um relatório de inspeção pra cliente novo."

**Comportamento esperado:**
Fazer EM UMA ÚNICA mensagem:

> "Para gerar o relatório, preciso confirmar:
> - **Empresa:** ?
> - **Área inspecionada:** ?
> - **Data e horário:** ?
> - **Tipo de inspeção** (rotineira / programada / pós-acidente / não programada): ?
> - **Logo do cliente** (pode inserir depois pelo botão 🏢 na toolbar)?
>
> Se quiser, pode mandar fotos da inspeção que eu analiso e classifico cada achado."

NÃO fazer múltiplas rodadas de perguntas.

---

## Caso 4 — Inspeção pós-acidente

**Usuário:**
> "Houve um quase-acidente ontem na caldeiraria da Indústria X. Preciso de um relatório de inspeção urgente."

**Comportamento esperado:**
1. Acionar MODO 1 — Inspeção Geral (com ênfase pós-ocorrência)
2. Adicionar campo "Tipo de evento" na Seção 3
3. Perguntar: qual foi a ocorrência? Há fotos? Quem estava envolvido (função, não nome)?
4. Incluir seção extra: "Análise de Causa Raiz" (método dos 5 porquês ou Ishikawa)
5. Reforçar no Sumário Executivo: "inspeção pós-ocorrência — ação imediata requerida"

---

## Caso 5 — Walkthrough pré-AET

**Usuário:**
> "Vou fazer uma AET no setor de solda da SMS Group. Precisa de um walkthrough antes?"

**Comportamento esperado:**
1. Acionar MODO 3 — Walkthrough Survey
2. Gerar HTML compacto (2 páginas): Dados Gerais + Achados Rápidos + Encaminhamentos
3. Ao final do HTML, incluir bloco JSON estruturado para alimentar `aet-premium`:
```json
{
  "empresa": "SMS Group Metalurgia do Brasil",
  "setor": "Caldeiraria e Soldagem",
  "riscos_identificados": ["ruído", "calor", "radiação não ionizante", "postura"],
  "nr_aplicaveis": ["NR-15", "NR-17"],
  "encaminhar_aet": true
}
```

---

## Caso 6 — Inspeção Comportamental BBS

**Usuário:**
> "Faz um relatório de inspeção comportamental na linha de embalagem, 20 observações, 14 seguras e 6 inseguras."

**Comportamento esperado:**
1. Acionar MODO 4 — BBS
2. Calcular taxa de segurança: 14/20 = 70%
3. Gerar seção de Análise Comportamental:
   - Gráfico pizza: 70% safe / 30% at-risk
   - Top 3 comportamentos de risco (pedir dados ou inferir do contexto)
   - Meta proposta: ≥ 90% seguro em 60 dias
4. Vincular ao PGR (NR-01 item 1.5 — participação dos trabalhadores)

---

## Caso 7 — Inserir logo do cliente

**Usuário:**
> [após HTML gerado] "Aqui o logo da empresa cliente." [envia PNG]

**Comportamento esperado:**
1. Salvar imagem em base64
2. Substituir placeholder da `.capa-logo-cliente img`
3. CSS obrigatório: `background:#fff; padding:6px 10px; border-radius:4px;`
4. NÃO usar `filter: brightness(0) invert(1)` — quebra impressão
5. Re-entregar HTML atualizado com logo incorporado

---

## Caso 8 — Modo Teste / Demo

**Usuário:**
> "Faz um relatório teste pra eu ver como fica o layout."

**Comportamento esperado:**
1. NÃO perguntar dados
2. Preencher com dados realistas:
   - Empresa: "Indústria Modelo Ltda. — CNPJ 00.000.000/0001-00"
   - Área: "Linha de Produção 01 — Setor Usinagem"
   - Data: data atual
   - 4 achados distribuídos: 1 Crítico (EPI sem CA) + 1 Alto (máquina sem proteção NR-12) + 1 Médio (sinalização NR-26) + 1 Baixo (organização 5S)
   - 3 ações 5W2H correspondentes
3. Gerar HTML completo
4. Avisar em banner amarelo no topo: "⚠️ DOCUMENTO DE DEMONSTRAÇÃO — Substitua os dados antes de imprimir."

---

## Anti-Casos — Quando NÃO Acionar a Skill

**Pergunta conceitual:**
> "Como faço para inspecionar uma máquina NR-12?"
→ NÃO acionar skill — é pergunta normativa, responder em prosa.
→ Pode mencionar ao final: "Se quiser que eu gere um relatório de inspeção formatado, é só me avisar."

**Pergunta normativa:**
> "Quais NRs se aplicam a trabalho em altura?"
→ NÃO acionar skill — responder citando NR-35 + NR-18 + NR-06 sem gerar HTML.

**Pedido de AET:**
> "Faz uma análise ergonômica do posto de trabalho."
→ NÃO acionar esta skill — acionar `aet-premium`.

**Pedido de CIPA:**
> "Cria o edital de eleição da CIPA."
→ NÃO acionar esta skill — acionar `cipa-eleicao`.
