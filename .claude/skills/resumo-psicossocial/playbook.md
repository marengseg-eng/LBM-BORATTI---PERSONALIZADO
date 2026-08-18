# Playbook — resumo-psicossocial

## Árvore de decisão rápida

```
Usuário quer resumo psicossocial?
│
├── Tem PDF/dados completos?
│   ├── SIM → Extrair → Gerar → present_files
│   └── NÃO → Perguntar dados mínimos (ver lista abaixo)
│
├── Qual o índice global?
│   ├── 0–24% (Conforme) → Veredicto verde + foco em monitoramento
│   ├── 25–44% (Atenção) → Veredicto amarelo + destacar fatores > 25%
│   ├── 45–59% (Moderado) → Veredicto laranja + ações prioritárias
│   ├── 60–74% (Elevado) → Veredicto laranja-vermelho + urgência
│   └── 75–100% (Crítico) → Veredicto vermelho + alerta legal NR-01
│
└── Quer versão editável? → Adicionar contenteditable nos campos
```

## Dados mínimos para gerar o one-pager

**Obrigatórios:**
1. Nome da empresa
2. Índice global (%)
3. Classificação final

**Importantes (perguntar se não tiver):**
4. Lista dos fatores com scores
5. Nº do documento
6. Data da avaliação
7. Nº de trabalhadores
8. Observações do avaliador
9. Principais ações do plano 5W2H

**Opcionais (usar padrões se ausentes):**
- CNPJ → "—"
- Setor → "Todos"
- GHE → omitir campo

## Padrões por classificação

### Conforme (verde)
- Ícone: ✅
- Frase veredicto: "Ambiente psicossocial CONTROLADO"
- Subtítulo: "Todos os fatores avaliados estão dentro dos parâmetros aceitáveis. Recomenda-se manutenção das boas práticas e monitoramento anual."

### Atenção (amarelo)
- Ícone: ⚠️
- Frase: "Fatores em ATENÇÃO — intervenção preventiva recomendada"
- Subtítulo: "Alguns fatores apresentam exposição moderada. Ações preventivas foram estruturadas para controle."

### Moderado (laranja)
- Ícone: 🔶
- Frase: "Risco MODERADO — ações de controle necessárias"
- Subtítulo: "Fatores moderados identificados exigem implantação de controles conforme NR-01 item 1.5.7."

### Elevado (vermelho-laranja)
- Ícone: 🔴
- Frase: "Risco ELEVADO — intervenção prioritária"
- Subtítulo: "Fatores elevados identificados. Implantação imediata das medidas de controle conforme NR-01 e ISO 45003."

### Crítico (vermelho)
- Ícone: 🚨
- Frase: "Risco CRÍTICO — ação imediata obrigatória"
- Subtítulo: "Situação crítica identificada. A NR-01 item 1.5.7 exige implantação imediata de controles. Risco de passivo trabalhista e autuação fiscal."

## Checklist antes de entregar

- [ ] Veredicto com cor correta para o índice
- [ ] 4 indicadores-chave preenchidos
- [ ] Ranking dos fatores com badges (mín. 6, máx. 12)
- [ ] Alerta da gestão com pontos de atenção reais
- [ ] Ações do 5W2H (mín. 4, máx. 8)
- [ ] "O que fazer agora" com ≥ 4 bullets
- [ ] Rodapé com CREA + CREFITO + contato
- [ ] Botão imprimir funcional
- [ ] `@media print` configurado (margin:0, size:A4)
- [ ] `print-color-adjust: exact` ativo
