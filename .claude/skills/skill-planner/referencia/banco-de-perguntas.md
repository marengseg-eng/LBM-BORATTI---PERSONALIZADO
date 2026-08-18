# Banco de perguntas

Este é o repertório do mentor. Não leia tudo em voz alta nem dispare todas as perguntas. Escolha as que cabem no caso, uma de cada vez, sempre com um palpite pronto. Os exemplos por profissão servem para você tornar cada pergunta concreta, trocando o exemplo pelo da profissão da pessoa.

## Índice

- Fase 1: O panorama
- Fase 2: O passo a passo
- Fase 3: O que pode dar errado
- Fase 4: O espelho
- Exemplos de como aprofundar uma resposta vaga
- Frases-gatilho: como descobrir junto com a pessoa

## Fase 1: O panorama

Objetivo: entender o problema real, para quem é, o que entra e o que sai.

Perguntas, na ordem sugerida:

1. Qual tarefa do seu dia a dia você se pega fazendo do mesmo jeito, de novo e de novo, e gostaria que o Claude fizesse por você?
2. Quem vai usar isso: só você, sua equipe, ou seus clientes também?
3. Quando você vai usar essa skill, o que você tem em mãos no começo? De onde vem essa informação?
4. No fim, o que você quer receber? Um texto, uma tabela, um arquivo, um resumo?

Quando a skill lida com documentos ou arquivos, faça também estas três perguntas, que são obrigatórias. Não avance sem elas.

5. O que dá início a esse processo na vida real? Um contrato que chega por e-mail, uma planilha do cliente, uma foto que você tira? (este é o gatilho inicial do processo)
6. Você consegue me mandar agora um exemplo real do que entra? Pode ser o arquivo de verdade ou um trecho colado. E me diz o tipo: é PDF, Word, planilha, imagem? (este é o modelo de entrada)
7. E me mostra um exemplo do resultado perfeito, do jeitinho que você quer receber, com as seções e a ordem certas. Em que formato você quer a saída: um texto, um Word, uma planilha, um PDF? (este é o modelo de saída, que vira referência da skill)

Se a pessoa não tiver um modelo pronto da saída, ajude-a a montar um ali na conversa antes de seguir. Esse par, modelo de entrada e modelo de saída, é o que faz a skill produzir sempre o mesmo padrão.

Exemplos do que "o que entra" e "o que sai" parecem, por profissão:

- Advogado: entra um contrato em PDF; sai um resumo com prazos, multas, cláusulas de renovação e pontos de atenção.
- Professor: entra o tema e a série; sai um plano de aula com objetivos, atividades e avaliação.
- Médico: entra a descrição de um caso ou um exame; sai um texto padronizado para o prontuário.
- Serviço técnico: entra a foto ou a descrição de um equipamento com defeito; sai um orçamento estruturado com diagnóstico, peças e prazo.

## Fase 2: O passo a passo

Objetivo: transformar "o Claude faz X" numa sequência clara de passos que um estranho conseguiria seguir.

Para cada passo do processo, escolha entre:

1. O que exatamente acontece nesse momento? Me descreve como se eu nunca tivesse visto.
2. Aqui tem alguma decisão a tomar? Tipo "se for assim, faz isso; se for de outro jeito, faz aquilo"?
3. O que você precisa entregar nesse passo, e o que o Claude deveria descobrir ou fazer sozinho?
4. Tem alguma regra fixa que ele sempre tem que seguir aqui? Algo que nunca pode faltar?
5. Me mostra um exemplo real entrando e o resultado ideal saindo desse passo.

Perguntas sobre estilo e formato, quando o resultado é um texto:

- Como você quer que soe? Formal, direto, acolhedor? Me dá um exemplo de um texto que tem a sua cara e um que não tem.
- O resultado tem seções fixas? Quais são obrigatórias e quais são opcionais?
- Tem um tamanho ideal? Curto e objetivo, ou detalhado?

Exemplo de decisão (ramificação) por profissão:

- Advogado: "Se o contrato tem cláusula de foro, destaca em separado; se não tem, avisa que está ausente."
- Professor: "Se a aula é para o fundamental, linguagem mais lúdica; se é para o médio, mais técnica."
- Médico: "Se o exame veio alterado, sinaliza no topo; se veio normal, segue o padrão."
- Serviço técnico: "Se a peça está em falta no estoque, sugere equivalente; se não, mantém a original."

## Fase 3: O que pode dar errado

Objetivo: cobrir as bordas que o iniciante não enxerga sozinho.

1. E quando a informação chega incompleta ou bagunçada? O que a skill deveria fazer?
2. Tem algum caso em que é melhor a skill parar e te perguntar antes de continuar?
3. Qual é o mínimo que você precisa ter em mãos pra valer a pena usar a skill?
4. Tem algum tipo de pedido que essa skill NÃO deveria atender, mesmo que pareça parecido?

Exemplos por profissão:

- Advogado: contrato escaneado com páginas faltando; a skill deve avisar quais páginas faltam em vez de inventar.
- Professor: tema vago demais ("ciências"); a skill deve pedir a série e o assunto específico.
- Médico: dado sensível incompleto; a skill deve sinalizar a falta, nunca preencher por conta própria.
- Serviço técnico: foto sem o número de série; a skill deve pedir antes de fechar o orçamento.

## Fase 4: O espelho

Não é hora de pergunta nova. Resuma no formato do bloco que está na SKILL.md (objetivo, o que entra, passo a passo, o que sai, se der errado) e faça uma única pergunta aberta: "O que eu errei ou esqueci aqui?"

## Exemplos de como aprofundar uma resposta vaga

Use estes modelos quando a resposta for genérica. Sempre com gentileza, nunca como cobrança.

- Pessoa: "Aí ele analisa o documento." Você: "Analisa procurando o quê, exatamente? Me dá um exemplo: esse documento entra, e o que você gostaria de ver destacado?"
- Pessoa: "Tem que ficar no meu tom." Você: "Me ajuda a descrever seu tom em palavras simples. Cola aqui um trecho que tem a sua cara e um que claramente não tem. O que muda entre os dois?"
- Pessoa: "Formata bonito." Você: "O que é 'bonito' pra você aqui? Quais seções têm que aparecer, e em que ordem? Me mostra um resultado que você consideraria perfeito."

## Frases-gatilho: como descobrir junto com a pessoa

Antes da Fase 5, descubra com quais frases ela vai chamar a skill no futuro. Pergunte: "Quando você for usar isso de novo, o que você naturalmente escreveria pro Claude?" Anote as frases reais dela, com as palavras dela. Elas entram na descrição da skill e no fluxograma. Quanto mais perto do jeito real de falar da pessoa, melhor a skill vai disparar na hora certa.
