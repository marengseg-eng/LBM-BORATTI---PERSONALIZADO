---
tipo: moc
titulo: Mapa de Skills LBM
tags: [moc, skills]
---

# 🔌 Mapa de Skills — do vault ao documento

Este vault guarda **o conhecimento e os dados**. As skills do Claude geram **o documento
formatado**. O fluxo eficiente é: preencher a nota aqui → abrir o Claude → acionar a skill
com esses dados em mãos.

| Skill | Gera | Insumo que sai deste vault |
|---|---|---|
| `dds-sst` | DDS em HTML A4 (3–4 folhas) | [[T - DDS]] — empresa, data, tema, nº de participantes |
| `relatorio-inspecao-sst` | Relatório de Inspeção (RIS) | [[T - Visita Técnica]] + [[Checklist - Inspeção Geral]] + fotos |
| `aet-premium` | AET completa | posto, função, medições, método ([[Metodologias Ergonômicas]]) |
| `psicossocial-nr01` | Questionário, dashboard, laudo e plano | [[Riscos Psicossociais - NR-01 e ISO 45003]] |
| `resumo-psicossocial` | One-pager A4 para o cliente | laudo psicossocial pronto |
| `pericia-trabalhista-pro` | Impugnação, quesitos, parecer, vistoria | [[T - Perícia]] + [[Súmulas e OJs - Insalubridade e Periculosidade]] |
| `ppp-ltcat-lbm` | PPP e LTCAT (Word/PDF) | GHE, agentes, enquadramento, dados do cliente |
| `cipa-eleicao` | Edital, atas, calendário, SIPAT, treinamento NR-05 | [[NR-05 — CIPA e CIPA+A]] + dados do cliente (GR, nº de empregados) |
| `treinamentos-sst` | Roteiro, slides, avaliação, presença, certificado | NR alvo + perfil da turma |
| `apr-pop-sst` | APR, POP, PT | tarefa específica + checklist da NR aplicável |
| `investigador-de-acidentes-sst` | Relatório de investigação, 5 porquês, árvore de causas | [[T - Acidente]] |
| `consultor-de-nrs-sst` | Interpretação aplicada de NR | dúvida concreta de cliente |
| `proposta-comercial-sst` | Proposta técnica e comercial | [[T - Oportunidade Comercial]] + [[Catálogo de Serviços]] |
| `conselheiro-estrategico-sst` | Análise estratégica do negócio | [[Pipeline]] |
| `humanizer` | Revisão de texto que ficou com cara de IA | qualquer texto do vault |
| `pdf-a4-optimizer` | PDF A4 limpo para impressão | documento gerado |

## Regra de ouro do fluxo

**Dado bruto mora no vault. Formatação mora na skill.** Não copie o documento gerado de
volta para dentro da nota inteiro — guarde no `_meta/anexos/` e linke. A nota fica com o
que interessa reencontrar depois: decisões, achados, números e o porquê.

## Prompt de partida (copiar e colar)

```
Cliente: [nome] — CNAE [x], GR [y], [n] empregados, setor [z]
Contexto: [o que foi levantado na visita / o que o cliente pediu]
Documento desejado: [DDS / RIS / AET / ...]
Dados: [colar a tabela da nota do vault]
```
