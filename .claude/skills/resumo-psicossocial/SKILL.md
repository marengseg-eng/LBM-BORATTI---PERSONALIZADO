---
name: resumo-psicossocial
description: >
  Gera uma folha-resumo HTML (one-pager A4) da Avaliação de Fatores de Risco Psicossociais para LBM BORATTI Consultoria em SST. Use esta skill SEMPRE que o usuário mencionar: resumo do laudo psicossocial, one-pager psicossocial, folha-resumo psicossocial, síntese do relatório psicossocial, sumário executivo psicossocial, página única laudo, resumo para cliente psicossocial, versão simplificada avaliação psicossocial, ou pedir para transformar/condensar um laudo/relatório de fatores psicossociais em uma única página legível. Também acionar quando o usuário fornecer um PDF/dados de avaliação psicossocial e pedir "uma folha", "resumo executivo", "versão para apresentar ao cliente" ou "fácil de entender". Output: HTML premium LBM BORATTI (navy #1a2f4e / laranja #e67e22), imprimível em A4 via botão, com grandes indicadores, ranking de fatores, ações principais e próximos passos — tudo em linguagem acessível ao cliente.
---

# Skill: Resumo Psicossocial — One-Pager LBM BORATTI

Gera uma **folha-resumo HTML A4** da Avaliação de Fatores de Risco Psicossociais, transformando um laudo técnico completo em um documento de fácil leitura para gestores e diretores de empresa.

---

## CONTEXTO DE USO

Este one-pager é o **documento de entrega ao cliente** — complementa o laudo técnico completo. Ele responde em 30 segundos à pergunta: *"Minha empresa está bem ou não?"*

Público-alvo do documento gerado: diretores, gerentes de RH, gestores — não necessariamente técnicos em SST.

---

## PASSO 0 — EXTRAIR DADOS DO LAUDO

Antes de gerar o HTML, identificar obrigatoriamente:

### Dados da empresa
- Razão social / nome
- CNPJ (se disponível)
- Data da avaliação
- Nº de trabalhadores avaliados / total
- Setor(es) avaliado(s)
- Nº do documento (ex: RPS-84-H4SUP)

### Resultado global
- Índice Global (%)
- Classificação: Conforme / Atenção / Moderado / Elevado / Crítico
- Nº de fatores críticos
- Nº de fatores moderados
- Nº de fatores conformes

### Ranking dos fatores (até 12)
Para cada fator: nome, score %, classificação

### Observações do avaliador
Pontos de atenção identificados pelo profissional (turno noturno, canal de denúncia, liderança, etc.)

### Plano de ação (5W2H)
Principais ações: título, descrição resumida, prazo

### Próximos passos / recomendações finais

---

## PASSO 1 — DETERMINAR COR DO VEREDICTO

| Índice Global | Classificação | Cor | Ícone |
|---|---|---|---|
| 0–24% | Conforme | Verde `#27ae60` | ✅ |
| 25–44% | Atenção | Verde-amarelo `#f0b429` | ⚠️ |
| 45–59% | Moderado | Laranja `#e67e22` | 🔶 |
| 60–74% | Elevado | Vermelho-laranja `#e74c3c` | 🔴 |
| 75–100% | Crítico | Vermelho escuro `#c0392b` | 🚨 |

---

## PASSO 2 — GERAR HTML ONE-PAGER

### Estrutura obrigatória (uma folha A4)

```
┌─────────────────────────────────────────────────────┐
│  HEADER: Logo LBM + Título + Empresa + Data         │
│  STRIPE LARANJA                                      │
├─────────────────────────────────────────────────────┤
│  VEREDICTO: ícone grande + texto direto + score     │
├─────────────────────────────────────────────────────┤
│  INDICADORES-CHAVE (4 cards): trabalhadores,        │
│  fatores avaliados, críticos, ações propostas       │
├────────────────────────┬────────────────────────────┤
│  RANKING DOS FATORES   │  COMO FOI FEITO +          │
│  (lista com badges)    │  ALERTA DA GESTÃO          │
├─────────────────────────────────────────────────────┤
│  AÇÕES PROPOSTAS (grid 2 colunas, até 6 itens)     │
├─────────────────────────────────────────────────────┤
│  O QUE FAZER AGORA (navy bg, 6 bullets)            │
├─────────────────────────────────────────────────────┤
│  FOOTER: RT (CREA + CREFITO) + Nº Documento        │
└─────────────────────────────────────────────────────┘
```

### Regras de design
- Família tipográfica: Barlow + Barlow Condensed (Google Fonts)
- Cores: navy `#1a2f4e`, laranja `#e67e22`, fundo `#f4f6f9`
- Tamanhos: corpo 12–13px, títulos 18–22px, números destaque 30–34px
- Botão imprimir fixo no canto superior direito
- `@media print`: botão oculto, `@page { margin:0; size:A4; }`
- `-webkit-print-color-adjust: exact; print-color-adjust: exact;`

### Linguagem dos textos
- Sem jargão técnico excessivo — usar linguagem direta
- Veredicto em **uma frase clara**: "Ambiente psicossocial CONTROLADO" ou "Atenção necessária: riscos identificados"
- Ações em verbos de ação: "Implantar canal de denúncia", "Capacitar lideranças"
- Próximos passos: frases curtas, no imperativo

---

## PASSO 3 — SEÇÕES CONDICIONAIS

### Se resultado = Conforme (0–24%)
- Box de veredicto: fundo `#e8f8f0`, borda verde
- Alerta da gestão: citar pontos de atenção identificados (mesmo sem risco crítico)
- Próximos passos: foco em monitoramento e inclusão no GRO/PGR

### Se resultado = Atenção ou Moderado (25–59%)
- Box de veredicto: fundo amarelo/laranja
- Destaque para fatores acima de 30%
- Ações em grid com badge "MÉDIA PRIORIDADE"

### Se resultado = Elevado ou Crítico (60–100%)
- Box de veredicto: fundo vermelho, texto branco
- Fatores críticos em seção destacada separada
- Badges vermelhos "AÇÃO IMEDIATA"
- Adicionar caixa de alerta legal: "Situação exige intervenção imediata conforme NR-01 item 1.5.7"

---

## PASSO 4 — RODAPÉ PADRÃO (OBRIGATÓRIO)

```
Marcelo Luis Boratti Melo
Eng. Seg. do Trabalho — CREA-SP 5069572947 | Fisioterapeuta / Ergonomista — CREFITO 3/209468-F
LBM BORATTI Consultoria · marengseg@gmail.com · (16) 99338-8989 · Sertãozinho/SP
```

Lado direito: Nº do documento + base normativa (NR-01 · ISO 45003:2021 · Lei 14.457/2022)

---

## DADOS FALTANTES

Se o usuário não fornecer o laudo completo (apenas mencionar o cliente), perguntar:

1. Índice global (%) e classificação final
2. Lista dos fatores com scores
3. Observações do avaliador
4. Principais ações do 5W2H
5. Nº do documento e data

Se fornecer o PDF ou os dados via contexto, extrair automaticamente sem perguntar.

---

## OUTPUT

- Arquivo: `resumo-psicossocial-[nome-empresa].html`
- Salvar em `/mnt/user-data/outputs/`
- Chamar `present_files` ao final
- Sempre incluir botão 🖨️ Imprimir / PDF

---

## REFERÊNCIAS NORMATIVAS OBRIGATÓRIAS

- NR-01 (Portaria MTE 1.419/2024) — item 1.5.7 (fatores psicossociais)
- ISO 45003:2021 — Gestão de riscos psicossociais
- Lei 14.457/2022 — CIPA+A (canal de denúncia de assédio)
- Portaria MTE 765/2025 — prazo 26/05/2026

---

## VARIAÇÕES DE ENTREGA

| Cenário | Ação |
|---|---|
| Usuário tem PDF do laudo | Extrair dados, gerar one-pager direto |
| Usuário tem dados parciais | Perguntar apenas o que falta |
| Usuário quer versão editável | Gerar com todos os campos `contenteditable` |
| Usuário quer para apresentação | Indicar skill `psicossocial-nr01` para relatório completo |
| Usuário quer versão Word | Indicar uso da skill `docx` após HTML aprovado |
