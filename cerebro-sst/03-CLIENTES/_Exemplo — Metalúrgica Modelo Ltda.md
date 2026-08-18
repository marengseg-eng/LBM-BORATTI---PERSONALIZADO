---
tipo: cliente
titulo: Metalúrgica Modelo Ltda
cnpj: 00.000.000/0001-00
cnae: 25.32-2/01
grau_risco: 3
setor: metalurgia
funcionarios: 87
cidade: Cascavel/PR
contato: Fulano (RH)
status: ativo
inicio_contrato: 2026-03-01
tags: [cliente/metalurgica-modelo, setor/metalurgia]
---

# Metalúrgica Modelo Ltda

> Nota de **exemplo**, para mostrar o preenchimento. Duplique [[T - Cliente]] para clientes reais
> e apague este arquivo quando não precisar mais dele.

## Identificação

| Campo | Dado |
|---|---|
| Razão social | Metalúrgica Modelo Ltda |
| CNPJ | 00.000.000/0001-00 |
| CNAE principal | 25.32-2/01 — estamparia e funilaria |
| Grau de risco | **3** ([[NR-04 — SESMT]]) |
| Nº de empregados | 87 (estabelecimento único) |
| Contato | Fulano — RH — (45) 90000-0000 |

## Estrutura de SST

- SESMT: não obrigatório para o porte/GR atual — reavaliar se passar de 100 empregados
- CIPA: constituída, mandato até 2027-03-14 — treinamento de **16 h** (GR 3)
- Brigada de incêndio: sim, 6 brigadistas

## GHE / Funções

| GHE | Funções | Nº | Riscos principais | NRs |
|---|---|---|---|---|
| GHE-01 Estamparia | operador de prensa | 22 | ruído, prensagem, postura | NR-12, NR-15 An.1, NR-17 |
| GHE-02 Solda | soldador | 14 | fumos metálicos, radiação NI, calor | NR-15 An.7/11/12, NR-06 |
| GHE-03 Acabamento | esmerilhador, pintor | 18 | poeira, solvente, ruído, vibração | NR-15 An.8/11/13 |
| GHE-04 Logística | operador de empilhadeira | 9 | atropelamento, carga, vibração | NR-11, NR-12 |
| GHE-05 Administrativo | analistas | 24 | ergonômico, psicossocial | NR-17, NR-01 |

## Documentos e validade

| Documento | Emissão | Validade / revisão | Situação |
|---|---|---|---|
| PGR | 2026-03-20 | 2028-03-20 | ✅ vigente |
| PCMSO (relatório analítico) | 2026-02-10 | 2027-02-10 | ✅ vigente |
| LTCAT | 2024-08-01 | revisar | ⚠️ desatualizado após troca de prensas |
| AET | — | — | ❌ pendente (GHE-01 e GHE-05) |
| Avaliação psicossocial | — | — | ❌ pendente |
| AVCB | 2025-11-02 | 2027-11-02 | ✅ vigente |

## Histórico

### Acidentes e CAT
- 2026-05-14 — esmagamento de dedo em prensa (GHE-01), CAT emitida, 12 dias de afastamento.
  Investigação: proteção com intertravamento burlado. Ver plano de ação.

### Autuações
- Nenhuma registrada até a data.

### Passivo identificado
1. LTCAT desatualizado após a troca de maquinário — impacto direto em PPP e aposentadoria especial
2. Ausência de AET em posto com queixa recorrente de ombro (GHE-01)
3. Riscos psicossociais ainda não avaliados

## Projetos

```dataview
TABLE WITHOUT ID file.link AS "Projeto", tipo AS "Tipo", status AS "Status", prazo AS "Prazo"
FROM "04-PROJETOS"
WHERE contains(string(cliente), this.file.name)
SORT prazo ASC
```
