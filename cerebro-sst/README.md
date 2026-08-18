# 🧠 Cérebro SST — Vault Obsidian | LBM BORATTI

Base de conhecimento e operação da **LBM BORATTI Consultoria Personalizada em
Segurança e Saúde no Trabalho**, no formato de vault do [Obsidian](https://obsidian.md).

Este não é um arquivo morto de PDFs. É o **cérebro operacional**: normas
interpretadas para aplicação, clientes, projetos, prazos, perícias, checklists de
campo e templates que alimentam as skills de geração de documento.

---

## Como abrir

1. Baixe o Obsidian (gratuito) em <https://obsidian.md>.
2. `Abrir pasta como cofre` → selecione a pasta **`cerebro-sst`** deste repositório.
3. Comece por **[[MOC - Cérebro SST]]** (`01-MAPAS/`). É a porta de entrada.

O vault já vem com configuração básica (`.obsidian/`): tema escuro, cor de destaque
laranja LBM, pasta de templates e de notas diárias definidas, links no formato
`[[wikilink]]`.

## Plugins da comunidade recomendados

Os painéis com consulta automática (prazos vencendo, projetos em aberto, clientes por
NR) usam **Dataview**. Sem ele, os blocos aparecem como código e o resto do vault
funciona normalmente.

| Plugin | Para quê | Prioridade |
|---|---|---|
| **Dataview** | Painéis dinâmicos de prazos, projetos, ações e perícias | 🔴 essencial |
| **Templater** | Templates com data automática e prompts | 🟠 alta |
| **Kanban** | Pipeline comercial e plano de ação em quadro | 🟡 média |
| **Calendar** | Agenda de visitas, treinamentos e vencimentos | 🟡 média |
| **Excalidraw** | Croqui de layout, árvore de causas, mapa de risco | 🟢 opcional |
| **Omnisearch** | Busca dentro de PDFs anexados (laudos, normas) | 🟢 opcional |

Instalação: `Configurações → Plugins da comunidade → Procurar`.

---

## Estrutura

```
cerebro-sst/
├── _meta/              Convenções, taxonomia de tags, anexos
├── 00-INBOX/           Captura rápida + notas diárias (processar semanalmente)
├── 01-MAPAS/           MOCs e painéis — a navegação do cérebro
├── 02-NORMAS/          Uma nota por NR: o que a norma exige, na prática
├── 03-CLIENTES/        Dossiê por cliente (GHE, documentos, histórico)
├── 04-PROJETOS/        Entregas em andamento (PGR, AET, LTCAT, perícia…)
├── 05-BIBLIOTECA/      Jurisprudência, metodologias, limites, glossário
├── 06-TEMPLATES/       Modelos de nota (cliente, projeto, visita, perícia…)
├── 07-CHECKLISTS/      Roteiros de campo prontos para imprimir/usar no celular
├── 08-COMERCIAL/       Catálogo de serviços e pipeline
├── 09-SKILLS/          Ponte entre o vault e as skills do Claude
└── 99-ARQUIVO/         Encerrados — sai da vista, não sai do histórico
```

## Fluxo de trabalho

```
Captura (00-INBOX)  →  Processa  →  Vira nota permanente
                                     ├─ Cliente   → 03-CLIENTES
                                     ├─ Projeto   → 04-PROJETOS
                                     ├─ Conhecimento → 02-NORMAS / 05-BIBLIOTECA
                                     └─ Ação com prazo → frontmatter `prazo:`
                                                          aparece em [[Painel - Ações e Prazos]]
```

Um projeto encerrado vai para `99-ARQUIVO/` com `status: concluido`. Nada é deletado —
o histórico é o que sustenta a defesa técnica anos depois.

## Regra de ouro sobre vigência normativa

Norma muda. Este vault registra **interpretação e aplicação**, não substitui o texto
oficial. Toda nota de NR traz o campo `verificado_em:` no frontmatter.

> Antes de usar uma nota de norma em documento que sai com assinatura técnica,
> confira o texto vigente em <https://www.gov.br/trabalho-e-emprego> e atualize
> `verificado_em:`.

---

_LBM BORATTI Consultoria Personalizada em SST — uso interno._
