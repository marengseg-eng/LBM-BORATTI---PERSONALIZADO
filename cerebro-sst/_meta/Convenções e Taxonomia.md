---
tipo: meta
titulo: Convenções e Taxonomia
tags: [meta]
---

# Convenções e Taxonomia

O que faz este vault funcionar não é a pasta — é o **frontmatter**. Os painéis do
[[MOC - Cérebro SST]] só enxergam a nota que preenche os campos certos.

## 1. Tipos de nota (`tipo:`)

| `tipo` | O que é | Pasta |
|---|---|---|
| `norma` | Interpretação aplicada de uma NR | `02-NORMAS/` |
| `cliente` | Dossiê do cliente | `03-CLIENTES/` |
| `projeto` | Entrega contratada com prazo | `04-PROJETOS/` |
| `visita` | Registro de campo (inspeção, coleta, AET) | `04-PROJETOS/` |
| `documento` | Entregável emitido (PGR, LTCAT, AET, PPP…) | `04-PROJETOS/` |
| `acao` | Item de plano de ação com responsável e prazo | junto do projeto |
| `pericia` | Processo judicial / assistência técnica | `04-PROJETOS/` |
| `acidente` | Investigação de acidente ou quase-acidente | `04-PROJETOS/` |
| `dds` | Diálogo Diário de Segurança realizado | `04-PROJETOS/` |
| `referencia` | Conhecimento sem dono (súmula, método, limite) | `05-BIBLIOTECA/` |
| `checklist` | Roteiro de campo | `07-CHECKLISTS/` |
| `template` | Modelo de nota | `06-TEMPLATES/` |
| `moc` | Mapa de conteúdo / painel | `01-MAPAS/` |

## 2. Campos padrão

```yaml
---
tipo: projeto                  # obrigatório, da tabela acima
titulo: PGR 2026 — Metalúrgica X
cliente: "[[Metalúrgica X]]"   # wikilink, sempre entre aspas
status: em-andamento           # ver seção 3
nrs: [NR-01, NR-09, NR-12]     # lista, sempre no formato NR-XX
responsavel: Boratti
prazo: 2026-09-30              # ISO YYYY-MM-DD — é o que alimenta os painéis
criado: 2026-08-18
tags: [sst/pgr, cliente/metalurgica-x]
---
```

**Data sempre em ISO (`YYYY-MM-DD`).** No corpo do texto pode escrever 30/09/2026; no
frontmatter, não — o Dataview não ordena data em formato brasileiro.

## 3. Status (`status:`)

`ideia` → `proposta` → `contratado` → `em-andamento` → `em-revisao` → `entregue` →
`concluido` | `parado` | `cancelado`

Um projeto com `status: concluido` sai dos painéis ativos. Mova para `99-ARQUIVO/`
quando o ciclo de vigência do documento encerrar.

## 4. Prioridade e risco

- `prioridade:` `alta` | `media` | `baixa`
- `risco:` classificação do risco tratado — `trivial` | `tolerável` | `moderado` |
  `substancial` | `intolerável` (escala da matriz do PGR)

## 5. Tags

Hierárquicas, minúsculas, sem acento, separadas por `/`:

```
sst/norma/nr-35        sst/pgr           sst/aet
sst/pericia            sst/psicossocial  sst/treinamento
cliente/nome-do-cliente
setor/metalurgia       setor/construcao  setor/frigorifico   setor/rural
agente/ruido           agente/calor      agente/quimico      agente/biologico
agente/ergonomico      agente/psicossocial
status/pendente        status/vencendo
```

Regra: **tag para atravessar pastas, link para conectar ideias.** Se dá para linkar,
linke — a tag é o último recurso.

## 6. Nomes de arquivo

- Cliente: nome fantasia limpo → `Metalúrgica X.md`
- Projeto: `TIPO AAAA — Cliente` → `PGR 2026 — Metalúrgica X.md`
- Visita: `Visita AAAA-MM-DD — Cliente` → `Visita 2026-08-18 — Metalúrgica X.md`
- Perícia: `Perícia — Processo 0001234-56.2025.5.09.0001.md`
- Norma: `NR-XX — Assunto.md`

Sem barra, sem `:`, sem `#` no nome do arquivo — quebram link em alguns sistemas.

## 7. Links obrigatórios

Toda nota de projeto linka: **cliente**, **NRs aplicáveis** e **visitas** que a
originaram. É essa malha que faz o grafo responder "tudo que já fiz de NR-35 no
frigorífico" em dois cliques.
