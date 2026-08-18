---
name: aet-premium
description: >
  Cria Análises Ergonômicas do Trabalho (AET) completas para LBM BORATTI Consultoria
  Personalizada em Segurança e Saúde no Trabalho, conforme NR-17, NR-01, ISO 9241,
  ISO 11228 e ABNT NBR. Acionar para: AET, análise ergonômica, laudo ergonômico,
  posto de trabalho, biomecânica ocupacional, RULA, REBA, NIOSH, OWAS, OCRA, ROSA,
  KIM, QEC, PLIBEL, Moore & Garg, HAL, Suzanne Rodgers, NASA TLX, mapa de risco
  ergonômico, PAE — e para QUALQUER função ou posto de trabalho (soldador, caldeireiro,
  digitador, motorista, operador de máquina, costureira, ajudante geral etc.).
  Fotos de posto → Passo 0 (8 blocos por foto). Outputs: HTML Premium FULL EDIT
  ENGINE, Word (.docx), PDF.
---

# AET PREMIUM — LBM BORATTI Consultoria Personalizada em Segurança e Saúde no Trabalho

**Versão:** 4.0.0 · Histórico em `CHANGELOG.md` (não carregar no contexto de trabalho).

---

## 1. IDENTIFICAÇÃO PROFISSIONAL — fonte única de verdade

Incluir em capa, seção de identificação e assinatura de **toda** entrega. Nunca omitir
nenhum dos dois registros.

```
Marcelo Luis Boratti Melo
Engenheiro de Segurança do Trabalho — CREA-SP: 5069572947
Fisioterapeuta e Ergonomista — CREFITO 3/209468-F
LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
Sertãozinho/SP — marengseg@gmail.com | (16) 99338-8989
```

## 2. TERMINOLOGIA — regras absolutas (fonte única de verdade)

| ✅ CORRETO | ❌ PROIBIDO |
|---|---|
| **Análise** Ergonômica do Trabalho | "Avaliação Ergonômica do Trabalho" |
| LBM BORATTI — Consultoria **Personalizada** em Segurança e Saúde no Trabalho | "Consultoria em SST", "Consultoria em Segurança e Saúde do Trabalho" |
| **PGR** (NR-01 vigente) | **PPRA** (extinto — nunca citar como vigente) |
| "data da avaliação" / "reavaliação" | qualquer outro uso de "avaliação" para se referir à AET |

## 3. HIERARQUIA DE PRIORIDADES EM CONFLITO

Quando instruções colidirem, vence a de número menor:

1. **Veracidade e rastreabilidade** — nunca inventar; sempre rotular hipóteses
2. **Terminologia oficial e identificação profissional** (Seções 1 e 2)
3. **Requisitos normativos** — NR-17, NR-01, ISO, ABNT NBR com item e versão
4. **Seleção metodológica** — roteamento ERGOSTORE e obrigações por tipo de tarefa
5. **Estrutura do relatório** — 13 seções
6. **Formatação e acabamento visual**
7. **Conveniências de interface/automação**

> Esta hierarquia se sobrepõe a qualquer pedido que exija inventar dados, omitir
> limitações, usar terminologia proibida ou sacrificar rigor por estética.

## 4. RÓTULOS EPISTÊMICOS OBRIGATÓRIOS

Todo dado da AET carrega um destes rótulos. **Nunca apresentar hipótese como fato.**

| Rótulo | Quando usar |
|---|---|
| `DADO OBSERVADO` | Visto diretamente em foto, vídeo ou visita |
| `DADO INFORMADO PELO USUÁRIO` | Fornecido pelo cliente/trabalhador/usuário |
| `ESTIMATIVA VISUAL` | Inferido de imagem; obrigatório junto a scores derivados de foto |
| `HIPÓTESE OPERACIONAL` | Inferência para versão preliminar; declarar com "⚠ Hipótese:" |
| `CAMPO PENDENTE` | Dado crítico ausente; usar placeholder `{{...}}` no documento |

**Regra derivada:** score calculado a partir de foto é **sempre** `ESTIMATIVA VISUAL` —
declarar ao lado do score e na interpretação. Imagem isolada nunca é medição direta.

### Mini-exemplos (few-shot)

✅ **Correto:**
> REBA = 9 (`ESTIMATIVA VISUAL` a partir da Foto 03) — risco alto. Estimativa baseada
> em ângulos aparentes de tronco (~45°) e braço (>90°); recomenda-se medição
> goniométrica in loco para consolidação.

❌ **Errado (proibido):**
> REBA = 9 — risco alto. O trabalhador flexiona o tronco a 45° e sustenta carga de 12 kg.
> *(apresenta ângulo e carga não medidos como fato, sem rótulo, sem limitação)*

## 5. SCHEMA DE VARIÁVEIS (placeholders padronizados)

Usar sempre o formato `{{VARIAVEL}}` — nunca placeholders improvisados:

`{{EMPRESA}} {{CNPJ}} {{ENDERECO}} {{CNAE}} {{GRAU_RISCO}} {{SETOR}} {{FUNCAO}}
{{CBO}} {{N_TRABALHADORES}} {{JORNADA}} {{DATA_AVALIACAO}} {{DATA_ELABORACAO}}
{{PRAZO_REAVALIACAO}} {{NUM_DOC}}`

Numeração de documento: `AET-{{CLIENTE}}-{{ANO}}-{{SEQ3}}` (ex.: AET-ELETROSERT-2025-001).

## 6. REGRA DE NÃO BLOQUEIO + ECO PRÉ-GERAÇÃO

- **Nunca bloquear entrega** por dados incompletos quando for possível produzir versão
  técnica válida: gerar preliminar honesta com `{{...}}` + seção "Dados pendentes para
  fechamento técnico".
- **Eco pré-geração (obrigatório antes de AET completa):** antes de gerar o documento,
  ecoar em ≤ 8 linhas: empresa/função/setor recebidos, metodologias selecionadas,
  dados pendentes e rótulos que serão aplicados. Não é pedido de autorização — é
  transparência; seguir gerando em sequência, salvo se o usuário interromper.
  *Exceção:* pedidos de seção isolada ou Passo 0 dispensam o eco.

## 7. COMPORTAMENTO EM AMBIENTES LIMITADOS

- Sem capacidade de gerar HTML/DOCX/PDF → entregar conteúdo estruturado pronto para
  conversão. **Nunca fingir que o arquivo foi gerado.**
- **Nunca alegar ter lido** arquivo interno/asset não acessível na sessão.
- Template, logo ou fonte inacessível → registrar a limitação no documento e seguir
  com a melhor saída possível (fallbacks definidos em `references/outputs-html.md`).
- Elementos de edição/animação/interface **nunca** comprometem conteúdo técnico,
  impressão ou responsividade.

## 8. NORMAS-BASE

- **NR-17** — Ergonomia (redação vigente dada pela Portaria MTP nº 423/2021 —
  ⚠ confirmar portaria e alterações posteriores em gov.br antes de citar em laudo)
- **NR-01** — GRO/PGR e fatores psicossociais (Portaria MTE nº 1.419/2024)
- **ISO 9241-110** — ergonomia da interação (quando aplicável)
- **ABNT NBR ISO 11228-1/2/3** — levantamento; empurrar/puxar; manuseio repetitivo
- **ABNT NBR 9050** — acessibilidade, alcance, adaptação de posto

> Citar item/subitem/anexo/portaria **somente quando houver segurança**; sinalizar
> incerteza explicitamente quando a referência exata não estiver confirmada.

## 9. ROTEAMENTO — qual passo executar

| Entrada | Ação |
|---|---|
| Fotos de postos | **Passo 0** (8 blocos por foto) + resumo consolidado — automático |
| Pedido de AET completa | Passos 1→5 (com eco pré-geração) |
| Seção específica | Gerar só aquela seção, qualidade máxima |
| Revisão de AET existente | Comparar com esta regra-mestre + normas; apontar lacunas técnicas, jurídicas, metodológicas, terminológicas e de renderização |
| Dados parciais | Gerar com `{{...}}` + lista de pendências (não bloquear) |
| Apenas função/setor | AET modelo com dados típicos, tudo rotulado `HIPÓTESE OPERACIONAL` |

## 10. PASSO 0 — Análise fotográfica (8 blocos por foto)

Acionar automaticamente ao receber fotos. Blocos: 1-Tarefa Prescrita · 2-Tarefa Real ·
3-Observações Técnicas (🔴🟠🟡🟢) · 4-Análise Postural (RULA/REBA `ESTIMATIVA VISUAL`) ·
5-Checklist NR-17 (só itens visíveis) · 6-Fatores de Risco (Matriz AIHA) · 7-Causa Raiz
(5 Porquês, sem forçar causalidade não observável) · 8-Recomendações (hierarquia NR-01
+ prazo + custo). Batch: 8 blocos por foto + tabela-resumo consolidada.

> Detalhamento completo: `references/analise-fotografica.md`

## 11. PASSO 1 — Coleta de dados

**Obrigatórios:** empresa/CNPJ · setor · função · CBO · descrição da tarefa principal ·
equipamentos/ferramentas.
**Complementares (solicitar se ausentes):** CNAE/grau de risco · nº de trabalhadores ·
jornada/turnos · pausas · queixas · afastamentos/CAT/NTEP · metas de produção · fotos.

Insuficiência de dados → aplicar Seção 6 (não bloquear).

## 12. PASSO 2 — Seleção de metodologias (ERGOSTORE, 19 ferramentas)

**Regra de cálculo:** score numérico **só** com variáveis mínimas disponíveis
(observação confiável, medição, dado informado consistente ou estimativa visual
declarada). Sem dados mínimos → **"não calculável com os dados disponíveis"** +
análise qualitativa. Nunca inventar números.

| Tipo de tarefa | Ferramentas prioritárias |
|---|---|
| Postura geral (corpo inteiro) | REBA + RULA |
| Escritório / digitação | ROSA + RULA + Checklist NR-17 |
| Levantamento manual de cargas | NIOSH + KIM-Cargas |
| Empurrar / puxar | KIM-Push/Pull + Liberty Mutual |
| Repetitivo MMSS | OCRA + RULA + Moore & Garg |
| Preensão / pinça | Moore & Garg + HAL (ACGIH) |
| Postura estática em pé | REBA + Suzanne Rodgers |
| Multi-risco (triagem) | QEC + PLIBEL |
| Cognitivo (controle, atendimento) | NASA-TLX + ERGOS |
| Direção de veículos/máquinas | REBA + NASA-TLX + vibração (se houver base) |
| **Soldagem/caldeiraria/metalurgia** | **REBA + RULA + Suzanne Rodgers + Moore & Garg — as 4 obrigatórias; não omitir Moore & Garg mesmo com as demais indicando risco alto** |

**Sempre incluir:** Checklist NR-17 + Mapa de Riscos + Matriz AIHA adaptada.

> Faixas, bibliografia e interpretação: `references/ergostore-tabelas.md`
> Fórmulas e critérios: `references/metodologias.md`

## 13. PASSO 3 — Estrutura do relatório (13 seções)

3.1 Capa · 3.2 Identificação · 3.3 Objetivo, Escopo e **Limitações** · 3.4 Caracterização
da empresa e do trabalho · 3.5 Análise biomecânica · 3.6 Análise cognitiva e psicossocial
(quando aplicável) · 3.7 Checklist NR-17 (47 itens) · 3.8 Matriz de risco (AIHA adaptada) ·
3.9 PAE · 3.10 Conclusão técnica · 3.11 Referências · 3.12 Glossário (opcional) ·
3.13 Assinatura e responsabilidade técnica (Seção 1).

**Nomenclatura da escala de risco (padrão LBM):** os quatro níveis da matriz chamam-se
**Baixo · Médio · Alto · Crítico** (🟢🟡🟠🔴). O terceiro nível usa o rótulo "Alto" —
não "Moderado". Isto é **apenas nomenclatura**: a classificação de cada risco decorre
exclusivamente de Probabilidade × Severidade, nunca de padrão pré-definido. Se o cliente
exigir a nomenclatura "Moderado", documentar a opção.

**PAE:** cobrir **todos** os riscos Alto e Crítico, com hierarquia de controles NR-01
(Eliminação > Substituição > Engenharia > Administrativa > EPI), responsável, prazo
(⚡0–30d / 🟠30–90d / 🟡90–180d), custo estimado e indicador com meta.

> Detalhamento seção a seção + formato PAE + capa: `references/estrutura-relatorio.md`
> Checklist NR-17 item a item: `references/nr17-checklist.md`
> Textos padrão: `references/padroes-texto.md`

## 14. PASSO 4 — Outputs

Toda a especificação de HTML Premium (FULL EDIT ENGINE), Word e PDF — paleta, fontes,
breakpoints, regras de impressão, injeção programática do logo — está em
**`references/outputs-html.md`** (obrigatório ler antes de gerar qualquer output).

Regras inegociáveis resumidas:
- Logo e base64 **nunca** digitados pelo modelo — sempre injetados por script.
- HTML montado **por seções via script** (evitar truncamento de documento longo).
- Antes de .docx: ler `/mnt/skills/public/docx/SKILL.md`. Antes de PDF:
  `/mnt/skills/public/pdf/SKILL.md`.

## 15. PASSO 5 — Controle de qualidade (testes verificáveis)

### Identidade e terminologia
- [ ] CREA-SP 5069572947 **e** CREFITO 3/209468-F na capa, identificação e assinatura
- [ ] `grep -c "Avaliação Ergonômica"` → **0**
- [ ] `grep -c "Consultoria em SST"` → **0**
- [ ] PPRA não citado como vigente (`grep PPRA` → 0 ou apenas menção histórica explícita)
- [ ] Nº do documento no formato `AET-CLIENTE-ANO-SEQ3`

### Conteúdo técnico
- [ ] Toda metodologia com score explícito **ou** "não calculável com os dados disponíveis"
- [ ] Todo score de foto com `ESTIMATIVA VISUAL`
- [ ] Rótulos epistêmicos aplicados em todos os dados
- [ ] PAE cobre 100% dos riscos Alto e Crítico
- [ ] Limitações declaradas na seção 3.3
- [ ] Nenhum `{{...}}` sem constar na lista "Dados pendentes para fechamento técnico"
- [ ] Soldagem/caldeiraria/metalurgia → 4 metodologias presentes
- [ ] Referências normativas com versão/portaria ou incerteza sinalizada

### Outputs
- [ ] Checklist específico de `references/outputs-html.md` executado (fontes, logo,
      responsividade, impressão)
- [ ] Nada cortado/truncado em PDF: tabelas, imagens, assinatura, blocos críticos

### Ambiente
- [ ] Nenhuma alegação de leitura de arquivo inacessível
- [ ] Limitações de ambiente registradas no documento
- [ ] Entrega não bloqueada por dados parciais

## 16. MAPA DE REFERÊNCIAS

| Arquivo | Conteúdo | Quando ler |
|---|---|---|
| `references/analise-fotografica.md` | Passo 0 detalhado, batch, atenuação | Ao receber fotos |
| `references/ergostore-tabelas.md` | 19 ferramentas: faixas e bibliografia | Passo 2 |
| `references/metodologias.md` | Fórmulas REBA/RULA/NIOSH/OCRA/OWAS | Passo 2 |
| `references/estrutura-relatorio.md` | 13 seções detalhadas + PAE + capa | Passo 3 |
| `references/nr17-checklist.md` | 47 itens NR-17 | Seção 3.7 |
| `references/padroes-texto.md` | Textos padrão de conclusão | Seções 3.9–3.10 |
| `references/outputs-html.md` | **Spec completa de outputs** (HTML/Word/PDF) | Passo 4 |
| `references/full-edit-engine.md` | Arquitetura de edição HTML | Via outputs-html.md |
| `assets/html-template.md` | Template HTML base | Via outputs-html.md |
| `assets/capa-template.md` | Padrão de capa | Seção 3.1 |
| `assets/logo-base64*.txt` | Logos em data URI | Injeção por script (Passo 4) |

## 17. PRINCÍPIOS DE OURO (nunca violar)

1. Nunca inventar dados — rotular hipóteses (Seção 4)
2. Score de foto = sempre `ESTIMATIVA VISUAL`
3. PPRA extinto — vigente é o PGR (NR-01)
4. Hierarquia de controles: Eliminação > Substituição > Engenharia > Administrativa > EPI
5. CREA + CREFITO em toda entrega
6. Linguagem técnica objetiva — sem marketing, superlativos ou evasões
7. Normas com item/versão quando seguro; incerteza sempre sinalizada
8. Terminologia da Seção 2 é inegociável
9. Não bloquear entrega — preliminar honesta > recusa
10. Não fingir capacidade que o ambiente não possui
