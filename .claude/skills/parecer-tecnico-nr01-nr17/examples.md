# Exemplos de uso

## Exemplo 1 — Caso completo (parecer FAVORÁVEL)

**Usuário:** *"Preciso do parecer técnico da GR Montagens. Segue o laudo em PDF."*

**PASSO 1 — eco dos dados** (a skill responde assim, antes de qualquer documento):

> Li o laudo. Confere os dados antes de eu montar o parecer:
>
> | Campo | Valor |
> |---|---|
> | Empresa | GR Montagens Industriais Guariba |
> | CNPJ | 34.194.672/0001-05 |
> | Avaliação | 15/06/2026 |
> | Emissão | 08/08/2026 ⚠️ confirmar |
> | Trabalhadores | 67/67 |
> | AEP | 61 itens · 61 baixa gravidade · 0 acima disso |
> | AET | concluída |
>
> **Cálculos derivados:** Σ = 247 pontos · índice global = 247÷12 = **21%** · **12/12 conformes** ·
> reavaliação até **14/06/2027**.
>
> **Veredicto pela regra:** FAVORÁVEL (todos conformes + AEP e AET concluídas).
>
> **Lacunas:** ⚠️ data de emissão · ⚠️ revisão (uso REV. 05?) · a tabela de providências não veio no
> laudo — proponho as 4 padrão. Confirma?

**PASSO 2 — usuário completa** → skill apresenta o briefing consolidado.

**PASSO 3 — usuário escreve "gera o HTML"** → documento em 2 folhas.

---

## Exemplo 2 — Dado que não fecha

**Usuário:** *"AEP: 74 itens, 68 de baixa gravidade e 4 acima."*

**Skill:**
> Esses três números não fecham: 68 + 4 = 72, e você informou 74 itens no total. Faltam 2 itens
> classificados. Não gero o documento com a AEP inconsistente — me confirma a distribuição correta.

---

## Exemplo 3 — Usuário pede o HTML direto

**Usuário:** *"Manda logo o HTML, já tem tudo no PDF."*

**Skill:** apresenta o PASSO 1 assim mesmo, e explica em uma linha:
> Ecoo os dados primeiro porque o parecer é assinado — um escore trocado vira problema em
> fiscalização. É rápido: confere a tabela e eu gero na sequência.

---

## Exemplo 4 — Índice global divergente

**Usuário:** *"O índice global é 25%."*
**Cálculo:** Σ = 247 ÷ 12 = 21%.

**Skill:**
> Divergência: você informou 25%, mas a média dos 12 escores dá 21% (Σ = 247). Não sobrescrevo
> nenhum dos dois. O 25% vem de outro método de composição (ponderado, por exemplo) ou algum escore
> do laudo está diferente do que passei? O documento sai com o valor que você confirmar.

---

## Exemplo 5 — AET ainda em elaboração

Cai na **regra 2** → `FAVORÁVEL COM RESSALVAS`, selo `AET EM ELABORAÇÃO`, tarja
`CICLO AVALIATIVO EM ANDAMENTO`, e a caixa verde vira **"Pendências para conclusão da AET"**.
A tabela ganha a linha obrigatória de conclusão da AET (`references/providencias-padrao.md`).

O parágrafo do card "AEP + AET + FATORES PSICOSSOCIAIS" precisa ser reescrito — se ele continuar
dizendo que a AET foi concluída, `montar.py` acusa a incoerência e o documento não deve ser emitido
com esse texto.

---

## Usando os scripts

```bash
# só os cálculos, para conferir no PASSO 1
python3 scripts/calcular.py dados.json
python3 scripts/calcular.py --exemplo          # caso GR Montagens

# documento pronto
python3 scripts/montar.py dados.json parecer.html
python3 scripts/montar.py --exemplo parecer.html

# PDF (Chrome headless, A4, sem cabeçalho do navegador)
chrome --headless --print-to-pdf=parecer.pdf --no-pdf-header-footer file://$PWD/parecer.html
```

`montar.py` **se recusa a gerar** quando `calcular.py` acusa AEP inconsistente ou índice global
divergente. É proposital: esses dois erros invalidam o parecer.

O JSON de entrada segue `assets/exemplo-dados.json`. Campos derivados (índice global, ranking,
donut, veredicto, data de reavaliação) **não vão no JSON** — são calculados.

### Comportamento automático
- Mais de 4 providências → a tabela entra em modo compacto para caber na folha 2.
- `conclusao_texto` aceita `<span class="az|vd|lj">` para destacar termos em azul, verde e laranja.
- Sem conexão, a Barlow não carrega e a fonte de fallback é mais larga: o título do cabeçalho quebra
  em duas linhas. Com internet (o caso normal de quem vai imprimir) fica em uma linha só.
