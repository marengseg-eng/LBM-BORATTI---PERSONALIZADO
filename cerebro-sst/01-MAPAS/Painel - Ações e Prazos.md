---
tipo: moc
titulo: Painel - Ações e Prazos
tags: [moc, status/pendente]
---

# ⏰ Ações e Prazos

## 🔴 Vencidas

```dataview
TABLE WITHOUT ID
  file.link AS "Item", cliente AS "Cliente", responsavel AS "Responsável", prazo AS "Venceu em"
FROM "03-CLIENTES" OR "04-PROJETOS" OR "08-COMERCIAL"
WHERE prazo AND prazo < date(today)
  AND status != "concluido" AND status != "cancelado"
SORT prazo ASC
```

## 🟠 Esta semana

```dataview
TABLE WITHOUT ID
  file.link AS "Item", cliente AS "Cliente", responsavel AS "Responsável", prazo AS "Prazo"
FROM "03-CLIENTES" OR "04-PROJETOS" OR "08-COMERCIAL"
WHERE prazo AND prazo >= date(today) AND prazo <= date(today) + dur(7 days)
  AND status != "concluido"
SORT prazo ASC
```

## 🟡 Próximos 30 dias

```dataview
TABLE WITHOUT ID
  file.link AS "Item", cliente AS "Cliente", prazo AS "Prazo"
FROM "03-CLIENTES" OR "04-PROJETOS" OR "08-COMERCIAL"
WHERE prazo AND prazo > date(today) + dur(7 days) AND prazo <= date(today) + dur(30 days)
  AND status != "concluido"
SORT prazo ASC
```

## ✅ Tarefas abertas em qualquer nota

```dataview
TASK
WHERE !completed AND !file.folder.contains("06-TEMPLATES")
GROUP BY file.link
```

## 📆 Recorrências que ninguém pode esquecer

| Recorrência | Periodicidade | Base |
|---|---|---|
| Revisão do PGR / inventário de riscos | até 2 anos (ou 3 anos em condição específica) — e sempre após acidente ou mudança | [[NR-01 — Disposições Gerais e GRO]] |
| Relatório analítico do PCMSO | anual | [[NR-07 — PCMSO]] |
| Eleição e posse da CIPA | anual (mandato) | [[NR-05 — CIPA e CIPA+A]] |
| SIPAT | anual | [[NR-05 — CIPA e CIPA+A]] |
| Reciclagem NR-35 (trabalho em altura) | bienal, e sempre em mudança de procedimento/função ou retorno de afastamento > 90 dias | [[NR-35 — Trabalho em Altura]] |
| Reciclagem NR-10 | bienal | [[NR-10 — Segurança em Instalações Elétricas]] |
| Reciclagem NR-33 | anual | [[NR-33 — Espaços Confinados]] |
| Calibração de instrumentos (dosímetro, TGD, bomba) | conforme certificado (usualmente anual) | [[NR-09 — Avaliação e Controle das Exposições]] |
| Inspeção de EPI / troca por validade | conforme CA e uso | [[NR-06 — EPI]] |
| Atualização de LTCAT | a cada mudança de ambiente/processo/EPI | [[MOC - Entregáveis]] |
