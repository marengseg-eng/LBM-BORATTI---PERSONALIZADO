# Enquadramento de agentes nocivos — PPP/LTCAT

Guia de apoio ao enquadramento. **Regra de ouro (LBM):** não inventar número de
item, artigo, anexo, prazo ou exigência. Cite a referência apenas quando tiver
segurança; na dúvida, sinalize a incerteza e recomende conferência na fonte
oficial vigente. Diferencie sempre **obrigação legal**, **boa prática técnica**
e **recomendação consultiva**.

## 1. Duas lógicas distintas — não confundir

- **Insalubridade (NR-15)** → define o **grau** (10% / 20% / 40%) para adicional
  trabalhista. Cada agente tem seu anexo.
- **Aposentadoria especial (previdenciário)** → define se a exposição **enquadra**
  o tempo como especial. Base: Regulamento da Previdência (Decreto 3.048/99,
  com as alterações do Decreto 10.410/2020) e a IN PRES/INSS vigente. O PPP/LTCAT
  servem a **esta** finalidade; o "grau" da NR-15 é referência de técnica/critério,
  não o que concede o benefício.

Os dois PDFs de referência bundlados tratam da segunda lógica:
- `references/*DECRETO_14410*` — resumo comparativo das alterações do
  **Decreto 10.410/2020** sobre o Decreto 3.048/99 (redação atual x anterior).
- `references/*INSTRU__O_NORMATIVA*128*` — **IN PRES/INSS nº 128** (regras de
  benefícios, incluindo aposentadoria especial, PPP e LTCAT). Consulte o texto
  bundlado para localizar o dispositivo exato antes de citar número de artigo.

## 2. Técnica de avaliação por tipo de agente

| Agente          | Avaliação      | Referência técnica usual                     |
|-----------------|----------------|----------------------------------------------|
| Ruído           | Quantitativa   | NR-15 Anexo I; NHO-01 (NEN em dB(A))         |
| Calor           | Quantitativa   | NR-15 Anexo 3; NHO-06 (IBUTG)                |
| Vibração        | Quantitativa   | NHO-09 (corpo inteiro) / NHO-10 (mãos-braços)|
| Agentes químicos| Quant./Qualit. | NR-15 Anexos 11/12/13; NHO conforme o agente |
| **Biológicos**  | **Qualitativa**| **NR-15, Anexo 14**                          |

Para agente biológico não há limite de tolerância nem medição — o enquadramento
é **qualitativo**, pela natureza da atividade e do contato.

## 3. Agentes biológicos — NR-15, Anexo 14 (verificado)

Avaliação **qualitativa**. O Anexo 14 separa por grau, e a diferença é decisiva:

**Grau máximo (40%)** — contato permanente com material infectante de maior
gravidade, p.ex. *carnes, glândulas, vísceras, sangue, ossos, couros, pelos e
dejeções de animais portadores de doenças infectocontagiosas* (carbunculose,
brucelose, tuberculose), além de esgotos e lixo urbano.

**Grau médio (20%)** — *"Trabalhos e operações em contato permanente com
pacientes, animais ou com material infectocontagiante, em: (...) estábulos e
cavalariças; (...)"*, entre outros estabelecimentos.

Aplicação a **atividade rural com bovinos** (vaqueiro, tratador, ordenhador):
contato permanente com os animais e o ambiente de curral/estábulo enquadra em
**grau médio (20%)** pela rubrica "estábulos e cavalariças" + contato permanente
com animais. **Não é grau máximo**, salvo prova de manejo habitual de animais
portadores das doenças infectocontagiosas citadas.

Pontos de atenção (sinalizar ao cliente quando pertinente):
- Há discussão jurisprudencial sobre equiparar "curral" a "estábulo/cavalariça";
  a maioria reconhece o direito do rural em contato permanente com o rebanho, mas
  o perito pode contestar — ancore a redação em "contato permanente com animais".
- Exigir que a exposição seja **habitual e permanente** (não ocasional nem
  intermitente) e descrever a fonte geradora concretamente.

## 4. Preenchimento sugerido de uma linha biológica (campo 15 / tabela do item 6)

- Tipo: **Biológico**
- Fator de risco: **Agentes biológicos (bactérias, vírus, fungos e parasitas) —
  contato permanente com [animais/secreções/dejetos/material orgânico] em
  [currais/estábulos/…]**
- Intens./Conc.: **Qualitativo**
- Técnica: **Qualitativa — NR-15, Anexo 14**
- EPC eficaz: **NA** (em regra) · EPI eficaz: **S/N conforme dados** ·
  CA do EPI: preencher o número quando houver, senão **NI** (não informado)

Não afirme EPI eficaz "S" sem o CA correspondente; a incoerência enfraquece o
documento e pode ser explorada em perícia.
