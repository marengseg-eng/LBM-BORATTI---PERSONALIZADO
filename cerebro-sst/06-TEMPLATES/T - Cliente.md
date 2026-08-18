---
tipo: cliente
titulo:
cnpj:
cnae:
grau_risco:
setor:
funcionarios:
cidade:
contato:
telefone:
email:
status: ativo
inicio_contrato:
tags: [cliente/]
---

# {{title}}

## Identificação

| Campo | Dado |
|---|---|
| Razão social | |
| CNPJ | |
| CNAE principal | |
| **Grau de risco** ([[NR-04 — SESMT]]) | |
| Nº de empregados (por estabelecimento) | |
| Endereço | |
| Contato / cargo | |

## Estrutura de SST

- SESMT: ( ) obrigatório ( ) não obrigatório — composição atual:
- CIPA: ( ) constituída ( ) designado — mandato até:
- Brigada de incêndio: ( ) sim ( ) não
- Responsável interno pelo tema:

## GHE / Funções

| GHE | Funções | Nº | Riscos principais | NRs aplicáveis |
|---|---|---|---|---|
| | | | | |

## Documentos e validade

| Documento | Emissão | Validade / revisão | Situação |
|---|---|---|---|
| PGR | | | |
| PCMSO (relatório analítico) | | | |
| LTCAT | | | |
| AET | | | |
| Avaliação psicossocial | | | |
| Laudo de insalubridade/periculosidade | | | |
| AVCB | | | |

## Histórico

### Acidentes e CAT
### Autuações e notificações
### Ações trabalhistas / perícias
### Passivo identificado

## Projetos

```dataview
TABLE WITHOUT ID file.link AS "Projeto", tipo AS "Tipo", status AS "Status", prazo AS "Prazo"
FROM "04-PROJETOS"
WHERE contains(string(cliente), this.file.name)
SORT prazo ASC
```

## Visitas

```dataview
LIST
FROM "04-PROJETOS"
WHERE tipo = "visita" AND contains(string(cliente), this.file.name)
SORT file.name DESC
```

## Anotações
