---
tipo: moc
titulo: MOC - Entregáveis
tags: [moc]
---

# 📄 Entregáveis

Anatomia de cada documento que sai com a assinatura da LBM BORATTI: o que é, o que
exige, quanto dura e o que costuma dar errado.

| Documento | Base | Validade / revisão | Skill |
|---|---|---|---|
| **PGR** (inventário + plano de ação) | [[NR-01 — Disposições Gerais e GRO]] | até 2 anos (3 anos se certificado ISO 45001 ou MEI/ME/EPP em condição específica) — e sempre após acidente, mudança de processo ou nova exigência | `gestao-sst-completa` |
| **PCMSO** | [[NR-07 — PCMSO]] | anual (relatório analítico) | — |
| **LTCAT** | Lei 8.213/91 + [[NR-15 — Atividades e Operações Insalubres]] | atualizar a cada mudança de layout, processo, EPI ou ambiente | `ppp-ltcat-lbm` |
| **PPP** | IN INSS + Anexo XV | contínuo (entrega na rescisão / requerimento) | `ppp-ltcat-lbm` |
| **AET** | [[NR-17 — Ergonomia]] | quando houver mudança de posto, queixa, afastamento ou exigência | `aet-premium` |
| **Avaliação de riscos psicossociais** | [[NR-01 — Disposições Gerais e GRO]] + ISO 45003 | integrada ao ciclo do PGR | `psicossocial-nr01` |
| **Relatório de Inspeção (RIS)** | NR aplicável ao setor | por visita | `relatorio-inspecao-sst` |
| **APR / POP / PT** | [[NR-01 — Disposições Gerais e GRO]] + NR da tarefa | por tarefa; revisar a cada mudança de método | `apr-pop-sst` |
| **Investigação de acidente** | NR-01 (item de análise de acidentes) | por evento | `investigador-de-acidentes-sst` |
| **Documentos de CIPA** | [[NR-05 — CIPA e CIPA+A]] | ciclo anual do mandato | `cipa-eleicao` |
| **Treinamentos por NR** | NR específica | conforme periodicidade da norma | `treinamentos-sst` |
| **DDS** | boa prática / NR-01 | diário ou por turno | `dds-sst` |
| **Impugnação / quesitos / parecer** | CPC + NR-15/16/17 | prazo processual | `pericia-trabalhista-pro` |
| **Proposta comercial** | — | validade da proposta | `proposta-comercial-sst` |

## Regras que valem para todo documento

- **Rastreabilidade**: metodologia declarada, instrumento com certificado de calibração
  vigente, data e condição da medição, quem mediu.
- **Coerência entre documentos**: PGR ↔ LTCAT ↔ PPP ↔ PCMSO ↔ ASO precisam contar a
  mesma história. Divergência é o que a perícia ataca primeiro.
- **Assinatura e responsabilidade técnica**: profissional legalmente habilitado, com
  registro; ART quando cabível.
- **Evidência**: foto datada, registro de entrega de EPI, lista de presença de
  treinamento. Documento sem evidência não sustenta defesa.

## Entregáveis em produção

```dataview
TABLE WITHOUT ID
  file.link AS "Documento", cliente AS "Cliente", status AS "Status", prazo AS "Prazo"
FROM "04-PROJETOS"
WHERE tipo = "documento" AND status != "concluido"
SORT prazo ASC
```
