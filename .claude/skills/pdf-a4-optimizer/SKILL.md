---
name: pdf-a4-optimizer
description: otimizar e normalizar arquivos pdf para saida profissional em folha iso a4, corrigindo tamanho de pagina, escala, orientacao, margens, centralizacao, excesso de branco, corte visual e problemas de sobreposicao gerados por montagem ou conversao. use quando o usuario pedir para deixar um pdf perfeito, pronto para impressao, em a4, ocupando a pagina inteira, sem sobreposicao, sem cortes, sem paginas tortas, com acabamento profissional, arquivo otimizado, reparado, redimensionado, padronizado, convertido para a4 ou validado visualmente.
---

# PDF A4 Optimizer

## Principio operacional

Tratar PDF como arte final: primeiro diagnosticar visualmente, depois normalizar para A4, renderizar de novo e verificar. Nunca declarar que o PDF ficou correto sem abrir/renderizar o resultado final.

A meta padrao e: folha ISO A4 real, conteudo maximizado sem corte, sem acumulacao de elementos sobrepostos por erro de montagem, orientacao coerente, arquivo salvo de forma otimizada e validado por renderizacao.

## Fluxo obrigatorio

1. Identificar a necessidade do usuario:
   - "ocupar a pagina inteira" + "sem cortar" -> usar `contain` com margem 0 mm, preservando proporcao.
   - "preencher toda a folha mesmo deformando" -> usar `stretch`, avisando que ha distorcao geometrica.
   - "preencher toda a folha sem faixas brancas" -> usar `cover` somente se corte for aceitavel.
   - PDF com fontes quebradas, camadas estranhas, anotacoes problemáticas, arte sobreposta ou visual diferente entre leitores -> usar `--flatten`.

2. Executar preflight visual:
   - Renderizar o PDF original quando possivel.
   - Verificar tamanhos de pagina, orientacao, paginas em branco, conteudo cortado, bordas, excesso de margem e sobreposicoes visiveis.
   - Se houver tabelas, assinaturas, carimbos ou elementos muito proximos da borda, preferir margem de seguranca entre 3 e 5 mm, salvo se o usuario exigir ocupacao maxima.

3. Normalizar para A4 usando o script incluido:

```bash
python scripts/optimize_pdf_a4.py input.pdf output_a4.pdf --mode contain --orientation auto --margin-mm 0 --check-dir check_renders --report report.json
```

4. Verificar o resultado:
   - Abrir/renderizar as paginas geradas em `check_renders`.
   - Confirmar que cada pagina tem dimensao A4: 595.276 x 841.890 pt em retrato, ou 841.890 x 595.276 pt em paisagem.
   - Confirmar que nao ha texto cortado, imagem cortada, sobreposicao criada na conversao, distorcao indesejada, pagina em branco indevida ou elementos fora da folha.
   - Se a saida ainda apresentar defeito visual, repetir com ajuste de margem, orientacao ou `--flatten`.

5. Entregar somente o PDF final e, quando util, um resumo curto do que foi corrigido. Nao entregar arquivos intermediarios, salvo se o usuario pedir relatorio de auditoria.

## Escolha tecnica

### Modo recomendado: contain

Usar `--mode contain` como padrao profissional. Ele preserva proporcao e impede corte. Se o PDF original nao tiver a mesma proporcao do A4, podem aparecer faixas brancas pequenas. Isso e preferivel a cortar texto ou deformar documentos tecnicos.

### Modo de preenchimento total: stretch

Usar `--mode stretch` apenas quando o usuario exigir que o conteudo ocupe exatamente toda a area A4. Alertar que isso pode deformar logotipos, plantas, assinaturas, fotos, QR codes e escalas graficas.

### Modo com corte: cover

Evitar `--mode cover` em documentos tecnicos. Usar apenas para capas, imagens decorativas ou materiais em que corte lateral/superior seja aceitavel.

### Flatten/rasterizacao

Usar `--flatten` quando:
- houver fontes substituidas, caracteres quebrados ou quadrados pretos;
- o PDF tiver camadas, transparencia, anotacoes, carimbos ou assinaturas que renderizam de forma instavel;
- o arquivo preservado em vetor continuar com sobreposicao visual;
- a prioridade for fidelidade visual para impressao, e nao edicao posterior do texto.

Exemplo:

```bash
python scripts/optimize_pdf_a4.py input.pdf output_a4_flat.pdf --mode contain --orientation auto --margin-mm 3 --flatten --raster-dpi 220 --jpeg-quality 92 --check-dir check_renders --report report.json
```

## Padrao de qualidade

Consultar `references/quality_checklist.md` quando o usuario pedir acabamento premium, verificacao rigorosa ou quando o PDF for para cliente, impressao, assinatura, treinamento ou entrega formal.

Criterios minimos:
- todas as paginas em A4 real;
- conteudo centralizado e maximizado;
- sem corte de textos, tabelas, imagens, assinaturas, rodapes ou cabecalhos;
- sem sobreposicao criada pelo processo de conversao;
- orientacao correta por pagina;
- arquivo abre em leitor PDF comum;
- validacao por renderizacao final.

## Script incluido

`scripts/optimize_pdf_a4.py` cria um novo PDF A4 a partir de um PDF existente. Por padrao, preserva vetor/texto com PyMuPDF usando uma pagina A4 limpa para cada pagina original. Isso evita acumulacao de conteudo entre paginas e reduz o risco de sobreposicao criada por editores/conversores.

Parametros principais:
- `--mode contain|stretch|cover`
- `--orientation auto|portrait|landscape`
- `--margin-mm N`
- `--flatten`
- `--raster-dpi N`
- `--jpeg-quality N`
- `--check-dir DIR`
- `--report report.json`

## Resposta ao usuario

Ao finalizar uma otimizacao, responder em portugues claro e direto:

```text
PDF otimizado em A4. Ajustes aplicados: padronizacao ISO A4, centralizacao, escala proporcional, orientacao automatica e validacao visual por renderizacao. Pontos de atencao: [listar somente se houver].
```

Se nao for possivel garantir algum criterio, dizer explicitamente qual criterio ficou pendente e por que.
