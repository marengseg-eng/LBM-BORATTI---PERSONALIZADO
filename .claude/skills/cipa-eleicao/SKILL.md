---
name: cipa-eleicao
description: >
  Gera documentos completos de CIPA — Comissão Interna de Prevenção de Acidentes e de
  Assédio (CIPA+A) para LBM BORATTI Consultoria em SST, conforme NR-05 vigente
  (Portaria MTP nº 422/2021 e alterações da Portaria MTP nº 4.219/2022 — Lei 14.457/2022).
  Use esta skill SEMPRE que o usuário mencionar CIPA, CIPA+A, eleição de CIPA, edital,
  ata de eleição, ata de posse, ata de reunião mensal, SIPAT, treinamento NR-05,
  calendário CIPA, mapa de riscos, designado de segurança, representante da NR-05,
  cipeiro, mandato CIPA, canal de denúncias de assédio, Lei 14.457, prevenção ao
  assédio sexual no trabalho, ou qualquer variação desses termos. Também acionar
  quando mencionar clientes que precisam organizar ou renovar a CIPA. Cobre: processo
  eleitoral completo (edital → posse), gestão anual (reuniões + atas), SIPAT e
  treinamento obrigatório NR-05 com CH variável por GR (8h/12h/16h/20h). Gera outputs
  em HTML premium (azul #1a2f4e / laranja #e67e22), Word (.docx) e PDF prontos para uso.
---

# 🛡️ CIPA+A / ELEIÇÃO — LBM BORATTI Consultoria em SST

## 👤 Identificação Profissional (sempre incluir em todos os documentos)
- **Responsável Técnico:** Marcelo Luis Boratti Melo
- **Engenheiro de Segurança do Trabalho** — CREA-SP: 5069572947
- **Fisioterapeuta e Ergonomista** — CREFITO 3/209468-F
- **Empresa:** LBM BORATTI Consultoria em Segurança e Saúde do Trabalho
- **Cidade:** Sertãozinho/SP
- **Contato:** marengseg@gmail.com | (16) 99338-8989

---

## ⚖️ Base Legal Vigente (CITAR EXATAMENTE ASSIM)

- **NR-05** — Comissão Interna de Prevenção de Acidentes **e de Assédio** — CIPA
- **Portaria MTP nº 422**, de 07 de outubro de 2021 (vigência desde 03/01/2022)
- **Portaria MTP nº 4.219**, de 20 de dezembro de 2022 (incluiu "de Assédio" no nome e
  conteúdo programático sobre assédio sexual e outras violências no trabalho)
- **Lei nº 14.457/2022** (Programa Emprega + Mulher — canal de denúncias obrigatório)
- **CLT**, arts. 163 a 165 (constituição e estabilidade)
- **Integração com NR-01** — PGR e ordens de serviço (itens 5.3.1.a/b, 5.9.1)

> ⚠️ **NUNCA** citar "Portaria MTE 8.213/2021" (não existe). **NUNCA** omitir o
> "e de Assédio" no nome da CIPA — é obrigatório desde 22/12/2022.

---

## 📋 Visão Geral

A skill CIPA+A gera toda a documentação do ciclo de vida da comissão: do edital de
convocação até as atas mensais, SIPAT, certificados de treinamento e política de
prevenção ao assédio. Todos os documentos seguem rigorosamente a NR-05 vigente,
Lei 14.457/2022 e são formatados para validade jurídica e visual profissional
padrão LBM BORATTI.

---

## 1️⃣ PASSO 1 — Coleta de Dados (SEMPRE perguntar antes de gerar)

### 📌 Dados obrigatórios para QUALQUER documento CIPA
- [ ] **Razão Social** da empresa e CNPJ
- [ ] **Endereço completo** (rua, número, bairro, cidade/UF, CEP)
- [ ] **CNAE principal** (ou ramo de atividade)
- [ ] **Número total de empregados** (para determinar Quadro I)
- [ ] **Grau de Risco** (GR 1, 2, 3 ou 4 — conforme Quadro I NR-04)
- [ ] **Nome do representante legal** (diretor/proprietário) e cargo
- [ ] **Data de término do mandato atual** (se houver CIPA em vigor)

### 🔍 Dados específicos por tipo de documento
> Consultar seção correspondente abaixo para dados adicionais necessários.

---

## 2️⃣ PASSO 2 — Dimensionamento da CIPA (Quadro I NR-05 vigente)

### 🚦 Regra de obrigatoriedade (decorrente do Quadro I atual)
- 🟢 **GR 1:** CIPA obrigatória a partir de **81 empregados**
- 🟡 **GR 2:** CIPA obrigatória a partir de **51 empregados**
- 🟠 **GR 3 e** 🔴 **GR 4:** CIPA obrigatória a partir de **20 empregados**
- ⚠️ **Abaixo dessas faixas:** nomear **Representante da NR-05** (item 5.4.13), não
  há eleição — há **Portaria de Nomeação** anual

### ⚖️ Paridade
A CIPA é **paritária**: o Quadro I da NR-05 indica o número de representantes
**dos empregados** (eleitos). O empregador designa **a mesma quantidade** de
representantes, sem eleição.

**Total de membros = 2 × (efetivos do Quadro I) + 2 × (suplentes do Quadro I)**

> 📖 Tabela completa e exemplos calculados em `references/dimensionamento.md`

### 🚫 MEI
Microempreendedor Individual é dispensado (item 5.4.13.2).

---

## 3️⃣ PASSO 3 — Módulos de Documentos

### 🗳️ MÓDULO A — Processo Eleitoral Completo
> 📖 Ver `references/processo-eleitoral.md` para prazos e sequência legal (item 5.5)

Documentos gerados em ordem cronológica:

```
1.  Comunicado de Abertura do Processo Eleitoral (D-60, mínimo)
2.  Comunicação ao Sindicato sobre início do processo (item 5.5.1.1)
3.  Edital de Convocação da Eleição
4.  Formulário de Inscrição de Candidatos
5.  Comunicado de Candidatos Habilitados
6.  Cédula de Votação
7.  Ata de Eleição e Apuração de Votos (eleição no mínimo D-30)
8.  Comunicado do Resultado da Eleição
9.  Ofício ao Sindicato com Resultado
10. Ata de Instalação e Posse da CIPA+A (1º dia útil após término do mandato)
11. Designação dos Representantes do Empregador (Presidente incluso)
12. Calendário Anual de Reuniões Ordinárias
```

**Dados adicionais necessários para o processo eleitoral:**
- [ ] Data de término do mandato atual (define todo o cronograma)
- [ ] Nome e cargo dos candidatos (se já definidos)
- [ ] Nome dos representantes do empregador (indicados pela empresa)
- [ ] Duração do mandato: **1 ano, permitida uma reeleição** (item 5.4.6)

---

### 💼 MÓDULO B — Gestão Anual: Reuniões e Atas

Documentos gerados:

```
1. Ata de Reunião Ordinária Mensal (ME/EPP GR1-GR2: pode ser bimestral)
2. Ata de Reunião Extraordinária (acidente grave/fatal ou solicitação)
3. Lista de Presença
4. Pauta da Reunião
5. Relatório Anual de Atividades da CIPA+A
6. Mapa de Riscos (item 5.3.1.b — integrado ao PGR)
7. Plano de Trabalho da CIPA+A (item 5.3.1.d)
```

**Regras importantes (NR-05):**
- Reuniões mensais; ME/EPP GR1-GR2 podem ser bimestrais (item 5.6.1.1)
- Titular que faltar a mais de **4 reuniões ordinárias sem justificativa** perde
  o mandato (item 5.6.6)
- Atas disponibilizadas a integrantes e decisões afixadas aos empregados
- Participação remota permitida (item 5.6.2)

**Dados adicionais necessários:**
- [ ] Número da reunião (ex.: 1ª Reunião Ordinária)
- [ ] Data, horário e local (ou link remoto)
- [ ] Membros presentes e ausentes (justificados ou não)
- [ ] Pauta tratada
- [ ] Deliberações (com responsável + prazo)
- [ ] Data da próxima reunião

---

### 🎉 MÓDULO C — SIPAT (Semana Interna de Prevenção de Acidentes do Trabalho)

Documentos gerados:

```
1. Planejamento e Cronograma da SIPAT
2. Convite/Comunicado Interno
3. Lista de Presença por atividade
4. Ata de Encerramento da SIPAT
5. Relatório Final da SIPAT
6. Certificado de Participação
```

**Base:** item 5.3.1.i — SIPAT **anual**, organizada pela CIPA+A com SESMT (quando houver).

**Recomendação LBM BORATTI:** incluir ao menos 1 atividade sobre prevenção ao
assédio sexual/moral e outras violências (atende item 5.3.1.j + Lei 14.457).

**Dados adicionais necessários:**
- [ ] Datas da SIPAT (início e fim — mínimo 1 dia, recomendado 3-5 dias)
- [ ] Atividades programadas (palestras, dinâmicas, simulados)
- [ ] Palestrantes/facilitadores (nome e tema)
- [ ] Tema central da SIPAT

---

### 🎓 MÓDULO D — Treinamento Obrigatório NR-05 (CH variável por GR)

**⏱️ Carga horária mínima (item 5.7.4):**

| Grau de Risco | CH Mínima Total | CH Presencial Mínima (se EAD) |
|---------------|-----------------|-------------------------------|
| 🟢 GR 1       | **8 horas**     | Pode ser integralmente EAD    |
| 🟡 GR 2       | **12 horas**    | 4 horas presenciais           |
| 🟠 GR 3       | **16 horas**    | 8 horas presenciais           |
| 🔴 GR 4       | **20 horas**    | 8 horas presenciais           |

**Regras:**
- Máximo **8h diárias** (item 5.7.4.1)
- Treinamento de **1º mandato:** prazo máximo **30 dias após a posse** (5.7.1.1)
- Treinamento realizado há menos de **2 anos** pode ser aproveitado na mesma
  organização (item 5.7.3)
- Representante da NR-05 (designado): **8h mínimas**
- Integrante do SESMT: dispensado do treinamento (item 5.7.4.5)

Documentos gerados:

```
1. Programa do Treinamento (conteúdo programático conforme CH do GR)
2. Lista de Presença (modelo por dia/módulo)
3. Avaliação de Aprendizagem (questionário)
4. Gabarito da Avaliação
5. Certificado de Conclusão (individual, com CH correta para o GR)
6. Registro de Treinamento (para arquivo NR-01 item 1.7)
```

**Conteúdo programático mínimo obrigatório (item 5.7.2):**
> Ver `references/conteudo-treinamento-nr05.md` para programa completo detalhado

Inclui **obrigatoriamente** (alínea "h" inserida pela Portaria 4.219/2022):
**prevenção e combate ao assédio sexual e a outras formas de violência no trabalho.**

**Dados adicionais necessários:**
- [ ] Lista de participantes (nome completo + função)
- [ ] GR do estabelecimento (define a CH)
- [ ] Modalidade (presencial / semipresencial / EAD)
- [ ] Datas e carga horária por módulo
- [ ] Local do treinamento (se presencial) ou plataforma (se EAD)
- [ ] Instrutor (BORATTI como responsável técnico)

---

### 🛡️ MÓDULO E — Política Antiassédio e Canal de Denúncias (Lei 14.457/2022)

**Obrigatório para empresas com CIPA desde 21/03/2023.**

Documentos gerados:

```
1. Política Interna de Prevenção ao Assédio Sexual e Violência no Trabalho
2. Procedimento de Canal de Denúncias (com garantia de anonimato)
3. Código de Conduta (complementar)
4. Comunicado aos Empregados sobre o Canal
5. Registro de Tratamento de Denúncias (modelo)
```

**Dados adicionais necessários:**
- [ ] Canal escolhido (e-mail dedicado, plataforma, ombudsman, hotline)
- [ ] Responsável(is) pela apuração
- [ ] Prazo interno para resposta/apuração
- [ ] Medidas disciplinares previstas no regulamento interno

---

## 4️⃣ PASSO 4 — Geração dos Outputs

### 🖥️ Output 1: HTML Premium (padrão LBM BORATTI)
- Paleta: azul-marinho `#1a2f4e`, laranja `#e67e22`, cinza claro `#f5f5f5`
- Cada documento em seção separada com `<div class="documento">`
- Cabeçalho com logo LBM BORATTI + dados da empresa cliente
- Rodapé com credenciais RT em todas as páginas impressas
- Campos de assinatura formatados (linha + nome + cargo)
- Botão "Imprimir / Exportar PDF" com `window.print()`
- CSS `@media print`: `@page { size: A4; margin: 20mm }`, `print-color-adjust: exact`
- Quebra de página entre documentos: cada seção A4 com `height: 297mm`,
  `overflow: hidden`, `page-break-after: always`, `break-after: page`
- Numeração de documento: `CIPA-[EMPRESA]-[ANO]-[MÓDULO]-[SEQ]`
- Todos os campos `contenteditable="true"` para edição rápida

### 📄 Output 2: Word (.docx)
- Ler `/mnt/skills/public/docx/SKILL.md` antes de gerar
- Documento por arquivo ou todos em um único .docx com quebras de seção
- Cabeçalho: logo LBM BORATTI | Rodapé: credenciais RT + número do documento
- Campos de assinatura com linhas formatadas

### 🖨️ Output 3: PDF
- Ler `/mnt/skills/public/pdf/SKILL.md` antes de gerar
- Derivado do HTML via impressão Chrome
- Um PDF por módulo ou PDF unificado com marcadores

---

## 5️⃣ PASSO 5 — Controle de Qualidade (Checklist de saída)

Antes de entregar, verificar:

- [ ] **Nome correto:** "Comissão Interna de Prevenção de Acidentes **e de Assédio** — CIPA"
- [ ] **Base legal correta:** Portaria MTP nº 422/2021 + MTP nº 4.219/2022 (nunca "8.213/2021")
- [ ] **Dimensionamento paritário:** empregador = empregados; começa em 81/51/20 conforme GR
- [ ] **Cronograma:** convocação ≥ D-60; inscrição mínima 15 dias corridos; eleição ≥ D-30
- [ ] **CH do treinamento:** 8h (GR1) / 12h (GR2) / 16h (GR3) / 20h (GR4) — nunca fixa em 20h
- [ ] **Conteúdo do treinamento:** inclui alínea "h" (prevenção ao assédio sexual/violência)
- [ ] **Canal de denúncias** referenciado (Lei 14.457/2022)
- [ ] **Integração com PGR (NR-01)** sinalizada (itens 5.3.1.a/b, 5.9.1)
- [ ] Dados da empresa corretos (Razão Social, CNPJ, endereço)
- [ ] Credenciais RT presentes (CREA + CREFITO)
- [ ] Campos de assinatura para todos os signatários obrigatórios
- [ ] Numeração de documento gerada
- [ ] Nenhum campo em branco sem marcação `[INSERIR DADO]`

---

## 🎯 Comportamento Padrão

1. **Módulo especificado + dados completos** → Gerar documentos do módulo em HTML premium
   (outputs .docx/PDF só quando solicitado explicitamente — economiza tokens)
2. **"Fazer CIPA" sem especificação** → Perguntar: empresa obrigada a CIPA ou apenas
   Representante da NR-05? Qual módulo precisa primeiro (eleitoral, gestão, SIPAT, treinamento)?
3. **Apenas nome da empresa** → Perguntar: CNPJ, nº empregados, GR e módulo desejado
4. **Pedido de documento único** (ex.: "ata de reunião") → Gerar apenas aquele documento
5. **Pedido de kit completo** → Gerar todos os módulos em sequência lógica
6. **Obras ≤ 180 dias** → Informar que está dispensada de CIPA; aplicar Anexo I (construção)

---

## ⛔ Quando NÃO usar esta skill

- **Impugnação de eleição de CIPA em processo judicial** → usar `impugnador-pericial`
- **Perícia trabalhista sobre insalubridade/periculosidade** → usar `pericia-trabalhista`
- **PGR / PCMSO / LTCAT completos** → usar `gestao-sst-completa`
- **Riscos psicossociais (NR-01)** → usar `psicossocial-nr01`
- **AET / ergonomia** → usar `aet-premium`

---

## 📚 Referências

- `references/dimensionamento.md` — Quadro I NR-05 vigente + exemplos calculados
- `references/processo-eleitoral.md` — Cronograma legal completo (item 5.5)
- `references/conteudo-treinamento-nr05.md` — Programa por CH (8h/12h/16h/20h)
- `templates/modelos-documentos.md` — Texto padrão de todos os documentos (edital,
  atas, certificado, política antiassédio) em formato Markdown para rápida conversão
  em HTML premium
