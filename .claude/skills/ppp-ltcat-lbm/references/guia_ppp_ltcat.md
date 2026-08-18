# Guia técnico — PPP e LTCAT (LBM BORATTI)

Referência de estrutura e mecânica de edição. Leia quando precisar entender os
campos, preencher um documento novo ou revisar um existente.

## 1. O que é cada documento

**LTCAT** (Laudo Técnico das Condições Ambientais do Trabalho): laudo que
comprova a exposição a agentes nocivos para fins previdenciários. Base do
enquadramento de aposentadoria especial. Assinado por Engenheiro de Segurança
do Trabalho ou Médico do Trabalho.

**PPP** (Perfil Profissiográfico Previdenciário): formulário (Anexo XV das
instruções normativas do INSS) que consolida dados administrativos, a
profissiografia e os registros ambientais — alimentado, entre outros, pelo
LTCAT. É o documento entregue ao INSS.

Regra prática: o LTCAT descreve/avalia; o PPP transcreve para o formulário
oficial. Os dois precisam ser coerentes entre si (mesma função, período, agentes
e intensidades).

## 2. Estrutura do PPP (formulário Anexo XV) — 1 tabela

Seções e campos principais (numeração do próprio formulário):

- **I — Dados administrativos**: 1 CAEPF/CEI, 2 Nome empresarial, 3 CNAE,
  4 Nome do trabalhador, 6 CPF, 7 Nascimento, 9 CTPS, 10 Admissão, 11 Regime.
- **12 — CAT registrada** (se houver).
- **13 — Lotação e atribuição**: 13.1 Período, 13.3 Setor, 13.4 Cargo,
  13.5 Função, 13.6 CBO, 13.7 Cód. GFIP.
- **14 — Profissiografia**: 14.1 Período, 14.2 Descrição das atividades.
- **II — Registros ambientais → 15 Exposição a fatores de risco** (a tabela-chave):
  15.1 Período, 15.2 Tipo, 15.3 Fator de risco, 15.4 Intens./Conc.,
  15.5 Técnica utilizada, 15.6 EPC eficaz (S/N), 15.7 EPI eficaz (S/N),
  15.8 CA do EPI. **É aqui que se acrescenta cada agente** (uma linha por agente).
  15.9 — bloco de perguntas sobre atendimento às NR-06 e NR-09 pelos EPI (S/N).
- **16 — Responsável pelos registros ambientais** (profissional habilitado, NIT,
  registro no conselho).
- **III — Monitoração biológica → 17 Exames** (Quadros I e II da NR-07),
  18 Responsável pela monitoração.
- **IV — Responsáveis pelas informações**, 19 Data de emissão, 20 Representante legal.

Atenção à mecânica: a tabela do PPP usa **muitas células mescladas**. Para
inserir um agente novo, **clone uma linha existente** (a do agente já presente,
ex.: Ruído) em vez de criar linha do zero — assim as mesclagens e a largura das
colunas são preservadas. Use `lib_docx.clonar_linha_risco`.

## 3. Estrutura do LTCAT (modelo LBM)

Sequência típica de itens (ajuste conforme o caso, mas mantenha a ordem):

1. Finalidade — 2. Empregador, função e período — 3. Dados do segurado —
4. Descrição das instalações — 5. Descrição das atividades —
6. Exposição a agentes potencialmente nocivos (subdividido por tipo de risco:
"Riscos Físicos", "Riscos Químicos", "Riscos Biológicos", etc., **mais** uma
tabela-resumo com colunas equivalentes às do campo 15 do PPP) —
7. EPC/EPI — 8. (agente quantitativo, ex.: Ruído) — 9. Métodos de amostragem —
10. Conclusão — 10.1 Enquadramentos — 11. Considerações finais —
Assinatura — Anexo fotográfico.

Ao inserir um agente no LTCAT há **dois lugares** a atualizar, para manter
coerência: (a) o subtópico textual dentro do item 6 (ex.: "Riscos Biológicos"
+ "6.1.x ..."), e (b) a linha correspondente na **tabela-resumo** do item 6.
E, quando o agente altera o enquadramento, complementar o item **10.1**.

## 4. Fluxo obrigatório (regra LBM — nunca pular)

Ao pedir um PPP ou LTCAT, **não gere o arquivo final de imediato**. Primeiro:

1. **Eco dos dados e das lacunas** — repita os dados recebidos (segurado,
   empresa, função/CBO, período, setor, agentes, intensidades, EPI/CA) e liste
   o que falta.
2. **Briefing** — objetivo do documento, estrutura sugerida, dados necessários,
   pontos de atenção técnica e normativa (grau de enquadramento, técnica de
   avaliação, coerência PPP↔LTCAT).
3. **Aguardar validação** do usuário.
4. Só então **gerar** o Word e, se pedido, o PDF A4.

## 5. Coerência que sempre deve ser conferida

- Função e CBO iguais no PPP e no LTCAT.
- Período de exposição idêntico.
- Cada agente do LTCAT aparece no campo 15 do PPP (e vice-versa).
- Técnica de avaliação correta por agente: **quantitativa** para ruído/calor
  (com NHO/NR-15) e **qualitativa** para agente biológico (NR-15, Anexo 14).
- EPC/EPI e CA preenchidos ou marcados como NA/NI de forma justificada.
- Habitualidade e permanência descritas de forma consistente.

## 6. Saídas

Padrão desta skill: **Word (.docx)** editável + **PDF A4** otimizado.
Gere o Word a partir dos modelos em `assets/templates/` e o PDF com
`scripts/gerar_pdf_a4.py`. Assinatura técnica e identidade visual: ver SKILL.md.
