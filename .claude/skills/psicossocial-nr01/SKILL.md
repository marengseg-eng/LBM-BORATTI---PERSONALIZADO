---
name: psicossocial-nr01
description: >
  Gera avaliações completas de Fatores de Riscos Psicossociais para LBM BORATTI
  Consultoria em SST, em conformidade com NR-01 revisada (Portaria MTE 1.419/2024),
  ISO 45003 e legislação trabalhista vigente. Use esta skill SEMPRE que o usuário
  mencionar fatores psicossociais, riscos psicossociais, saúde mental no trabalho,
  burnout, estresse ocupacional, assédio moral, assédio sexual, violência no trabalho,
  PsicoRisk, COPSOQ, JCQ, ITRA, NR-01 psicossocial, gestão de riscos psicossociais,
  adoecimento mental, transtorno mental relacionado ao trabalho, ambiente psicossocial,
  avaliação psicossocial, questionário de clima, ou qualquer variação desses termos.
  Gera: questionário HTML interativo, relatório com dashboard, plano de ação (PGR/NR-01)
  e laudo técnico. Instrumentos: COPSOQ-III, JCQ (Karasek), ITRA. Outputs em HTML
  premium (azul #1a2f4e / laranja #e67e22), Word (.docx) e PDF.
---

# FATORES PSICOSSOCIAIS NR-01 — LBM BORATTI Consultoria em SST

## Identificação Profissional (sempre incluir)
- **Responsável Técnico:** Marcelo Luis Boratti Melo
- **Engenheiro de Segurança do Trabalho** — CREA-SP: 5069572947
- **Fisioterapeuta e Ergonomista** — CREFITO 3/209468-F
- **Empresa:** LBM BORATTI Consultoria em Segurança e Saúde do Trabalho
- **Cidade:** Sertãozinho/SP

---

## Visão Geral

A skill Psicossocial NR-01 cobre o ciclo completo de gestão dos fatores de riscos
psicossociais: identificação (questionário), análise (relatório/dashboard), controle
(plano de ação PGR) e documentação legal (laudo técnico). Baseia-se na NR-01 revisada
(Portaria MTE 1.419/2024), ISO 45003:2021 e nos instrumentos validados COPSOQ-III,
JCQ e ITRA.

---

## PASSO 1 — Coleta de Dados (SEMPRE perguntar antes de gerar)

### Dados obrigatórios para QUALQUER documento
- [ ] **Razão Social** da empresa e CNPJ
- [ ] **Endereço completo**
- [ ] **Número total de empregados**
- [ ] **Setores/departamentos** a avaliar
- [ ] **Instrumento escolhido** (COPSOQ-III, JCQ, ITRA — ou recomendar)

### Dados específicos por módulo
> Consultar seção correspondente abaixo

---

## PASSO 2 — Escolha do Instrumento

Com base no perfil da empresa, recomendar ou confirmar o instrumento:

| Instrumento | Melhor para | Dimensões avaliadas | Nº de itens |
|-------------|------------|---------------------|-------------|
| **COPSOQ-III** | Empresas de médio/grande porte, múltiplos setores | 28 dimensões psicossociais | 40 itens (curto) |
| **JCQ (Karasek)** | Avaliação de demanda-controle-suporte; indústria | Demanda, Controle, Suporte Social | 17-49 itens |
| **ITRA** | Adoecimento relacionado ao trabalho; clínico | 4 inventários: condições, custo humano, prazer-sofrimento, danos | 94 itens |

> Ler `references/instrumentos.md` para versões, validação brasileira e scoring

**Regra geral:**
- Empresa grande, diagnóstico amplo → **COPSOQ-III**
- Foco em organização do trabalho / demanda-controle → **JCQ**
- Suspeita de adoecimento / ação trabalhista → **ITRA** (+ força jurídica)
- Combinação para máxima cobertura → **COPSOQ-III + ITRA**

---

## PASSO 3 — Módulos de Documentos

### MÓDULO A — Questionário de Aplicação (HTML Interativo)
> Ler `references/instrumentos.md` e `assets/html-questionario.md` antes de gerar

**Quando usar:** Aplicação direta para os trabalhadores — presencial ou online

**Dados adicionais necessários:**
- [ ] Instrumento(s) selecionado(s)
- [ ] Setores a incluir no questionário
- [ ] Formato de aplicação (papel impresso vs. digital/link)
- [ ] Anonimato: sempre garantido (obrigatório pela NR-01)

**Estrutura do HTML interativo:**
```
- Capa: logo empresa + logo LBM BORATTI + instruções de preenchimento
- Garantia de anonimato (destaque obrigatório)
- Seção de perfil: setor, função, tempo de empresa, sexo (opcional)
- Perguntas do instrumento com escala Likert (4 ou 5 pontos)
- Barra de progresso
- Botão "Enviar" (download JSON ou submissão)
- Tempo estimado de preenchimento
```

**Especificações técnicas HTML:**
- Escala Likert com botões de rádio estilizados (não checkboxes padrão)
- Cada dimensão em bloco visual separado com cor de fundo suave
- Validação client-side: não permitir envio com questões em branco
- Responsivo para celular (trabalhadores de chão de fábrica)
- Paleta: azul `#1a2f4e`, laranja `#e67e22`, fundo neutro `#f8f9fa`
- Versão para impressão com espaço para marcação manual

---

### MÓDULO B — Relatório de Resultados com Dashboard
> Ler `references/scoring.md` e `references/interpretacao.md` antes de gerar

**Quando usar:** Após coleta dos dados — apresentar resultados à empresa

**Dados adicionais necessários:**
- [ ] Respostas coletadas (planilha, JSON ou dados digitados)
- [ ] Número de respondentes por setor
- [ ] Taxa de resposta (%)
- [ ] Data da coleta

**Estrutura do relatório:**

```
1. IDENTIFICAÇÃO
   - Empresa, período de coleta, instrumento, nº de respondentes

2. METODOLOGIA
   - Instrumento utilizado + referência de validação brasileira
   - Forma de coleta e anonimato garantido
   - Critérios de pontuação e interpretação

3. PERFIL DA AMOSTRA
   - Distribuição por setor, função, tempo de empresa, sexo
   - Taxa de resposta (respondentes / total de empregados)

4. DASHBOARD DE RESULTADOS
   Para cada dimensão avaliada:
   - Score médio (0–100 ou escala do instrumento)
   - Classificação de risco: BAIXO / MÉDIO / ALTO / CRÍTICO
   - Gráfico de barras horizontal por dimensão
   - Comparativo por setor (se aplicável)
   - Semáforo de risco: 🟢 Baixo | 🟡 Médio | 🟠 Alto | 🔴 Crítico

5. ANÁLISE INTERPRETATIVA
   - Dimensões de maior risco (Top 5)
   - Padrões identificados (ex.: alto controle + alta demanda)
   - Relação com indicadores organizacionais (absenteísmo, turnover, se disponíveis)
   - Setores mais críticos

6. CONCLUSÃO TÉCNICA
   - Nível geral de risco psicossocial da empresa
   - Prioridades de intervenção
   - Necessidade de avaliação complementar

7. REFERÊNCIAS NORMATIVAS
   - NR-01, ISO 45003, instrumento utilizado

8. ASSINATURA RT
```

**Especificações do Dashboard HTML:**
- Gráfico de barras horizontais com Chart.js ou SVG puro
- Código de cores consistente com classificação de risco
- Tabela resumo com todas as dimensões e seus scores
- Seção de impressão otimizada (`@media print`)
- Botão "Exportar PDF"

---

### MÓDULO C — Plano de Ação Psicossocial (PGR — NR-01)
> Ler `references/plano-acao.md` antes de gerar

**Quando usar:** Após relatório — formalizar no PGR as medidas de controle

**Base legal:** NR-01 item 1.5.3 — o PGR deve incluir fatores psicossociais como
categoria de risco a ser gerenciada, com inventário, plano de ação e monitoramento.

**Estrutura do Plano de Ação:**

Para cada dimensão classificada como ALTO ou CRÍTICO, gerar:

```
FATOR DE RISCO: [dimensão — ex.: "Exigências Quantitativas Elevadas"]
SETOR(ES) AFETADO(S): [lista]
SCORE IDENTIFICADO: [valor] — Risco [ALTO/CRÍTICO]
DESCRIÇÃO: [o que foi identificado]

MEDIDAS DE CONTROLE:
  Nível 1 — Organizacionais (prioritárias):
    [ ] [medida específica]
  Nível 2 — Relacionais/Grupais:
    [ ] [medida específica]
  Nível 3 — Individuais (suporte):
    [ ] [medida específica]

RESPONSÁVEL: [cargo]
PRAZO: Imediato (0-30d) / Curto (30-90d) / Médio (90-180d) / Longo (180-360d)
INDICADOR DE MONITORAMENTO: [métrica objetiva]
REAVALIAÇÃO: [data prevista]
```

**Hierarquia de controles para riscos psicossociais (ISO 45003):**
1. Eliminar o fator (ex.: eliminar trabalho em isolamento)
2. Reduzir a exposição (ex.: limitar horas extras)
3. Controles organizacionais (ex.: política de não-perturbação fora do horário)
4. Controles relacionais (ex.: programa de apoio entre pares)
5. Controles individuais (ex.: programa de manejo do estresse)

---

### MÓDULO D — Laudo Técnico Psicossocial
> Ler `references/laudo-tecnico.md` antes de gerar

**Quando usar:**
- Ação trabalhista envolvendo doença mental ocupacional
- Processo de afastamento por burnout/transtorno de ansiedade
- Investigação de acidente com componente psicossocial
- Autuação fiscal ou procedimento do MPT

**Dados adicionais necessários:**
- [ ] Finalidade do laudo (processo judicial, administrativo, preventivo)
- [ ] Reclamante/trabalhador (se processo judicial): nome + função + período
- [ ] Diagnóstico clínico (CID-10/CID-11) se disponível
- [ ] Condições de trabalho identificadas
- [ ] Documentos disponíveis (questionário aplicado, relatório, prontuários)

**Estrutura do Laudo:**

```
1. QUALIFICAÇÃO DO PERITO/AT
   - BORATTI com dupla credencial (CREA + CREFITO)
   - Habilitação em ergonomia e saúde do trabalho

2. OBJETO E FINALIDADE DO LAUDO

3. DOCUMENTOS ANALISADOS

4. METODOLOGIA
   - Instrumento(s) utilizado(s) com referência de validação
   - NR-01, ISO 45003, CID-11 (reconhece burnout como fenômeno ocupacional)

5. CONDIÇÕES PSICOSSOCIAIS IDENTIFICADAS
   - Resultados por dimensão com scores
   - Comparativo com benchmarks nacionais/internacionais

6. ANÁLISE DO NEXO CAUSAL (quando aplicável)
   - Diagnóstico clínico × condições de trabalho identificadas
   - NTEP: CID × CNAE (Lista B INSS)
   - Fatores extralaborais considerados

7. CONCLUSÃO TÉCNICA
   - Há ou não fatores de risco psicossocial acima do aceitável?
   - Há nexo causal entre as condições de trabalho e o adoecimento?
   - Recomendações

8. BASE NORMATIVA
   - NR-01 (Portaria MTE 1.419/2024)
   - ISO 45003:2021
   - CID-11 (Z73, F43.8, F32 etc.)
   - Lei 8.213/91 Art. 20 e 21-A (NTEP)

9. ASSINATURA COM CREDENCIAIS COMPLETAS
```

---

## PASSO 4 — Geração dos Outputs

### Output 1: HTML Premium
- Paleta: azul `#1a2f4e`, laranja `#e67e22`, cinza `#f5f5f5`
- Questionário: responsivo, escala Likert estilizada, validação JS
- Relatório: gráficos SVG/Chart.js, semáforos de risco coloridos
- Plano de ação: cards por fator de risco com badges de prioridade
- Laudo: numeração de parágrafos, citações em destaque
- Todos: botão PDF, `@page { size: A4; margin: 20mm }`, `print-color-adjust: exact`

### Output 2: Word (.docx)
- Ler `/mnt/skills/public/docx/SKILL.md` antes de gerar
- Estilos consistentes, tabelas de plano de ação formatadas
- Cabeçalho LBM BORATTI, rodapé com credenciais RT

### Output 3: PDF
- Ler `/mnt/skills/public/pdf/SKILL.md` antes de gerar
- Metadados: autor = Marcelo Luis Boratti Melo

---

## PASSO 5 — Controle de Qualidade

- [ ] Instrumento identificado com versão e referência de validação brasileira
- [ ] Anonimato dos respondentes garantido (declaração explícita no documento)
- [ ] Scores calculados conforme metodologia do instrumento
- [ ] Todas as dimensões classificadas com nível de risco
- [ ] Plano de ação cobre todos os riscos ALTO/CRÍTICO
- [ ] Base normativa: NR-01 + ISO 45003 presentes
- [ ] Credenciais RT presentes (CREA + CREFITO)
- [ ] Para laudos: nexo causal claramente argumentado ou negado
- [ ] Nenhuma referência a PPRA (extinto — usar PGR)

---

## Comportamento Padrão

1. **Empresa + instrumento** → Gerar questionário HTML imediatamente
2. **Dados de respostas fornecidos** → Calcular scores e gerar relatório/dashboard
3. **"Fazer o plano de ação"** → Perguntar quais dimensões ficaram em ALTO/CRÍTICO
4. **Ação trabalhista mencionada** → Acionar Módulo D (laudo técnico)
5. **Dúvida sobre instrumento** → Recomendar com base no perfil da empresa
6. **"Kit completo psicossocial"** → Gerar os 4 módulos em sequência

---

## Referências

- `references/instrumentos.md` — COPSOQ-III, JCQ e ITRA: versões, itens, escala, validação BR
- `references/scoring.md` — Metodologia de cálculo de scores por instrumento
- `references/interpretacao.md` — Benchmarks, pontos de corte e classificação de risco
- `references/plano-acao.md` — Medidas de controle por dimensão e hierarquia ISO 45003
- `references/laudo-tecnico.md` — Estrutura detalhada, nexo causal, CID-11, NTEP
- `references/base-normativa.md` — NR-01 revisada, ISO 45003, legislação trabalhista
- `assets/html-questionario.md` — Template HTML do questionário interativo
