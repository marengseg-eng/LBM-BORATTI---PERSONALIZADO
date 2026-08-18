---
name: proposta-comercial-sst
description: >
  Cria Propostas Técnicas comerciais para a LBM BORATTI Consultoria Personalizada em
  Segurança e Saúde no Trabalho. Acionar quando o usuário pedir proposta, orçamento,
  cotação, precificação ou apresentação comercial de serviços de SST — incluindo
  Ergonomia/AET, NR-01 psicossocial, CIPA/Treinamentos, Perícia Trabalhista, Gestão
  SST (PGR/PCMSO/LTCAT/PPP) e combos. Skill AUTOSSUFICIENTE: escopos, tiers, regras
  duras, Blindagem Jurídica e protocolo de preços estão neste arquivo. REGRA CRÍTICA:
  nunca inventar valores — preços só fornecidos por Boratti na sessão.
---

# PROPOSTA COMERCIAL SST — LBM BORATTI

**Versão:** 2.0.0 (autossuficiente) · Histórico em `CHANGELOG.md`.

> Skill autocontida: não invocar `references/` ou `assets/` externos — todo o conteúdo
> operacional está aqui.

## 1. Identificação Profissional (em toda proposta)

```
Marcelo Luis Boratti Melo
Engenheiro de Segurança do Trabalho — CREA-SP: 5069572947
Fisioterapeuta e Ergonomista — CREFITO 3/209468-F
LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
Sertãozinho/SP • marengseg@gmail.com • (16) 99338-8989
```

Razão social — forma única: "Consultoria **Personalizada** em Segurança e Saúde
**no** Trabalho". Nunca "do Trabalho", nunca "Consultoria em SST".

## 2. ⚠ PROTOCOLO DE PREÇOS — REGRA CRÍTICA Nº 1

**O modelo NUNCA inventa, estima ou "sugere" valores de serviço.** Sem exceção.

Fluxo obrigatório:
1. Verificar se Boratti informou valores nesta sessão (mensagens ou arquivo).
2. Se não: **perguntar objetivamente** os valores dos tiers aplicáveis (uma pergunta,
   os 4 campos) antes de montar a folha de preços.
3. Se Boratti mandar gerar sem valores: usar placeholders destacados
   `{{VALOR_ESSENCIAL}} {{VALOR_PROFISSIONAL}} {{VALOR_PREMIUM}} {{VALOR_TOTAL}}`
   (realce amarelo no HTML/Word) + aviso "valores pendentes de definição" no eco final.
4. As únicas cifras que o modelo pode escrever sozinho são as **condições fixas** da
   Seção 7 (7% à vista, 10% fidelidade, 50/50, 2× sem juros, 15% combo) — porque são
   política comercial, não preço de serviço.

Prazos de execução seguem a mesma regra: informados por Boratti ou `{{PRAZO_TIER}}`.

## 3. PASSO 1 — Coleta de dados

> **Antes de perguntar:** extrair da conversa — o usuário frequentemente já forneceu
> os dados do cliente. Perguntar apenas o que realmente falta.

**Cliente (obrigatórios):** razão social · CNPJ · cidade/UF · contato (nome, cargo,
e-mail/telefone) · nº de funcionários · setor/atividade (CNAE se souber) · grau de risco.
**Serviço:** tipo (Seção 4) · urgência/contexto (fiscalização, autuação, ação
trabalhista, preventivo, **pós-prazo NR-01**) · histórico SST (tem PGR? PCMSO? AET?) ·
tier desejado (ou apresentar os 4).
**Complementares:** nº de postos/funções (AET) · nº de setores (psicossocial) ·
processos em andamento (perícia) · prazos críticos.

Dados do cliente insuficientes → perguntar. Nunca gerar proposta com dado de cliente
inventado.

## 4. PASSO 2 — Tipos de proposta e escopos

> ⚠ Os escopos abaixo foram consolidados na v2.0 como base de trabalho. Ajustes de
> posicionamento comercial são prerrogativa de Boratti — acatar qualquer alteração
> dele sobre este texto.

### PROP-ERG — Ergonomia / AET
Escopo-núcleo: Análise Ergonômica do Trabalho por posto/função conforme NR-17 e NR-01,
pelo **Método LBMBORATTI-ERGO** — análise fotográfica estruturada, aplicação das
ferramentas reconhecidas (REBA, RULA, NIOSH, OCRA, Moore & Garg, entre as 19 do kit),
checklist NR-17 item a item, matriz de risco, Plano de Ação Ergonômico (PAE) com
hierarquia de controles, relatório premium editável + Word + PDF. Dimensionar por nº
de postos/funções.
Gradação de tiers: Essencial (postos críticos indicados) → Profissional (setor
completo) → Premium (empresa + PAE detalhado + apresentação de resultados) → Total
(tudo + reavaliação programada + suporte na implantação).

### PROP-PSICO — NR-01 Fatores de Riscos Psicossociais
Escopo-núcleo: ciclo completo — questionário validado (COPSOQ-III / JCQ / ITRA
conforme perfil), aplicação com anonimato garantido, relatório com dashboard,
integração dos fatores ao inventário de riscos do PGR, plano de ação e laudo técnico
quando aplicável.
Gradação: Essencial (diagnóstico + relatório) → Profissional (+ plano de ação PGR) →
Premium (+ treinamento de lideranças + canal de escuta) → Total (+ monitoramento
periódico e reavaliação anual).

### PROP-CIPA — CIPA e Treinamentos
Escopo-núcleo: processo eleitoral completo da CIPA+A (edital → apuração → posse),
atas, calendário anual, treinamento NR-05 com carga horária conforme grau de risco,
adequação à Lei 14.457/2022 (prevenção ao assédio), SIPAT, treinamentos por NR
conforme demanda (NR-06, 10, 11, 12, 18, 23, 33, 35 etc.).
Gradação: Essencial (eleição + treinamento) → Profissional (+ gestão anual de atas) →
Premium (+ SIPAT) → Total (assessoria anual completa da comissão).

### PROP-PER — Perícia Trabalhista (Assistência Técnica)
Escopo-núcleo: atuação como assistente técnico com dupla habilitação (CREA +
CREFITO — agentes físicos/químicos/biológicos E ergonômicos/DORT): parecer preventivo,
quesitos, acompanhamento de vistoria, impugnação/manifestação sobre laudo.
Gradação: Essencial (1 módulo, ex.: quesitos) → Profissional (acompanhamento do
processo: quesitos + vistoria) → Premium (+ impugnação/manifestação) → Total
(assessoria completa no contencioso, múltiplos processos — precificar por caso).

### PROP-SST — Gestão SST (PGR/PCMSO/LTCAT/PPP)
Escopo-núcleo: PGR completo (inventário de riscos + plano de ação, NR-01 vigente
incluindo fatores psicossociais), LTCAT, PPP, ordens de serviço, integração com PCMSO
(elaborado por médico do trabalho parceiro/da empresa — deixar a autoria médica
explícita), treinamentos obrigatórios básicos.
Gradação: Essencial (PGR) → Profissional (PGR + LTCAT) → Premium (+ PPP + OS +
integração PCMSO) → Total (gestão anual completa com atualizações e atendimento a
fiscalização).

### PROP-COMBO — Combinações
Somar escopos dos serviços envolvidos; aplicar **desconto combo de 15%** sobre o
valor somado (informado por Boratti). Combo mais vendável hoje: **PGR/Gestão SST +
NR-01 Psicossocial + Ergonomia** (ver argumento pós-prazo, Seção 6).

## 5. PASSO 3 — Estrutura e regras duras

**Ordem das 4 folhas (A4):**
1. Capa executiva · 2. Apresentação LBM + Diagnóstico do cliente ·
3. Escopo + Tiers + Preços · 4. Condições comerciais + Próximos passos + Assinatura.

**Regras duras (não negociáveis):**
- Título da capa: **"PROPOSTA TÉCNICA"** — nunca "e Comercial".
- Nº da proposta: `PROP-[TIPO]-[ANO]-[SEQ3]`. Validade: **30 dias**.
- **NUNCA** incluir seção "Fora do Escopo" / exclusões (padrão LBM).
- **Blindagem Jurídica Trabalhista**: seção obrigatória com destaque visual ⚖️ (Seção 6).
- 4 tiers sempre: **Essencial / Profissional / Premium / Total** — recomendado em realce.
- Nenhuma menção a PPRA (extinto) — sempre PGR.
- Diagnóstico do cliente personalizado: situação identificada, riscos legais da
  não-conformidade, NRs/CLT aplicáveis e impacto estimado (qualitativo; cifras de
  multa só com base verificada — ver Seção 6).

## 6. BLINDAGEM JURÍDICA TRABALHISTA + ARGUMENTO PÓS-PRAZO NR-01

### Blindagem Jurídica (texto-base — ajustável por Boratti)
> A documentação SST da LBM BORATTI é elaborada com **visão pericial**: o responsável
> técnico atua como assistente técnico em perícias trabalhistas e conhece, na prática,
> os pontos que peritos e advogados atacam em laudos e programas. Cada documento é
> construído para **resistir a contestação** — metodologia declarada, rastreabilidade
> de dados, referências normativas com item e versão, e coerência entre PGR, LTCAT,
> PPP e eSocial. Resultado: redução concreta do passivo trabalhista e previdenciário,
> e uma defesa documental pronta antes de qualquer reclamatória existir.

### Argumento NR-01 psicossocial — PÓS-PRAZO (obrigatório em toda proposta, qualquer serviço)
Situação vigente (confirmada em fontes oficiais em jul/2026):
- A nova redação do capítulo 1.5 da NR-01 (Portaria MTE 1.419/2024) entrou em vigor
  em **26/05/2026** (prazo fixado pela Portaria MTE 765/2025 e reafirmado pela CTPP
  em março/2026, sem nova prorrogação).
- **A fase educativa acabou.** Desde 26/05/2026 a fiscalização é punitiva: empresa sem
  fatores psicossociais no PGR está sujeita a autuação.
- Contexto de pressão: recorde de afastamentos por transtornos mentais (546 mil
  benefícios por incapacidade temporária em 2025) e crescimento de ações trabalhistas
  sobre o tema; MPT atuante independentemente da fiscalização do MTE.

**Como usar na proposta:** verificar se o cliente tem PGR com psicossociais. Se não
tem → enquadrar como **regularização urgente de empresa já exposta** (não mais
"preparação para o prazo"). Oferecer combo com PROP-PSICO. Valores de multa da NR-28:
citar apenas com o valor conferido na fonte oficial na sessão — sem conferir, usar
"multas administrativas conforme NR-28, por item descumprido" sem cifra.

**Proibido:** prometer imunidade a autuação/condenação. A blindagem reduz risco e
fortalece defesa; nunca garantir resultado.

## 7. Condições comerciais (texto literal)
```
- PIX (CNPJ LBM BORATTI): forma de pagamento padrão — desconto 7% à vista
- Transferência bancária: mesmas condições do PIX
- Parcelado em até 2× sem juros | acima de 2× com INPC/mês
- Sinal: 50% na assinatura + 50% na entrega
- Desconto à vista (integral): 7%
- Desconto renovação / cliente recorrente: 10%
- Início dos serviços: após assinatura + confirmação do sinal
- Validade da proposta: 30 dias
- Reajuste após vencimento: INPC acumulado
- Contrato: sim (modelo padrão LBM BORATTI)
```

## 8. Próximos passos (folha 4)
Como aceitar · documentos necessários para início · contato direto (WhatsApp
(16) 99338-8989 / e-mail) · CTA claro ("Responda este e-mail" ou "Assine digitalmente").

## 9. PASSO 4 — Outputs

**HTML premium:** paleta `#1a2f4e`/`#e67e22`/`#f5f5f5` · 4 folhas A4 com
`page-break-after` · toolbar "Inserir Logo" + "Imprimir/PDF" · `contenteditable` ·
cards de tier com badge no recomendado · seção Blindagem com destaque ⚖️ ·
`@page A4, print-color-adjust: exact` · placeholders `{{VALOR_*}}` com realce amarelo ·
logo por injeção de script (nunca digitar base64; ausente → fallback textual + nota) ·
montagem por seções via script.
**Word:** ler `/mnt/skills/public/docx/SKILL.md` antes; capa, tabela de tiers,
cabeçalho LBM, rodapé RT + nº da proposta.
**PDF:** ler `/mnt/skills/public/pdf/SKILL.md`; derivado do HTML; metadados = nº da
proposta / autor RT.

## 10. PASSO 5 — Controle de qualidade
- [ ] Dados do cliente corretos; nº `PROP-[TIPO]-[ANO]-[SEQ3]`; validade 30 dias
- [ ] **Nenhum valor inventado**: todo preço veio de Boratti ou está como `{{VALOR_*}}`
- [ ] 4 tiers presentes; recomendado destacado
- [ ] Blindagem Jurídica presente e destacada; sem promessa de imunidade
- [ ] Argumento NR-01 no enquadramento **pós-prazo** (vigente desde 26/05/2026)
- [ ] Cifra de multa só se conferida na sessão; senão, "conforme NR-28" sem valor
- [ ] Sem seção de exclusões; sem PPRA; título "PROPOSTA TÉCNICA"
- [ ] Credenciais RT + razão social oficial
- [ ] PCMSO com autoria médica explícita (quando no escopo)

## 11. Comportamento padrão
1. Dados completos + valores informados → eco de 5 linhas (cliente, serviço, tier
   recomendado, valores, pendências) → gerar nos formatos pedidos
2. Dados parciais → extrair do contexto; perguntar só o que falta
3. **Valores ausentes → perguntar (Seção 2); insistência em gerar → `{{VALOR_*}}`**
4. Pedido de revisão → confrontar com esta estrutura e apontar lacunas
5. Proposta rápida → versão compacta: Capa + Escopo + Tiers/Preços + Blindagem + Assinatura
6. Cliente recorrente → expansão de escopo + fidelidade 10% + continuidade
7. Qualquer proposta → checar adequação NR-01 psicossocial do cliente e oferecer
   combo com enquadramento pós-prazo (Seção 6)
