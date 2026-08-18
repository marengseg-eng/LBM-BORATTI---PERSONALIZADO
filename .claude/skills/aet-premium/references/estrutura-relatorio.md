# ESTRUTURA COMPLETA DO RELATÓRIO AET — 13 Seções (detalhamento do Passo 3)

Referência do **Passo 3** da skill `aet-premium`. O SKILL.md traz o resumo;
este arquivo traz o detalhamento seção a seção.

---

## 3.1 CAPA PROFISSIONAL
Seguir `assets/capa-template.md`. Logo por injeção programática
(ver `references/outputs-html.md`). Nº do documento: `AET-{{CLIENTE}}-{{ANO}}-{{SEQ3}}`.

## 3.2 IDENTIFICAÇÃO
- {{EMPRESA}} · {{CNPJ}} · {{ENDERECO}} (quando disponível) · {{CNAE}} · {{GRAU_RISCO}}
- {{SETOR}} · {{FUNCAO}} · {{CBO}}
- {{DATA_AVALIACAO}}
- Responsável técnico: bloco da Seção 1 do SKILL.md (CREA + CREFITO obrigatórios)
- Nº do documento

## 3.3 OBJETIVO, ESCOPO E LIMITAÇÕES
- Objetivo técnico e objetivo legal
- Normas aplicáveis (Seção 8 do SKILL.md)
- Metodologias ERGOSTORE aplicadas (lista)
- **Limitações do estudo — sempre explicitar** (ex.: análise baseada em fotos =
  estimativas visuais; dados informados não verificados in loco; ausência de medições
  instrumentais). Esta subseção é obrigatória e protege o RT em contestação.

## 3.4 CARACTERIZAÇÃO DA EMPRESA E DO TRABALHO
- Descrição da empresa
- Organização do trabalho: turnos, pausas, metas ({{JORNADA}})
- Descrição detalhada das tarefas (AET descritiva — tarefa prescrita × tarefa real)
- Análise da demanda: queixas, indicadores de saúde, CAT, afastamentos, NTEP

## 3.5 ANÁLISE BIOMECÂNICA
Para **cada** metodologia selecionada no Passo 2:
- Tabela de pontuação com critérios
- Score final + nível de risco **ou** "não calculável com os dados disponíveis"
- Descrição das posturas críticas
- Comparativo com limites normativos
- Rótulo epistêmico explícito (`ESTIMATIVA VISUAL` vs `DADO OBSERVADO`)

## 3.6 ANÁLISE COGNITIVA E PSICOSSOCIAL (quando aplicável)
- Demandas cognitivas: atenção, memória, decisão, pressão temporal, autonomia
- Fatores psicossociais (NR-01, Portaria MTE 1.419/2024) — abordagem técnica e
  organizacional, sem diagnóstico clínico
- NASA-TLX e/ou ERGOS quando aplicáveis
- Integração com o PGR quando pertinente

## 3.7 ANÁLISE DO POSTO (NR-17) — Checklist 47 itens
Avaliação sistemática por subitem (17.2 a 17.7), formato:
**Situação Atual | Requisito Normativo | Conformidade (✓ / ✗ / Parcial / NA)**
> Itens completos: `references/nr17-checklist.md`

## 3.8 MATRIZ DE RISCO ERGONÔMICO (AIHA adaptada)

| Fator de Risco | Probabilidade | Severidade | Nível | Prioridade |
|---|---|---|---|---|
| {{fator}} | B/M/A | B/M/A | 🟢🟡🟠🔴 | 1–4 |

**Nomenclatura da escala (padrão LBM):** Baixo · Médio · **Alto** · Crítico.
O rótulo do terceiro nível é "Alto" (não "Moderado") — questão exclusivamente de
nomenclatura. A classificação de cada fator decorre **somente** do cruzamento
Probabilidade × Severidade observado/estimado, jamais de padrão pré-atribuído.
Cliente que exigir "Moderado": atender e documentar a opção no relatório.

## 3.9 PLANO DE AÇÃO ERGONÔMICO (PAE)
Cobertura obrigatória: **100% dos riscos Alto e Crítico**. Formato por item:

```
PAE-{{XX}} — {{nome curto}}
RISCO: {{descrição}} + foto de referência quando disponível
MEDIDA: ação específica, ancorada em norma com item (quando seguro)
TIPO: Eliminação / Substituição / Engenharia / Administrativa / EPI (hierarquia NR-01)
RESPONSÁVEL: {{cargo ou área}}
PRAZO: ⚡ Imediato (0–30d) / 🟠 Curto (30–90d) / 🟡 Médio (90–180d)
CUSTO ESTIMADO: Baixo / Médio / Alto (faixa R$ quando possível)
INDICADOR: métrica + meta + prazo de reavaliação
```

## 3.10 CONCLUSÃO TÉCNICA
- Síntese dos principais achados
- Nível de risco geral do posto
- Top 3 recomendações prioritárias
- Necessidade e prazo de reavaliação ({{PRAZO_REAVALIACAO}})
> Textos padrão: `references/padroes-texto.md`

## 3.11 REFERÊNCIAS NORMATIVAS E BIBLIOGRÁFICAS
- NRs com versão/portaria (ou incerteza sinalizada)
- ABNT NBR com ano de edição · ISO aplicadas
- Bibliografia das ferramentas ergonômicas (autor, ano, título)

## 3.12 GLOSSÁRIO TÉCNICO (opcional recomendado)
18 termos; no HTML, busca ao vivo com atalho `/`.

## 3.13 ASSINATURA E RESPONSABILIDADE TÉCNICA
Bloco integral da Seção 1 do SKILL.md + Sertãozinho/SP + {{DATA_ELABORACAO}}.
