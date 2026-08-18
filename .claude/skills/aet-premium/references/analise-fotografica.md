# PASSO 0 — ANÁLISE FOTOGRÁFICA (8 BLOCOS POR FOTO)

Este documento descreve o protocolo de análise **foto a foto** usado pelo MÉTODO LBM BORATTI
antes de compor o relatório completo. Baseado no modelo canônico `AET-ELETROSERT-2025-001`.

---

## Quando aplicar

- **Sempre** que o usuário enviar uma ou mais fotos de postos de trabalho
- **Antes** de gerar as Seções 3.4 (Caracterização), 3.5 (Biomecânica) e 3.7 (NR-17)
- Em **batch mode**: ao receber múltiplas fotos, gerar 8 blocos por foto e ao final uma **tabela-resumo consolidada**

---

## Os 8 blocos obrigatórios por foto

### Bloco 1 — TAREFA PRESCRITA
O que o trabalhador **deveria** estar fazendo segundo descrição de cargo / procedimento /
CBO. Base formal e teórica.

**Formato:**
```
📋 TAREFA PRESCRITA
Função: [Cargo] — CBO [código]
Atividade prevista: [descrição breve]
Equipamentos previstos: [lista]
```

---

### Bloco 2 — TAREFA REAL
O que é **efetivamente observado** na foto. Descrição objetiva, sem julgamento, do que
está acontecendo no momento do registro.

**Formato:**
```
🎬 TAREFA REAL OBSERVADA
[Descrição narrativa em 3–5 linhas do que a foto mostra: postura, ferramentas,
mobiliário, organização, vestimenta/EPI visíveis, ambiente ao fundo]
```

⚠️ **Regra:** Nunca inventar dados não visíveis. Se algo não aparece, sinalizar como
"⚠ Hipótese:" ou omitir.

---

### Bloco 3 — OBSERVAÇÕES TÉCNICAS
Achados ergonômicos classificados por criticidade usando emojis semafóricos:

| Emoji | Significado |
|---|---|
| 🔴 | Achado crítico — intervenção imediata |
| 🟠 | Achado de alto risco — intervenção necessária |
| 🟡 | Achado de risco médio — investigar e corrigir |
| 🟢 | Achado positivo — manter/replicar |

**Formato:**
```
🔍 ACHADOS ERGONÔMICOS
🔴 [achado crítico com descrição + referência normativa]
🟠 [achado alto com ângulo/medida estimada]
🟡 [achado médio]
🟢 [ponto positivo — quando existir]
```

---

### Bloco 4 — ANÁLISE POSTURAL (RULA + REBA ESTIMATIVOS)
Pontuação biomecânica **por foto**, marcada como **ESTIMATIVA** (baseada em análise
visual, não em medição direta com goniômetro).

**Formato:**
```
📐 ANÁLISE POSTURAL (ESTIMATIVA)
┌─────────┬────────┬─────────────────────────┐
│ Método  │ Score  │ Nível de ação           │
├─────────┼────────┼─────────────────────────┤
│ RULA    │ [1-7]  │ [descrição textual]     │
│ REBA    │ [1-15] │ [descrição textual]     │
└─────────┴────────┴─────────────────────────┘
Observações: [posturas específicas que elevaram o score]
```

**Níveis RULA:**
- 1–2: Aceitável
- 3–4: Investigar
- 5–6: Investigar e corrigir em breve
- 7: Investigar e corrigir **imediatamente**

**Níveis REBA:**
- 1: Risco desprezível
- 2–3: Risco baixo
- 4–7: Risco médio — investigar
- 8–10: Risco alto — investigar e corrigir
- 11–15: Risco muito alto — intervenção imediata

---

### Bloco 5 — CHECKLIST NR-17 (ITENS RELEVANTES)
Marcar apenas os itens da NR-17 que **aparecem** na foto. Não listar itens não avaliáveis.

**Formato:**
```
📋 CHECKLIST NR-17 (itens visíveis)
✅ 17.5.3 Cadeira com apoio lombar ajustável
❌ 17.5.2 Monitor na linha dos olhos (tela 15 cm abaixo do ideal)
⚠️ 17.5.4 Apoio para pés — não visível
```

Símbolos:
- ✅ Conforme
- ❌ Não conforme
- ⚠️ Parcial / não avaliável visualmente

---

### Bloco 6 — FATORES DE RISCO (MATRIZ AIHA P×S)
Para cada achado 🔴 ou 🟠, atribuir Probabilidade × Severidade.

**Formato:**
```
⚠️ FATORES DE RISCO
┌──────────────────────────┬──────┬──────┬──────────┐
│ Fator                    │ Prob │ Sev  │ Nível    │
├──────────────────────────┼──────┼──────┼──────────┤
│ Flexão cervical >40°     │  A   │  A   │ 🔴 Crít. │
│ Cadeira sem apoio braços │  M   │  M   │ 🟡 Médio │
└──────────────────────────┴──────┴──────┴──────────┘
```

Probabilidade: B (Baixa) / M (Média) / A (Alta)
Severidade: B / M / A
Nível: 🟢 Baixo | 🟡 Médio | 🟠 Alto | 🔴 Crítico

---

### Bloco 7 — CAUSA RAIZ (5 PORQUÊS)
Análise rápida da causa raiz do principal risco encontrado, em cascata de 5 porquês.

**Formato:**
```
🎯 CAUSA RAIZ (5 Porquês)
Problema: [risco principal identificado]
1. Por que ocorre? → [causa imediata]
2. Por que isso? → [causa intermediária]
3. Por que? → [causa contextual]
4. Por que? → [causa organizacional]
5. Por que? → [causa raiz sistêmica]
```

---

### Bloco 8 — RECOMENDAÇÕES ESPECÍFICAS
Recomendações **para aquela foto**, seguindo a **hierarquia de controles** da NR-01 (2024).

Hierarquia (em ordem de prioridade):
1. **Eliminação** do risco
2. **Substituição** do processo/equipamento
3. **Controle de engenharia** (mobiliário, layout, equipamentos)
4. **Controle administrativo** (pausas, rodízio, treinamento)
5. **EPI** (último recurso)

**Formato:**
```
💡 RECOMENDAÇÕES ESPECÍFICAS
✅ [ação com hierarquia] — [referência NR quando aplicável]
✅ [ação com hierarquia]
ℹ️ [orientação complementar, quando aplicável]

[Para cada ação, na consolidação do relatório:]
  Prazo: ⚡ Imediato (0–30d) / 🟠 Curto (30–90d) / 🟡 Médio (90–180d)
  Custo: Baixo / Médio / Alto
```

---

## Batch mode — Tabela-resumo consolidada

Após os 8 blocos de **todas** as fotos, gerar uma tabela consolidada:

```
| Foto | Posto / Função              | Setor          | REBA | RULA | Nível    |
|------|------------------------------|----------------|------|------|----------|
|  01  | Recepcionista — sem headset  | Recepção       |  8   |  7   | 🔴 Crít. |
|  02  | Analista Adm. — digitação    | Administrativo |  5   |  5   | 🟡 Médio |
|  03  | Técnico — bancada            | Laboratório    |  8   |  6   | 🟠 Alto  |
| ...  | ...                          | ...            | ...  | ...  | ...      |
```

E um resumo de criticidade:
```
DISTRIBUIÇÃO DE RISCO
🔴 Crítico:  N postos
🟠 Alto:     N postos
🟡 Médio:    N postos
🟢 Baixo:    N postos
```

---

## Regras de ouro

1. **Nunca inventar dados não visíveis** — sempre marcar hipóteses com "⚠ Hipótese:"
2. **Scores RULA/REBA são SEMPRE ESTIMATIVAS** — declarar isso explicitamente
3. **Modelo de atenuação por exposição**: Quando a tarefa é curta (<10 min), infrequente
   (1–2×/dia), com EPI adequado e sem queixas, aplicar fator de atenuação no risco final —
   documentar **todos** os fatores atenuantes
4. **Consistência de nomenclatura**: "Alto" em vez de "Moderado" foi adotado como padrão
   LBM — mas cliente pode solicitar "Moderado"; sempre documentar a opção de classificação
5. **Foto ausente ≠ risco ausente** — declarar limitações do estudo quando fotos não
   cobrirem todos os postos
