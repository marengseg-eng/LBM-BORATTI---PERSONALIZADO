---
tipo: moc
titulo: Pipeline
tags: [comercial, moc]
---

# Pipeline Comercial

Nova oportunidade: [[T - Oportunidade Comercial]].

## Estágios

`contato-inicial` → `diagnostico` → `proposta-enviada` → `negociacao` → `fechado` | `perdido`

## Em aberto

```dataview
TABLE WITHOUT ID
  file.link AS "Oportunidade", cliente AS "Cliente", status AS "Estágio", validade AS "Validade"
FROM "08-COMERCIAL"
WHERE tipo = "oportunidade" AND status != "fechado" AND status != "perdido"
SORT status ASC
```

## Fechadas

```dataview
TABLE WITHOUT ID file.link AS "Oportunidade", cliente AS "Cliente", servicos AS "Serviços"
FROM "08-COMERCIAL"
WHERE tipo = "oportunidade" AND status = "fechado"
```

## Perdidas — e por quê (revisar trimestralmente)

```dataview
TABLE WITHOUT ID file.link AS "Oportunidade", cliente AS "Cliente"
FROM "08-COMERCIAL"
WHERE tipo = "oportunidade" AND status = "perdido"
```

## Rotina comercial

- **Semanal**: revisar oportunidades paradas há mais de 7 dias — follow-up ou marcar perdida
- **Mensal**: mapear clientes da carteira com documento vencendo em 90 dias (renovação é a
  venda mais barata que existe) — ver [[MOC - Clientes]]
- **Trimestral**: ler as perdidas juntas e procurar o padrão
