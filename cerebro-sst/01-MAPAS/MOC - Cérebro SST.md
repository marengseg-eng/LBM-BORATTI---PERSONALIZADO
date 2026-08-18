---
tipo: moc
titulo: MOC - Cérebro SST
tags: [moc, home]
---

# 🧠 Cérebro SST — LBM BORATTI

> Porta de entrada do vault. Fixe esta nota (`Marcar como favorito`) e comece o dia por aqui.

## Mapas

| Mapa | Para quê |
|---|---|
| [[MOC - Normas Regulamentadoras]] | O que cada NR exige, na prática |
| [[MOC - Clientes]] | Carteira, contratos e histórico |
| [[MOC - Entregáveis]] | Anatomia de cada documento que emitimos |
| [[MOC - Comercial]] | Serviços, precificação e pipeline |
| [[Painel - Ações e Prazos]] | O que vence primeiro |
| [[Mapa de Skills LBM]] | Qual skill do Claude gera qual documento |

## Painéis

### 🔥 Vence nos próximos 30 dias

```dataview
TABLE WITHOUT ID
  file.link AS "Item", tipo AS "Tipo", cliente AS "Cliente", prazo AS "Prazo"
FROM "03-CLIENTES" OR "04-PROJETOS"
WHERE prazo AND prazo <= date(today) + dur(30 days)
  AND status != "concluido" AND status != "cancelado"
SORT prazo ASC
```

### 🚧 Projetos em andamento

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto", cliente AS "Cliente", status AS "Status", prazo AS "Prazo"
FROM "04-PROJETOS"
WHERE tipo = "projeto" AND (status = "em-andamento" OR status = "em-revisao")
SORT prazo ASC
```

### 📥 Inbox por processar

```dataview
LIST
FROM "00-INBOX"
WHERE file.name != "00-INBOX" AND !file.folder.contains("diario")
SORT file.mtime DESC
```

### ⚖️ Perícias ativas

```dataview
TABLE WITHOUT ID
  file.link AS "Processo", cliente AS "Parte", prazo AS "Prazo fatal", status AS "Status"
FROM "04-PROJETOS"
WHERE tipo = "pericia" AND status != "concluido"
SORT prazo ASC
```

### 📚 Normas com verificação de vigência vencida (> 180 dias)

```dataview
TABLE WITHOUT ID
  file.link AS "Norma", verificado_em AS "Última verificação"
FROM "02-NORMAS"
WHERE tipo = "norma" AND (!verificado_em OR verificado_em <= date(today) - dur(180 days))
SORT verificado_em ASC
```

## Rotina

**Diária** — abrir a nota do dia (`00-INBOX/diario/`), jogar tudo que apareceu no Inbox,
olhar o painel de prazos.

**Semanal (sexta, 30 min)** — zerar o Inbox: cada item vira projeto, ação, nota de
conhecimento ou lixo. Revisar status dos projetos. Conferir o que vence na semana seguinte.

**Mensal** — revisar carteira de clientes (documento vencendo? treinamento a reciclar?),
atualizar pipeline comercial, verificar vigência das NRs mais usadas.

**Anual** — arquivar concluídos, revisar catálogo de serviços e precificação.

## Convenções

Antes de criar nota nova: [[Convenções e Taxonomia]].
