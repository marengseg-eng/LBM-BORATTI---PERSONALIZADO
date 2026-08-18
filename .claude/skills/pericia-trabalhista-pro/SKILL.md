---
name: pericia-trabalhista-pro
description: >
  Skill AUTOSSUFICIENTE de Perícia Trabalhista (LBM BORATTI / SST). Use SEMPRE que
  mencionar: perícia, laudo pericial, impugnar laudo, contestar perícia, manifestação
  técnica, assistente técnico, quesitos, parecer divergente, vistoria pericial, vícios
  do laudo, falha metodológica, atenuação de EPI, "vide laudo", Art. 473/477/479/480
  CPC, insalubridade, periculosidade, nexo causal, DORT, LER, NR-15, NR-16, NR-17,
  NHO-01/06/07/08, ruído, calor, agentes químicos, agentes biológicos, ergonomia,
  reclamatória, TST, TRT, Súmula 289, Súmula 448, ou enviar PDF de laudo para analisar.
  Cobre 4 módulos: IMPUGNAÇÃO (pós-laudo), QUESITOS (pré/pós-laudo), PARECER preventivo
  (pré-ação) e VISTORIA pericial. Aplicar PASSO 0 (classificação de agentes) e PASSO 0-B
  (verificação de Súmula/OJ no TST e NR vigente) antes de qualquer módulo. Outputs:
  HTML premium (azul #1a2f4e / laranja #e67e22, contenteditable) + Word (.docx).
---

# PERÍCIA TRABALHISTA PRO — LBM BORATTI

**Versão:** 3.0.0 (autossuficiente) · Histórico em `CHANGELOG.md`.

> Esta skill é **autocontida**: todo o conteúdo operacional (classificação de agentes,
> vetores, módulos, fundamentação, outputs) está neste arquivo. Não depende de arquivos
> externos para funcionar. Não invocar `modules/`, `references/` ou `templates/` —
> foram consolidados aqui.

---

## 1. IDENTIFICAÇÃO PROFISSIONAL (incluir em todos os documentos)

```
Responsável Técnico: Marcelo Luis Boratti Melo
Engenheiro de Segurança do Trabalho — CREA-SP: 5069572947
Fisioterapeuta e Ergonomista — CREFITO 3/209468-F
LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
Sertãozinho/SP • marengseg@gmail.com • (16) 99338-8989
```

> **Razão social — forma única e obrigatória:** "LBM BORATTI — Consultoria
> **Personalizada** em Segurança e Saúde **no** Trabalho". Nunca "do Trabalho",
> nunca "Consultoria em SST". Em peça que vai a juízo, razão social divergente do
> registro é flanco de impugnação pela parte contrária.

A dupla habilitação (CREA + CREFITO) confere ao AT legitimidade simultânea para
agentes físicos/químicos/biológicos (CREA) e ergonômicos/DORT (CREFITO) — destacar
na qualificação de cada documento (é diferencial técnico real perante o juízo).

---

## 2. PASSO 0 — CLASSIFICAÇÃO DE AGENTES (ler antes de qualquer módulo)

**REGRA ABSOLUTA:** confirmar o agente, o anexo aplicável e o tipo de avaliação
(QUANTITATIVA × QUALITATIVA) **antes** de aplicar qualquer exigência técnica. Errar
essa classificação invalida toda a argumentação e desacredita o AT.

### Tabela-mestre NR-15 (insalubridade)

| Anexo NR-15 | Agente | Avaliação | NHO/critério |
|---|---|---|---|
| 1 | Ruído contínuo/intermitente | **QUANTITATIVA** | NHO-01 |
| 2 | Ruído de impacto | **QUANTITATIVA** | NHO-01 |
| 3 | Calor | **QUANTITATIVA** (IBUTG) | NHO-06 |
| 5 | Radiações ionizantes | **QUANTITATIVA** | norma específica |
| 6 | Trabalho sob ar comprimido | QUALITATIVA (inspeção) | — |
| 7 | Radiações não-ionizantes | QUALITATIVA | — |
| 8 | **Vibração** | **QUANTITATIVA** | NHO-09 (corpo inteiro) / NHO-10 (mãos-braços) |
| 9 | Frio | QUALITATIVA | — |
| 10 | Umidade | QUALITATIVA (inspeção) | — |
| 11 | Agentes químicos com LT | **QUANTITATIVA** | NHO-07/08 |
| 12 | Poeiras minerais (asbesto, sílica) | **QUANTITATIVA** | norma específica |
| 13 | Agentes químicos (avaliação qualitativa) | QUALITATIVA | — |
| 13-A | Benzeno | QUALITATIVA (PPEOB/inspeção) | — |
| 14 | Agentes biológicos | **QUALITATIVA** | — |

> **⚠ Anexo 8 (Vibração) é QUANTITATIVO** — erro comum é tratá-lo como qualitativo.
> **⚠ Anexo 13 vs 11:** o 13 é qualitativo (lista de atividades); o 11 é quantitativo
> (limite de tolerância). Não confundir.

### Erros típicos a atacar (ou evitar cometer)
- Exigir medição para agente qualitativo (Anexo 14 biológicos, p. ex.)
- Usar "área de risco" (conceito de **NR-16/periculosidade**) em manifestação de
  **insalubridade** (NR-15)
- Aplicar limite de tolerância a agente qualitativo
- Comparar com TLV-ACGIH quando a NR-15 tem tabela/limite próprio
- Confundir critério **q=5** (dobra de dose NR-15/insalubridade) com **q=3**
  (critério NHO-01/previdenciário)

---

## 3. PASSO 0-B — VERIFICAÇÃO NORMATIVA OBRIGATÓRIA

A legislação de SST muda com frequência. **Antes de citar em documento final qualquer
Súmula/OJ do TST ou qualquer limite/critério da NR-15/NR-16, confirmar via web_search:**

1. **Redação vigente da Súmula/OJ** no site oficial do TST (`jurisprudencia.tst.jus.br`).
   Nunca citar de memória.
2. **Versão vigente da NR** no `gov.br/MTE`.

### Atualizações normativas confirmadas (fontes oficiais — jul/2026)

| Portaria | O que faz (redação correta) | Vigência |
|---|---|---|
| **MTE nº 1.411/2025** (22/08/2025, DOU 25–26/08/2025) | Aprova o **Anexo VI da NR-16** — Atividades Perigosas dos **Agentes das Autoridades de Trânsito**. Regulamenta a Lei 14.684/2023 (inciso III do art. 193 CLT). | Em vigor desde a publicação |
| **MTE nº 2.021/2025** (03/12/2025, DOU 04/12/2025) | Aprova o **Anexo V da NR-16** — Atividades Perigosas em **Motocicletas** (motoboys, motofretistas). Insere item **15.4.1.3 na NR-15** e **16.3.1 na NR-16**: laudos de insalubridade/periculosidade devem ficar disponíveis a trabalhadores, sindicatos e inspeção do trabalho. | Anexo V e itens: **120 dias após 04/12/2025 → abril/2026** |

> **⚠ Correção histórica (v3.0):** versões anteriores desta skill descreviam a Portaria
> 2.021/2025 como "modificação da NR-15" e o Anexo V como sendo da NR-15. **Errado.**
> O Anexo V (motocicletas) e o Anexo VI (agentes de trânsito) são ambos da **NR-16**.
> Sempre reconfirmar no gov.br antes de citar — normas posteriores podem ter alterado.

**Marcação de incerteza:** toda Súmula/OJ não confirmada nesta sessão recebe o marcador
`[CONFERIR TST]` no rascunho. O QA final (Passo 6) exige **zero** marcadores no documento
entregue.

**Ancoragem segura:** ancorar o argumento no **texto da própria NR** (base estável) e
usar jurisprudência como reforço, nunca como fundamento único.

---

## 4. REGRA DE PREMISSAS EXPLÍCITAS (antes de redigir Módulos A–D)

Antes de redigir qualquer documento, apresentar bloco **"PREMISSAS DA ANÁLISE"**
(máx. 8 linhas) e **aguardar validação de Boratti**:

1. Módulo selecionado e gatilho da árvore de decisão
2. Agente + anexo NR-15/NR-16 + tipo de avaliação (quant/qual)
3. Fase processual (preventiva / pré-laudo / pós-laudo)
4. Base normativa e jurisprudencial a usar (com status do PASSO 0-B)
5. Dados confirmados **vs.** dados assumidos (separar claramente)
6. Lacunas de informação que limitam a análise

**NÃO se aplica** a perguntas pontuais (consulta de limite, dúvida normativa,
esclarecimento conceitual) — nesses casos, responder direto, sem bloco.

*Objetivo: auditabilidade. Premissa errada detectada aqui custa 1 minuto; detectada
no documento pronto, custa o retrabalho inteiro.*

---

## 5. ÁRVORE DE DECISÃO — qual módulo acionar

```
FASE PREVENTIVA (antes da ação)
  └─ Documentar condições reais de trabalho          → MÓDULO C (Parecer)

FASE PRÉ-LAUDO (perícia agendada/em curso)
  ├─ Formular quesitos para o perito                 → MÓDULO B (Quesitos)
  └─ Acompanhar vistoria do perito do juízo          → MÓDULO D (Vistoria)

FASE PÓS-LAUDO (laudo emitido)
  ├─ Laudo desfavorável → contestar tecnicamente     → MÓDULO A (Impugnação)
  └─ Pedir esclarecimentos (Art. 477 CPC)            → MÓDULO B (Quesitos)
```

| Trigger semântico | Módulo |
|---|---|
| "Impugnar laudo de [agente]", "contestar perícia", envio de PDF de laudo | **A — Impugnação** |
| "Gerar quesitos", "quesitos pré-perícia", "Art. 477 CPC" | **B — Quesitos** |
| "Parecer preventivo", "blindagem antes de ação" | **C — Parecer** |
| "Acompanhei a vistoria", "relatório de vistoria" | **D — Vistoria** |

Objetivo ambíguo → perguntar antes de iniciar. Não presumir.

---

## 6. PASSO 1 — Coleta de dados

### Obrigatórios (qualquer módulo)
Nº do processo · Vara/Tribunal · Reclamante (nome + função) · Reclamada (razão social +
CNPJ) · Agente(s)/tema · Período reclamado (admissão/demissão) · Pedido do reclamante
(insalubridade grau X / periculosidade / DORT / danos morais).

### Adicionais — Módulo A (Impugnação)
Laudo pericial (PDF/texto — **ler integralmente antes de redigir**) · Perito do Juízo
(nome + habilitação) · Conclusão do perito (deferiu/indeferiu, grau, período) ·
Documentos da empresa (LTCAT, PGR, fichas de EPI, medições).

> Laudo ausente → "O laudo pericial não foi localizado. Favor enviar o PDF ou colar o
> texto integral para análise." Não redigir impugnação sem o laudo.

---

## 7. PASSO 2 — Vetores A–E (análise sistemática, todos os módulos)

### VETOR A — Vícios Metodológicos (maior impacto processual)
Tempo de amostragem × jornada (NHO-01 para ruído) · representatividade da condição
operacional no dia · equipamento adequado (dosímetro × decibelímetro; IBUTG para calor) ·
calibração laboratorial (validade, certificado, rastreabilidade RBC) · calibração de
campo (pré/pós) · memória de cálculo presente · metodologia descrita e fundamentada no
NHO · perito com habilitação adequada ao agente (CPC Art. 156).

### VETOR B — Erros de Aplicação Normativa
Anexo NR-15/NR-16 correto · limite de tolerância × nível de ação · grau de insalubridade
correto (mín/méd/máx) · critério q=5 (NR-15) × q=3 (NHO-01) · regime trabalho×descanso
(calor, Anexo 3) · classificação da atividade (leve/moderada/pesada).

### VETOR C — Análise de EPI (CLT Art. 191, II + Súmula 289 TST `[CONFERIR TST]`)
EPI identificado com CA/modelo/fabricante · cálculo de atenuação (NRRsf/NIOSH) · fichas
de entrega assinadas · treinamento de uso comprovado · fiscalização do uso efetivo ·
durabilidade/vida útil fundamentada · perito ignorou EPI documentado → argumento direto.

> **Súmula 289 (elisão da insalubridade por EPI):** o fornecimento do EPI não elide
> automaticamente a insalubridade; exige comprovação de uso efetivo e eficaz. Confirmar
> redação vigente no TST antes de citar.

### VETOR D — Omissões e Lacunas
Ciclo de trabalho detalhado (tempos por tarefa) · fontes geradoras identificadas ·
histórico de medições (LTCAT/PGR) · exames ocupacionais (audiometrias, espirometrias) ·
condição de produção no dia × habitual.

### VETOR E — Questões Processuais
Prescrição quinquenal · respostas conclusivas do perito (Art. 473, IV CPC) · perito
respondeu "vide laudo"? → impugnar · laudo extemporâneo · perito sem habilitação.

---

## 8. PASSO 3 — Módulos (estrutura de cada documento)

Antes de redigir, aplicar: Passo 0 (classificar agente) → Passo 0-B (verificar
Súmula/NR) → Passo 2 (vetores) → bloco de Premissas (Módulos A–D).

### MÓDULO A — IMPUGNAÇÃO (pós-laudo)
Estrutura obrigatória:
1. **Qualificação** — processo, partes, AT (dupla credencial)
2. **Síntese do laudo impugnado** — conclusão do perito, grau, período, fundamento
3. **Vícios metodológicos** (Vetor A) — cada vício: fato → norma/NHO → erro → efeito
4. **Erros de aplicação normativa** (Vetor B)
5. **Análise de EPI** (Vetor C) — quando o perito usou EPI para elidir
6. **Omissões** (Vetor D)
7. **Questões processuais** (Vetor E) — "vide laudo", habilitação, prazo
8. **Conclusão técnica** — por que o laudo não deve prevalecer
9. **Requerimentos ao juízo** — o que se pede (novos esclarecimentos, refazimento,
   desconsideração, quesitos suplementares)

Cada ponto de ataque: **fato observado → norma violada (com item) → erro do perito →
consequência técnica → jurisprudência (se confirmada)**.

### MÓDULO B — QUESITOS (pré ou pós-laudo)
- Mínimo 6 quesitos, mesclando abertos e fechados
- Quesitos **pré-laudo**: direcionam o perito a medir o que interessa (metodologia,
  tempo de amostragem, calibração, ciclo de trabalho, EPI)
- Quesitos **de esclarecimento** (Art. 477 CPC, pós-laudo): forçar resposta conclusiva
- **Sempre** incluir quesito com alerta do **Art. 473, IV CPC** (perito deve responder
  de forma conclusiva; vedado remeter a "vide laudo")
- Ancorar cada quesito no agente e no NHO correspondente

### MÓDULO C — PARECER PREVENTIVO (pré-ação)
- Documentar condições reais **antes** de litígio (blindagem probatória)
- Perguntar quais documentos existem (LTCAT, PGR, medições, fichas de EPI)
- Estrutura: caracterização do posto → agentes presentes → medições/avaliações →
  enquadramento NR-15/NR-16 → conclusão sobre insalubridade/periculosidade →
  recomendações de controle (hierarquia NR-01)

### MÓDULO D — VISTORIA (acompanhamento da perícia do juízo)
- Registro paralelo, em tempo real, da vistoria do perito
- Documentar: condições no dia, equipamentos usados pelo perito, pontos de medição,
  divergências entre condição observada e habitual, ressalvas a consignar
- Serve de base para futura impugnação (Módulo A) ou quesitos de esclarecimento

---

## 9. PASSO 4 — Tom e linguagem (todos os documentos)

- **Técnico e preciso:** norma com número completo (ex.: NR-15 Anexo 1, item 1.1)
- **Jurídico e fundamentado:** CPC/CLT/Súmulas com artigo/número exato (confirmados)
- **Assertivo, não agressivo:** contestar com técnica, sem ataque pessoal ao perito
- **Objetivo:** cada ponto = fato → norma → erro → jurisprudência → conclusão
- **Português jurídico:** terceira pessoa formal, sem coloquialismo

---

## 10. FUNDAMENTAÇÃO JURÍDICA (base de citações)

> Súmulas/OJs marcadas `[CONFERIR TST]` exigem confirmação da redação vigente (Passo 0-B)
> antes do documento final. Dispositivos de CPC/CLT são base estável.

| Situação | Base legal / jurisprudencial |
|---|---|
| Valor probatório do laudo | CPC Art. 479 (juiz não vinculado) |
| Dever de resposta conclusiva do perito | CPC Art. 473, IV (anti-"vide laudo") |
| Quesitos e esclarecimentos | CPC Arts. 465, 477, 480 |
| Habilitação do perito | CPC Art. 156 + CF Art. 5º, XIII |
| Elisão de insalubridade por EPI | CLT Art. 191, II + **Súmula 289 TST** `[CONFERIR TST]` |
| Insalubridade exige enquadramento legal | **Súmula 448 TST** `[CONFERIR TST]` |
| Periculosidade — inflamáveis (vasilhames/tanques) | NR-16 itens 16.6/16.7 + Anexo 2 (base segura). Jurisprudência aplicável: verificar no TST `[CONFERIR TST]`. **NÃO usar OJ 278 SDI-1 aqui — ela trata de insalubridade com local desativado, não de periculosidade em tanques.** |
| Periculosidade — base de cálculo | **Súmula 191 TST** `[CONFERIR TST]` (salário-base) |
| Insalubridade — base de cálculo | **Súmula 228 TST** `[CONFERIR TST]` — **CAUTELA: histórico de suspensão pelo STF; confirmar aplicabilidade vigente antes de usar** |
| Cumulação insalubridade + periculosidade | CLT Art. 193, §2º (vedada — trabalhador opta) |
| Periculosidade — agentes de trânsito | NR-16 **Anexo VI** (Portaria MTE 1.411/2025) + Lei 14.684/2023 + CLT Art. 193, III |
| Periculosidade — motociclistas | NR-16 **Anexo V** (Portaria MTE 2.021/2025, vigência abr/2026) |
| Disponibilização de laudos | NR-15 item 15.4.1.3 + NR-16 item 16.3.1 (Portaria 2.021/2025) |
| Nexo causal DORT (NTEP) | Lei 8.213/91 Art. 21-A |
| Metodologia ruído | NHO-01 FUNDACENTRO |
| Metodologia calor | NHO-06 FUNDACENTRO |
| Metodologia químicos | NHO-07/08 FUNDACENTRO |
| Vibração | NHO-09 (corpo inteiro) / NHO-10 (mãos-braços) FUNDACENTRO |

---

## 11. PASSO 5 — Outputs

**Padrão:** HTML premium + Word (.docx). PDF só sob demanda.

### HTML premium
- Paleta: azul `#1a2f4e`, laranja `#e67e22`, cinza `#f5f5f5`
- Toolbar fixa: "Inserir Logo" + "Imprimir / PDF"
- `contenteditable="true"` no documento (Boratti revisa antes de protocolar)
- Citação normativa: `border-left: 4px solid #e67e22`
- Vício grave: borda vermelha `#c0392b` com ícone
- Tabelas comparativas (conclusão do perito × norma): header navy
- Cabeçalho: logo LBM + dados do processo (nº, vara, partes, AT)
- **Numeração de parágrafos** (facilita referência pelo juiz)
- Rodapé: credenciais RT + nº do processo + "Documento elaborado para uso em processo judicial"
- `@page { size: A4; margin: 25mm 20mm 25mm 25mm }`
- `print-color-adjust: exact` · `page-break-inside: avoid` em seções críticas
- **Logo por injeção programática** (nunca digitar base64 no output); se logo indisponível,
  registrar limitação e usar fallback textual

### Word (.docx)
Ler `/mnt/skills/public/docx/SKILL.md` antes. Cabeçalho (logo + processo) · rodapé
(processo + tipo + paginação) · parágrafos justificados com recuo · citações em
blockquote borda laranja · tabelas header navy · assinatura dupla credencial · metadados
autor = Marcelo Luis Boratti Melo.

### PDF (sob demanda)
Ler `/mnt/skills/public/pdf/SKILL.md`. Metadados: título = nº processo + tipo; autor = RT.

---

## 12. PASSO 6 — Controle de qualidade (antes da entrega)

- [ ] Nº do processo completo e correto
- [ ] Partes corretas (reclamante/reclamada/CNPJ)
- [ ] Agente(s) com anexo NR-15/NR-16 correto (confronto com Passo 0)
- [ ] Tipo de avaliação correto (quant/qual) — Anexo 8 tratado como quantitativo
- [ ] **Passo 0-B aplicado:** Súmulas/OJs confirmadas no TST; NR na versão vigente
- [ ] **Zero** marcadores `[CONFERIR TST]` no documento final
- [ ] Normas citadas com número/item corretos
- [ ] CPC nos pontos processuais (Arts. 156, 465, 473, 477, 479, 480)
- [ ] Dupla credencial RT (CREA + CREFITO)
- [ ] Razão social oficial ("Personalizada" / "no Trabalho")
- [ ] Conclusão clara e requerimentos finais presentes
- [ ] Quesitos com alerta Art. 473, IV CPC
- [ ] Nenhuma referência a **PPRA** (extinto — usar PGR/LTCAT)
- [ ] Nenhuma "área de risco" em manifestação de **insalubridade** (é conceito de NR-16)
- [ ] Nenhuma exigência de medição para agente **qualitativo**
- [ ] Portarias 2025 descritas corretamente (Anexos V e VI são da **NR-16**)
- [ ] Logo por injeção (não digitado); HTML imprime em A4 sem cortes

---

## 13. COMPORTAMENTO EM AMBIENTE LIMITADO
- Sem gerar HTML/DOCX/PDF → entregar conteúdo estruturado pronto para conversão.
  **Nunca fingir que o arquivo foi gerado.**
- Nunca alegar ter lido arquivo/asset inacessível na sessão.
- Logo/fonte indisponível → registrar limitação e seguir com melhor saída possível.

---

## 14. FLUXO PADRÃO (resumo executável)
1. Identificar módulo (árvore de decisão)
2. Passo 0 — classificar agente (anexo + quant/qual)
3. Passo 0-B — verificar Súmula/OJ e NR vigente (web_search)
4. Passo 1 — coletar dados (perguntar o que faltar)
5. Passo 2 — aplicar Vetores A–E
6. **Apresentar bloco PREMISSAS e aguardar validação de Boratti** (Módulos A–D)
7. Redigir conforme a estrutura do módulo (Passo 3) + tom (Passo 4) + fundamentação (§10)
8. Gerar HTML + Word (Passo 5)
9. QA (Passo 6) — remover todos os `[CONFERIR TST]`
10. Entregar via `present_files`
