---
name: parecer-tecnico-nr01-nr17
description: >
  Emite o Parecer Técnico conclusivo de Fatores de Riscos Psicossociais + AEP/AET (NR-01 e NR-17) da LBM BORATTI
  Consultoria em SST, em 2 folhas A4 (Dashboard + Parecer e recomendações). Use SEMPRE que o usuário mencionar:
  parecer técnico, parecer NR-01, parecer NR-17, parecer psicossocial, parecer favorável, parecer desfavorável,
  parecer com ressalvas, conclusão técnica, síntese conclusiva, ciclo avaliativo concluído, encerrar o ciclo,
  fechamento do ciclo psicossocial, dashboard psicossocial, dashboard dos 12 fatores, gráfico de rosca dos fatores,
  ranking dos fatores psicossociais, índice global do método, AEP, avaliação ergonômica preliminar, AET concluída,
  registro de conclusão da AET, manutenção e acompanhamento dos controles, providências obrigação/recomendação,
  reavaliação bienal NR-01, PT-NR17. Também acionar quando o usuário enviar um laudo/relatório psicossocial (RPS)
  ou uma AEP e pedir "o parecer", "a conclusão", "as 2 folhas", "o documento de fechamento" ou "o dashboard".
  NÃO usar para: gerar o laudo psicossocial completo e os questionários (skill psicossocial-nr01), o one-pager
  em linguagem de cliente (skill resumo-psicossocial) ou a AET em si (skill aet-premium) — esta skill CONSOLIDA
  esses produtos em um parecer conclusivo. Output: HTML premium A4 2 folhas (navy #1a2f4e / laranja #e67e22),
  imprimível em PDF, e Word (.docx) quando solicitado.
---

# Skill: Parecer Técnico — Fatores de Riscos Psicossociais e AEP (NR-01 e NR-17)

Gera o **documento de fechamento do ciclo avaliativo**: consolida o laudo psicossocial (12 fatores), a AEP
(Avaliação Ergonômica Preliminar) e o status da AET (Análise Ergonômica do Trabalho) em um parecer técnico
conclusivo de **2 folhas A4**, assinado pelo responsável técnico.

**Posição na cadeia de documentos LBM:**

```
psicossocial-nr01  →  LAUDO completo + questionários + plano de ação
aet-premium        →  AET (aprofundamento ergonômico)
        ↓
parecer-tecnico-nr01-nr17  →  PARECER CONCLUSIVO (esta skill)  ← fecha o ciclo
        ↓
resumo-psicossocial →  one-pager comercial em linguagem de cliente
```

---

## REGRA DURA — NUNCA INVENTAR DADO

- **Nenhum escore, percentual, contagem, data, CNPJ ou nome é inferido.** Todo número vem do laudo/AEP
  fornecido pelo usuário ou é declarado por ele na sessão.
- Se um dado obrigatório faltar, ele entra na **lista de lacunas** do PASSO 1 e o documento **não é gerado**.
- Textos normativos, prazos legais e classificações **podem** ser preenchidos pela skill (estão nas
  `references/`), pois são norma pública — não são dados do cliente.
- O parecer **nunca** é mais favorável do que os dados permitem. Ver PASSO 3 (regra de veredicto).

---

## FLUXO OBRIGATÓRIO (3 passos, com trava)

```
PASSO 1 — ECO DOS DADOS + LACUNAS      →  aguardar o usuário completar/confirmar
PASSO 2 — BRIEFING CONSOLIDADO         →  aguardar autorização expressa
PASSO 3 — GERAR O HTML                 →  só após o usuário escrever "gera o HTML"
```

**Nunca pular direto para o HTML.** Mesmo que o usuário mande o laudo completo de primeira, apresentar o
PASSO 1 (eco + cálculos derivados) para conferência antes de produzir o documento.

---

## PASSO 1 — COLETA E ECO DOS DADOS

Extrair do laudo/AEP enviado, ou perguntar. Ecoar tudo em tabela, marcando `⚠️ FALTA` no que estiver ausente.

### Bloco A — Identificação
| Campo | Exemplo |
|---|---|
| Razão social | GR Montagens Industriais Guariba |
| CNPJ | 34.194.672/0001-05 |
| Data da avaliação | 15/06/2026 |
| Data de emissão | 08/08/2026 |
| Revisão | REV. 05 |
| Documento-base (laudo) | Laudo de Fatores Psicossociais e AEP, código RPS-MG-ZC8Z7 |

O **código do parecer** é gerado pela skill (não perguntar):
`PT-NR17-{INICIAIS_EMPRESA}-{DDMMAA_EMISSÃO}` → `PT-NR17-GR-080826`

### Bloco B — Amostra
- Trabalhadores avaliados / total do escopo → `67/67`

### Bloco C — Os 12 fatores (escore % de cada um)
Lista fixa e fechada. O usuário fornece o escore de cada um, na escala **0% a 100%**:

`Demanda` · `Controle` · `Apoio Social` · `Relacionamentos` · `Papel` · `Mudança` · `Jornada` ·
`Condições Ergonômicas` · `Assédio Moral` · `Assédio Verbal` · `Assédio Físico / Violência` · `Assédio Sexual`

> Se o laudo trouxer menos de 12 fatores, **não completar com estimativa** — perguntar. O cabeçalho do
> documento ("12 FATORES AVALIADOS") e o card "12/12" acompanham a quantidade real.

### Bloco D — AEP (Avaliação Ergonômica Preliminar)
- Total de itens avaliados → `61`
- Itens de baixa gravidade e ocorrência improvável → `61`
- Itens de gravidade média, alta, crítica, substancial ou intolerável → `0`

> Os três valores devem fechar: `baixa + médio_ou_pior = total`. Se não fecharem, apontar a inconsistência
> no PASSO 1 e não seguir.

### Bloco E — Status do ciclo
- **AEP**: concluída e registrada / em elaboração / não iniciada
- **AET**: elaborada e concluída / em elaboração / não exigida / não iniciada
- **GRO/PGR**: ação contínua (integração e acompanhamento)

### Bloco F — Providências (tabela da folha 2)
Cada linha: `Providência` · `Natureza (OBRIGAÇÃO | RECOMENDAÇÃO)` · `Responsável` · `Prazo / evidência`.

Se o usuário não trouxer a tabela, **propor** o conjunto padrão de `references/providencias-padrao.md`
(4 linhas) e pedir confirmação — a proposta é sugestão normativa, não dado do cliente.

### Bloco G — Registro de conclusão da AET
Parágrafo curto informado pelo responsável técnico. Se a AET não estiver concluída, este bloco vira
"Pendências para conclusão da AET" e o veredicto muda (PASSO 3).

---

## PASSO 2 — CÁLCULOS DERIVADOS (a skill calcula, não pergunta)

Rodar `scripts/calcular.py` ou aplicar as fórmulas abaixo. **Sempre mostrar os cálculos no briefing.**

| Grandeza | Fórmula | Exemplo GR Montagens |
|---|---|---|
| **Base visual** | `Σ` de todos os escores | `24+24+22+21+20+20+20+20+20+19+19+18 = 247` pontos |
| **Índice global do método** | `round(Σ ÷ nº de fatores)` | `247 ÷ 12 = 20,58 → 21%` |
| **Ranking** | ordem **decrescente** de escore | #01 Condições Ergonômicas 24% … #12 Mudança 18% |
| **Fatores conformes** | contagem de escores na faixa Conforme | `12/12` |
| **Fatia do donut** | `escore_i ÷ Σ × 360°` | Condições Ergonômicas = `24/247 × 360 = 34,9°` |
| **Data de reavaliação** | `data da avaliação + 1 ano − 1 dia` | `15/06/2026 → 14/06/2027` |

**Conferência obrigatória:** se o usuário informar um índice global que divergir do calculado, **não
sobrescrever nenhum dos dois** — apontar a divergência e perguntar qual prevalece.

### Faixas de classificação (idênticas às da skill `resumo-psicossocial` — manter coerência entre documentos)

| Escore | Classificação | Badge | Cor |
|---|---|---|---|
| 0–24% | **Conforme** | `CONFORME` | verde `#1e7a4a` sobre `#f0fbf4` |
| 25–44% | **Atenção** | `ATENÇÃO` | âmbar `#8a6100` sobre `#fff8e6` |
| 45–59% | **Moderado** | `MODERADO` | laranja `#a55200` sobre `#fff2e4` |
| 60–74% | **Elevado** | `ELEVADO` | vermelho `#a52626` sobre `#fdeeee` |
| 75–100% | **Crítico** | `CRÍTICO` | vinho `#7d1d1d` sobre `#fbe4e4` |

Detalhes de paleta, cores dos 12 fatores e geometria do donut: `references/classificacao.md`.

---

## PASSO 3 — REGRA DE VEREDICTO (define o parecer da folha 2)

Aplicar **na ordem**; o primeiro que bater define o resultado.

| # | Condição | Parecer | Cor do card |
|---|---|---|---|
| 1 | Algum fator **Elevado/Crítico** (≥60%), **ou** item AEP crítico/intolerável sem controle implantado, **ou** AET exigida e não iniciada | **DESFAVORÁVEL** | vermelho `#c0392b` |
| 2 | Algum fator **Atenção/Moderado** (25–59%), **ou** AET em elaboração, **ou** providência obrigatória vencida | **FAVORÁVEL COM RESSALVAS** | laranja `#e67e22` |
| 3 | Todos os fatores **Conformes** + AEP concluída + AET concluída (ou justificadamente não exigida) | **FAVORÁVEL** | verde `#12a37a` |

- O selo abaixo do veredicto acompanha o status da AET: `AET CONCLUÍDA` / `AET EM ELABORAÇÃO` /
  `AET PENDENTE` / `AET NÃO EXIGIDA`.
- A tarja "CICLO AVALIATIVO CONCLUÍDO" só aparece no caso **3**. Nos demais: "CICLO AVALIATIVO EM
  ANDAMENTO".
- Frase de fecho da seção 4 é montada a partir do veredicto — os três modelos estão em
  `references/base-normativa.md`.

---

## PASSO 4 — GERAR O HTML (só após "gera o HTML")

Usar `assets/template-parecer.html` como base. É um arquivo completo e funcional, com marcadores `{{TOKEN}}`.

### Folha 1 — Dashboard
1. Header duas-tonalidades + faixa laranja
2. Faixa de identificação (empresa · CNPJ · avaliação · emissão)
3. 4 KPI cards: trabalhadores · índice global · fatores conformes · status AET
4. Gráfico de rosca (12 fatias, SVG) + ranking completo com barras e badges
5. Caixa "Leitura técnica do dashboard"
6. 3 mini-cards da AEP
7. Rodapé de enquadramento: NR-17 · NR-01 · STATUS

### Folha 2 — Parecer e recomendações
1. Card do veredicto + card do ciclo avaliativo
2. 3 cards de etapa: 01 AEP · 02 AET · 03 GRO/PGR
3. Seção 3 — tabela "Manutenção e acompanhamento dos controles"
4. Caixa verde "Registro de conclusão da AET"
5. Seção 4 — Conclusão técnica (3 tarjas + parágrafo)
6. Fontes oficiais consultadas + bloco de assinatura do RT

### Regras de renderização (não negociáveis)
- Tipografia **Barlow** + **Barlow Condensed** (Google Fonts), com fallback `system-ui, Arial`.
- Cores: navy `#1a2f4e`, navy escuro `#0f2440`, laranja `#e67e22`.
- `@page { size: A4; margin: 0 }` · `.folha { width:210mm; min-height:297mm }` · quebra entre folhas.
- `-webkit-print-color-adjust: exact; print-color-adjust: exact;`
- Botão **Imprimir / Salvar PDF** fixo no topo direito, com `.no-print { display:none }` na impressão.
- Logo LBM embutido em base64 (`assets/logo_lbm_base64.txt`) — **nunca** referenciar arquivo externo.
- Rodapé de todas as folhas: `LBM BORATTI · Marcelo Luís Boratti de Melo | CREA-SP 5069572947 | CREFITO 3/209468-F` + `n / total`.
- O documento **cabe em exatamente 2 folhas**. Se o conteúdo estourar, reduzir a tabela de providências
  (agrupar linhas) — **nunca** cortar a seção 4 nem a assinatura.

### Bloco de assinatura (fixo)
```
MARCELO LUÍS BORATTI DE MELO
Engenheiro de Segurança do Trabalho — CREA-SP 5069572947
Fisioterapeuta e Ergonomista — CREFITO 3/209468-F
marengseg@gmail.com | (16) 99338-8989 | Sertãozinho/SP
```

### Fontes oficiais (rodapé da folha 2)
Listar com a data da consulta (= data de emissão). Textos e links em `references/base-normativa.md`.
Se a emissão for posterior a alguma atualização normativa, **verificar a redação vigente antes de citar**.

---

## ATALHO — SCRIPTS

```bash
python3 scripts/calcular.py dados.json          # confere os derivados no PASSO 1
python3 scripts/montar.py  dados.json out.html  # gera o documento pronto
python3 scripts/montar.py  --exemplo out.html   # caso GR Montagens, para referência
```

`montar.py` **bloqueia a emissão** quando a AEP não fecha ou o índice global informado diverge do
calculado, e **avisa** quando o texto do card do ciclo contradiz o status da AET. Formato do JSON:
`assets/exemplo-dados.json`. Campos derivados não entram no JSON.

Se a tabela tiver mais de 4 providências, o script aplica o modo compacto automaticamente para a
folha 2 não estourar. Testado com 4 e com 6 linhas — 2 folhas em ambos.

Usar os scripts é opcional: dá para preencher `assets/template-parecer.html` à mão. Nesse caso,
refazer as contas do PASSO 2 e conferir a paginação antes de entregar.

---

## SAÍDAS

| Formato | Quando | Como |
|---|---|---|
| **HTML A4 (padrão)** | sempre | `assets/template-parecer.html` preenchido; abrir e imprimir em PDF |
| **PDF** | se pedido | imprimir o HTML pelo Chrome (A4, margens zero, "gráficos de plano de fundo" ligado) |
| **Word (.docx)** | se pedido | skill `docx`, mantendo cabeçalho, tabela da seção 3 e assinatura |

---

## ERROS QUE JÁ CUSTARAM RETRABALHO

1. **Somar errado a base visual.** `Base visual` é a **soma** dos escores, não a média nem o total de itens.
2. **Ordenar o ranking pelo nome do fator.** É por escore, decrescente.
3. **Escrever "FAVORÁVEL" com AET em elaboração.** Cai na regra 2 → *com ressalvas*.
4. **Prometer reavaliação bienal como obrigação.** A NR-01 traz o bienal como regra geral; o anual é
   **recomendação** de boa prática. A natureza na tabela muda conforme isso.
5. **Deixar o gráfico sem a ressalva.** A linha "O gráfico não representa prevalência clínica ou legal"
   é obrigatória — o instrumento é de gestão de risco, não diagnóstico de saúde.
6. **Gerar HTML sem autorização.** O usuário precisa escrever "gera o HTML".
