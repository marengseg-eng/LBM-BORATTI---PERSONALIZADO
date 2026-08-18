# Plano de Ação e Interpretação — Fatores Psicossociais

## Classificação de Risco por Score

| Score (0-100) | Classificação | Cor | Ação Requerida |
|---------------|--------------|-----|----------------|
| 0–33 | **BAIXO** | 🟢 Verde | Manter e monitorar |
| 34–50 | **MÉDIO-BAIXO** | 🟡 Amarelo | Atenção, medidas preventivas |
| 51–66 | **MÉDIO-ALTO** | 🟠 Laranja | Intervenção planejada |
| 67–100 | **ALTO / CRÍTICO** | 🔴 Vermelho | Intervenção imediata |

> Para ITRA: pontos de corte próprios (0–2,9 / 3–3,9 / 4–6) — ver instrumentos.md

---

## Medidas de Controle por Dimensão — COPSOQ-III

### Exigências Quantitativas Elevadas (volume excessivo)
**Medidas organizacionais:**
- Revisão de metas e dimensionamento de equipe
- Redistribuição de tarefas entre colaboradores
- Política de priorização de demandas
- Eliminação de tarefas desnecessárias (lean administrativo)

**Medidas administrativas:**
- Reuniões de alinhamento semanal com gestores
- Canal formal de comunicação de sobrecarga
- Registro e análise de horas extras

---

### Ritmo de Trabalho Acelerado
**Medidas organizacionais:**
- Revisão de metas de produção (realismo vs. pressão excessiva)
- Introdução de pausas estruturadas (NR-17 para trabalhos repetitivos)
- Análise e balanceamento de linha de produção

---

### Baixa Influência / Autonomia no Trabalho
**Medidas organizacionais:**
- Ampliação da autonomia nas decisões do posto de trabalho
- Gestão participativa / círculos de qualidade
- Enriquecimento de cargo (job enrichment)
- Delegação gradual com acompanhamento

---

### Baixo Reconhecimento e Respeito
**Medidas administrativas:**
- Política formal de reconhecimento (programa de boas práticas)
- Feedback positivo estruturado nas avaliações de desempenho
- Treinamento de lideranças em comunicação apreciativa

---

### Baixa Qualidade de Liderança
**Medidas administrativas:**
- Programa de desenvolvimento de lideranças
- Avaliação 360° de gestores
- Coaching para gestores com scores críticos
- Canal de escuta anônimo para relatos sobre liderança

---

### Baixo Apoio Social (colegas e supervisores)
**Medidas relacionais:**
- Programa de integração e trabalho em equipe
- Atividades de team building
- Grupos de apoio entre pares (peer support)
- Treinamento em comunicação não-violenta

---

### Conflito Trabalho-Família
**Medidas organizacionais:**
- Política de flexibilidade de horário (quando possível)
- Proibição de contato fora do horário de trabalho (direito à desconexão)
- Aviso prévio mínimo para horas extras
- Benefício de apoio à família (auxílio creche, etc.)

---

### Insegurança no Trabalho
**Medidas administrativas:**
- Comunicação transparente sobre situação da empresa
- Plano de desenvolvimento individual (PDI) para cada colaborador
- Programa de requalificação profissional
- Política clara de critérios para promoções e desligamentos

---

### Burnout / Esgotamento Profissional
**Medidas de intervenção (todos os níveis):**
- Afastamento temporário quando indicado (com suporte médico)
- Programa de Assistência ao Empregado (PAE/EAP)
- Redução temporária de demandas para colaboradores em risco
- Treinamento de gestores para identificação precoce de sinais
- Encaminhamento para saúde mental (parceria com PCMSO)

---

### Assédio Moral / Violência (quando identificado)
**AÇÃO IMEDIATA — independente de outros riscos:**
- Apuração formal dos casos relatados (comissão de ética / RH)
- Política de prevenção e combate ao assédio (Lei 14.457/2022)
- Canal de denúncia anônimo
- Treinamento obrigatório para toda a liderança
- Protocolo de acolhimento às vítimas
- Registro e acompanhamento dos casos

---

## Modelo de Card — Plano de Ação HTML

```html
<div class="acao-card risco-alto">
  <div class="acao-header">
    <span class="badge-risco">🔴 RISCO ALTO</span>
    <h3>[DIMENSÃO]</h3>
    <span class="score">Score: [XX]/100</span>
  </div>
  <div class="acao-body">
    <p class="setor"><strong>Setores afetados:</strong> [SETORES]</p>
    <p class="descricao">[DESCRIÇÃO DO PROBLEMA IDENTIFICADO]</p>
    <div class="medidas">
      <h4>Medidas de Controle</h4>
      <ul>
        <li class="org">🏢 [Medida organizacional]</li>
        <li class="adm">📋 [Medida administrativa]</li>
        <li class="ind">👤 [Medida individual]</li>
      </ul>
    </div>
    <div class="acao-footer">
      <span>👤 Responsável: [CARGO]</span>
      <span>📅 Prazo: [PRAZO]</span>
      <span>📊 Indicador: [MÉTRICA]</span>
    </div>
  </div>
</div>
```

---

## Indicadores de Monitoramento Sugeridos

| Dimensão | Indicador Objetivo |
|----------|-------------------|
| Exigências quantitativas | Horas extras mensais / taxa de absenteísmo |
| Burnout | Afastamentos por CID F (saúde mental) |
| Assédio / Conflitos | Nº de registros no canal de denúncia |
| Reconhecimento | Resultado da pesquisa de clima (anual) |
| Apoio social | Taxa de rotatividade por setor |
| Qualidade de liderança | Score de avaliação 360° dos gestores |
| Conflito trabalho-família | Nº de pedidos de demissão com motivo relatado |
| Geral | Reavaliação com instrumento em 12 meses |
