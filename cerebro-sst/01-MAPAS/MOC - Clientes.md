---
tipo: moc
titulo: MOC - Clientes
tags: [moc, cliente]
---

# 🏭 Clientes

Novo cliente: use [[T - Cliente]] (`06-TEMPLATES/`) e salve em `03-CLIENTES/`.

## Carteira ativa

```dataview
TABLE WITHOUT ID
  file.link AS "Cliente", setor AS "Setor", grau_risco AS "GR", funcionarios AS "Nº emp.", status AS "Status"
FROM "03-CLIENTES"
WHERE tipo = "cliente" AND status != "encerrado"
SORT file.name ASC
```

## Documentos vencendo (90 dias)

```dataview
TABLE WITHOUT ID
  file.link AS "Documento", cliente AS "Cliente", validade AS "Validade"
FROM "03-CLIENTES" OR "04-PROJETOS"
WHERE validade AND validade <= date(today) + dur(90 days)
SORT validade ASC
```

## Por setor

```dataview
TABLE WITHOUT ID rows.file.link AS "Clientes"
FROM "03-CLIENTES"
WHERE tipo = "cliente"
GROUP BY setor
```

## O que todo dossiê de cliente precisa ter

1. Dados cadastrais: CNPJ, CNAE, grau de risco, nº de empregados por estabelecimento
2. Estrutura organizacional de SST: tem SESMT? CIPA ou designado? Quem é o contato?
3. Inventário de GHE / funções
4. Documentos vigentes e validade: PGR, PCMSO, LTCAT, laudos, treinamentos
5. Histórico: acidentes, CAT, autuações, ações trabalhistas, perícias
6. Passivo identificado e o que está sendo feito a respeito
