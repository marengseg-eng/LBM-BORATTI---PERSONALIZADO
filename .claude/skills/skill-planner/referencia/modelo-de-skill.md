# Modelo de skill

Este arquivo tem três partes: como escrever uma boa SKILL.md, como montar o fluxograma de aprovação da Fase 5, e como empacotar e entregar a skill pronta na Fase 6.

## Índice

- Como escrever a SKILL.md
- Boas práticas
- O fluxograma de aprovação (Fase 5)
- Como empacotar e entregar (Fase 6)

## Como escrever a SKILL.md

Toda skill é uma pasta com um arquivo `SKILL.md` dentro. Esse arquivo começa com um cabeçalho e segue com as instruções.

```yaml
---
name: nome-com-hifens-minusculas
description: O que a skill faz e quando ela deve ser usada. Escreva em terceira pessoa. Inclua as frases reais que a pessoa vai usar para chamar a skill. Seja um pouco "insistente" sobre quando usar, para a skill disparar mesmo quando o usuário não a nomear. Até 1024 caracteres.
---
```

Depois do cabeçalho, escreva as instruções em português, no modo imperativo ("Faça", "Verifique", "Resuma"). Estruture conforme o processo que vocês desenharam juntos.

## Boas práticas

**Seja conciso.** O Claude já é inteligente. Não explique o que é um PDF ou como uma planilha funciona. Acrescente só o contexto que ele não tem: as regras do trabalho da pessoa, o formato exato que ela quer, os exemplos dela.

**Explique o porquê, não só o quê.** Em vez de "SEMPRE faça X", explique por que X importa. O Claude segue melhor quando entende a razão do que quando recebe uma regra rígida sem explicação.

**Mostre exemplos.** Um par de "isto entra, isto sai" vale mais que um parágrafo de descrição. Use os exemplos reais que a pessoa deu na entrevista.

**Use as palavras da pessoa.** A descrição e os gatilhos devem soar como ela fala. Aproveite as frases que ela disse na Fase de descoberta de gatilhos.

**Divida quando ficar grande.** Se a SKILL.md passar de umas 500 linhas, mova o detalhe para arquivos em uma pasta `referencia/` e aponte para eles a partir da SKILL.md. Mantenha as referências a um nível só de distância.

**Evite armadilhas comuns:** nada de informação que envelhece ("antes de agosto de 2025"), nada de termo trocado no meio do caminho (escolha um termo e use sempre o mesmo), nada de descrição vaga ("ajuda com documentos"), nada de caminho de arquivo no estilo Windows.

### Estrutura de arquivos de uma skill

```
nome-da-skill/
├── SKILL.md            (as instruções principais)
├── referencia/         (detalhes lidos só quando precisa)
│   └── exemplos.md
└── scripts/            (código que roda, quando houver)
    └── utilitario.py
```

Skills simples de iniciante quase sempre são só a SKILL.md, sem referência nem script. Não crie pastas que não vão ser usadas.

## O fluxograma de aprovação (Fase 5)

Antes de construir, renderize um fluxograma dentro da conversa usando o recurso visual interativo do claude.ai. O objetivo é a pessoa olhar e entender o desenho inteiro de uma vez, então priorize clareza sobre enfeite.

O fluxograma deve conter, em português e em linguagem simples:

- No topo, o nome da skill e uma frase do que ela faz.
- Um bloco "O que entra" com a informação que a pessoa fornece.
- Os passos do processo, na ordem, ligados por setas. Cada passo em uma ou duas linhas.
- Os pontos de decisão desenhados como bifurcação ("se for assim, vai por aqui; se não, por ali").
- Um bloco "O que sai" com o resultado final.
- Um bloco "Frases que acionam" com as frases reais que a pessoa vai digitar.

Diretrizes visuais: use rótulos curtos, fluxo de cima para baixo, e legenda do tipo de cada bloco (entrada, passo, decisão, saída). Faça pensando em quem nunca viu um fluxograma. Evite cores que dependam de tema claro ou escuro; prefira contraste alto e formas com rótulo.

Depois de mostrar, faça uma pergunta de aprovação clara e espere. Se a pessoa pedir ajuste, volte à entrevista, corrija, e mostre o fluxograma de novo. Só construa quando houver aprovação explícita.

## Como empacotar e entregar (Fase 6)

Depois da aprovação, escreva os arquivos da skill em uma pasta dentro de `/tmp`, por exemplo `/tmp/nome-da-skill/`. Use o nome real da skill no lugar de `nome-da-skill`.

Se a skill lida com documentos, salve o modelo de saída que a pessoa forneceu na Fase 1 como referência dentro da skill, por exemplo em `referencia/modelo-de-saida.md` (ou no formato em que ele veio). Na SKILL.md, instrua a skill a seguir esse modelo como padrão fixo da saída. É isso que faz a skill reproduzir sempre a mesma estrutura que a pessoa aprovou, em vez de inventar um formato novo a cada uso. Quando fizer sentido, registre também o modelo ou o tipo do arquivo de entrada, para a skill saber o que esperar.

Em seguida, empacote a skill com o script da skill-creator. Este comando gera o arquivo `.skill` na pasta de saída, o que faz aparecer o botão "Salvar habilidade" na conversa:

```bash
cd /mnt/skills/examples/skill-creator && python -m scripts.package_skill /tmp/nome-da-skill /mnt/user-data/outputs/
```

Depois de empacotar, apresente o arquivo `.skill` resultante para a pessoa com a ferramenta de apresentar arquivos. Entregue sempre o `.skill` empacotado, nunca um arquivo de texto solto, e nunca um `.md` para download. É o `.skill` que permite salvar e instalar a habilidade com um clique.

Por fim, em poucas linhas e sem jargão, explique para a pessoa o que foi criado e como ela usa: clicar em salvar, e depois é só pedir ao Claude usando uma das frases-gatilho. Ofereça ajustar qualquer coisa que ela queira.
