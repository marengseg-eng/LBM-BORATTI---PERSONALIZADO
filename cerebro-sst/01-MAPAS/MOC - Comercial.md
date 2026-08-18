---
tipo: moc
titulo: MOC - Comercial
tags: [moc, comercial]
---

# 💼 Comercial

- [[Catálogo de Serviços]] — escopo de cada serviço e o que **não** está incluso
- [[Pipeline]] — oportunidades em andamento

## Funil

```dataview
TABLE WITHOUT ID
  rows.file.link AS "Oportunidades", length(rows) AS "Qtd"
FROM "08-COMERCIAL"
WHERE tipo = "oportunidade"
GROUP BY status
```

## Propostas aguardando resposta

```dataview
TABLE WITHOUT ID
  file.link AS "Oportunidade", cliente AS "Cliente", enviada_em AS "Enviada", validade AS "Validade"
FROM "08-COMERCIAL"
WHERE tipo = "oportunidade" AND status = "proposta-enviada"
SORT validade ASC
```

> [!important] Preço
> Este vault **não guarda tabela de preço fechada**. Valor é definido caso a caso por
> Boratti, considerando escopo, deslocamento, nº de GHE, nº de postos e prazo. A skill
> `proposta-comercial-sst` nunca inventa valor — ela usa o que for informado na sessão.
