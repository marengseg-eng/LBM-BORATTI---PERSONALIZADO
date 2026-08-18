# Classificação, paleta e geometria do dashboard

## 1. Os 12 fatores — ordem canônica e cor fixa por posição no ranking

A cor é ligada à **posição no ranking** (#01 a #12), não ao nome do fator. Assim o donut e o ranking
sempre batem visualmente, independentemente da empresa avaliada.

| Pos. | Cor | Hex |
|---|---|---|
| #01 | azul-claro | `#2aa8e8` |
| #02 | azul-royal | `#3b5bdb` |
| #03 | roxo | `#7b3fe4` |
| #04 | magenta | `#ec2f72` |
| #05 | laranja-vermelho | `#f4511e` |
| #06 | âmbar | `#f5a623` |
| #07 | verde | `#12a37a` |
| #08 | ciano | `#0fc2d6` |
| #09 | verde-água | `#2dd4a7` |
| #10 | roxo-médio | `#8b5cf6` |
| #11 | rosa | `#f4306d` |
| #12 | azul | `#3b82f6` |

### Lista fechada dos fatores avaliados
1. Demanda
2. Controle
3. Apoio Social
4. Relacionamentos
5. Papel
6. Mudança
7. Jornada
8. Condições Ergonômicas
9. Assédio Moral
10. Assédio Verbal
11. Assédio Físico / Violência
12. Assédio Sexual

Os seis primeiros correspondem aos domínios clássicos de organização do trabalho (padrão HSE-MS /
COPSOQ). Jornada e Condições Ergonômicas fazem a ponte com a NR-17. Os quatro últimos cobrem a
exigência da Lei 14.457/2022 e da NR-01 quanto a assédio e violência no trabalho.

---

## 2. Faixas de classificação

| Escore | Classificação | Texto do badge | Cor do texto | Fundo | Borda |
|---|---|---|---|---|---|
| 0–24% | Conforme | `CONFORME` | `#1e7a4a` | `#f0fbf4` | `#7fce9f` |
| 25–44% | Atenção | `ATENÇÃO` | `#8a6100` | `#fff8e6` | `#e8c766` |
| 45–59% | Moderado | `MODERADO` | `#a55200` | `#fff2e4` | `#efab6d` |
| 60–74% | Elevado | `ELEVADO` | `#a52626` | `#fdeeee` | `#e79a9a` |
| 75–100% | Crítico | `CRÍTICO` | `#7d1d1d` | `#fbe4e4` | `#d97070` |

> As faixas são **as mesmas** da skill `resumo-psicossocial`. Se o instrumento efetivamente aplicado
> (COPSOQ-III, JCQ/Karasek, ITRA, PsicoRisk) tiver pontos de corte próprios, usar os do instrumento e
> **declarar isso na Leitura Técnica** — nunca misturar as duas réguas no mesmo documento.

---

## 3. Fórmulas

```
Σ            = soma de todos os escores          → "Base visual: {Σ} pontos de escore"
Índice global= round(Σ ÷ n_fatores)              → número grande no centro do donut
Fatia_i      = escore_i ÷ Σ × 360°               → ângulo da fatia do fator i
Barra_i      = escore_i % da largura da trilha   → escala 0–100%, não normalizada por Σ
Conformes    = nº de escores ≤ 24%               → card "{conformes}/{n_fatores}"
Reavaliação  = data_avaliação + 1 ano − 1 dia
```

Atenção à diferença: **o donut é proporcional a Σ** (distribuição relativa), enquanto **a barra do
ranking é absoluta na escala 0–100%**. São duas leituras distintas do mesmo escore e não devem ser
uniformizadas.

### Donut em SVG (stroke-dasharray)

Circunferência com `r = 54` → `C = 2π × 54 ≈ 339,29`.

Para cada fator, em ordem de ranking:
```
comprimento_i = escore_i ÷ Σ × C
stroke-dasharray  = "{comprimento_i} {C - comprimento_i}"
stroke-dashoffset = "-{soma dos comprimentos anteriores}"
```
Com `transform="rotate(-90 60 60)"` no grupo, para começar às 12 horas.
Separação visual entre fatias: `stroke-width: 26` e um `gap` de 1,2 unidade descontado do comprimento.

---

## 4. Exemplo conferido (GR Montagens Industriais Guariba)

| # | Fator | Escore | Classificação |
|---|---|---|---|
| 01 | Condições Ergonômicas | 24% | Conforme |
| 02 | Jornada | 24% | Conforme |
| 03 | Controle | 22% | Conforme |
| 04 | Assédio Moral | 21% | Conforme |
| 05 | Demanda | 20% | Conforme |
| 06 | Apoio Social | 20% | Conforme |
| 07 | Assédio Verbal | 20% | Conforme |
| 08 | Assédio Físico / Violência | 20% | Conforme |
| 09 | Papel | 20% | Conforme |
| 10 | Relacionamentos | 19% | Conforme |
| 11 | Assédio Sexual | 19% | Conforme |
| 12 | Mudança | 18% | Conforme |

`Σ = 247` · `Índice global = round(247/12) = round(20,58) = 21%` · `Conformes = 12/12`
`Reavaliação = 15/06/2026 + 1 ano − 1 dia = 14/06/2027`

### Critério de ordenação e desempate

Ordenar pelo escore **não arredondado** do instrumento; exibir o valor arredondado. Dois fatores podem
mostrar o mesmo percentual e ainda assim ocupar posições distintas — no exemplo acima, cinco fatores
exibem 20% e cada um tem sua posição definida pela casa decimal do cálculo original.

Só quando o laudo não trouxer a casa decimal: manter a ordem em que os fatores aparecem no laudo de
origem. **Não reordenar por nome nem pela lista canônica** — isso troca a leitura do ranking e não
corresponde ao cálculo. Se o laudo não permitir desempatar, perguntar ao responsável técnico.
