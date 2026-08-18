---
name: humanizer
description: "Revisa e reescreve textos gerados por IA para soarem naturais e humanos, removendo padrões típicos de LLMs. Use SEMPRE que mencionar: humanizar texto, remover padrão IA, texto parece IA, soar mais humano, revisar escrita artificial, limpar texto gerado, texto robótico, tom de chatbot, texto sem alma, ou pedir para reescrever conteúdo que \"parece ChatGPT\". Também acionar quando o usuário fornecer um texto e pedir para \"melhorar o tom\", \"tornar mais natural\", \"tirar o ar de IA\" ou \"deixar com minha voz\". Detecta e corrige: vocabulário de alta frequência de LLMs (delve, crucial, pivotal, underscore, highlight), abuso de travessão, listas com negrito mecânico, conclusões genéricas otimistas, hedging excessivo, regra dos três forçada, frases de enchimento, artefatos de chat e tom bajulador. Suporta calibração de voz com amostra do próprio estilo do usuário. Output: rascunho humanizado → auditoria de resíduos → versão final revisada."
---

# humanizer

**Versão:** 2.5.1  
**Licença:** MIT  
**Compatibilidade:** claude-code, opencode  
**Ferramentas permitidas:** Read, Write, Edit, Grep, Glob, AskUserQuestion

---

## Quando acionar

Acionar quando o usuário quiser editar ou revisar texto para que soe mais natural e menos gerado por IA. Baseado no guia "Signs of AI writing" da Wikipedia (WikiProject AI Cleanup).

---

## O que faz

Identifica padrões de escrita de IA e reescreve o texto para soar humano. Além de remover os padrões negativos, injeta personalidade, voz e alma no texto final.

---

## Calibração de Voz

Se o usuário fornecer uma amostra da própria escrita, a skill analisa antes de reescrever:

- Padrões de tamanho de frase (curto e direto, longo e fluido, misto)
- Nível de vocabulário (casual, acadêmico, intermediário)
- Como inicia parágrafos
- Hábitos de pontuação
- Frases recorrentes ou vícios verbais
- Como faz transições

Sem amostra, usa voz natural, variada e com opinião como padrão.

**Como fornecer amostra:**

Inline: "Humanize este texto. Aqui está uma amostra da minha escrita: [amostra]"

Por arquivo: "Humanize este texto. Use meu estilo de escrita em [caminho do arquivo] como referência."

---

## Personalidade e Alma

Evitar padrões de IA é apenas metade do trabalho. Escrita estéril e sem voz é tão óbvia quanto escrita de IA. Boa escrita tem um humano por trás.

**Sinais de escrita sem alma (mesmo tecnicamente limpa):**

- Todas as frases têm o mesmo comprimento e estrutura
- Sem opiniões, apenas relato neutro
- Sem reconhecimento de incerteza ou sentimentos mistos
- Sem perspectiva em primeira pessoa quando caberia
- Sem humor, sem personalidade
- Parece artigo de enciclopédia ou release de imprensa

**Como adicionar voz:**

Ter opiniões e reagir aos fatos, não apenas relatá-los. Variar o ritmo (frase curta, depois uma mais longa que toma seu tempo). Reconhecer complexidade ("isso é impressionante, mas também um pouco perturbador"). Usar "eu" quando couber. Deixar alguma imperfeição entrar — tangentes e observações laterais são humanas. Ser específico sobre sentimentos, não apenas "preocupante".

---

## Padrões Detectados e Corrigidos

### Padrões de conteúdo

**Ênfase excessiva em significância e legado**

Palavras a observar: stands/serves as, is a testament/reminder, vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance, reflects broader, symbolizing its enduring, contributing to the, setting the stage for, marking/shaping the, represents a shift, key turning point, evolving landscape, indelible mark, deeply rooted.

Problema: o texto infla a importância adicionando afirmações sobre como aspectos arbitrários "representam" ou "contribuem para" um tema maior.

**Ênfase excessiva em notabilidade e cobertura**

Palavras a observar: independent coverage, local/regional/national media outlets, active social media presence.

Problema: listas de veículos sem contexto, afirmações de notabilidade sem base.

**Análises superficiais com terminações em -ing**

Palavras a observar: highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, fostering, encompassing, showcasing.

Problema: a IA acrescenta frases com particípio presente para adicionar profundidade falsa.

**Linguagem promocional e publicitária**

Palavras a observar: boasts a, vibrant, rich (figurativo), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, breathtaking, must-visit, stunning.

Problema: tom neutro quebrado, especialmente em temas de "patrimônio cultural".

**Atribuições vagas (weasel words)**

Palavras a observar: Industry reports, Observers have cited, Experts argue, Some critics argue, several sources.

Problema: opiniões atribuídas a autoridades vagas sem fontes específicas.

**Seções formulaicas de desafios e perspectivas**

Palavras a observar: Despite its... faces several challenges, Despite these challenges, Challenges and Legacy, Future Outlook.

Problema: artigos gerados por IA incluem seções formulaicas de "Desafios" que não acrescentam nada concreto.

---

### Padrões de linguagem

**Vocabulário de IA de alta frequência**

Palavras a observar: actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verbo), interplay, intricate/intricacies, key (adjetivo), landscape (substantivo abstrato), pivotal, showcase, tapestry (abstrato), testament, underscore (verbo), valuable, vibrant.

Essas palavras aparecem com frequência muito maior em textos pós-2023.

**Substituição de "ser/estar" (copula avoidance)**

Palavras a observar: serves as, stands as, marks, represents [a], boasts, features, offers [a].

Problema: a IA substitui construções simples ("é", "tem") por construções elaboradas.

**Paralelismos negativos e negações de cauda**

Problema: construções como "Not only...but..." ou "It's not just about X, it's Y" são usadas em excesso. Também fragmentos de negação acrescentados no final da frase ("no guessing", "no wasted motion") em vez de cláusulas reais.

**Regra dos três forçada**

Problema: a IA agrupa ideias em trios para parecer abrangente.

**Variação elegante (troca de sinônimos)**

Problema: o código de penalidade de repetição da IA causa substituição excessiva de sinônimos para o mesmo referente.

**Intervalos falsos**

Problema: construções "from X to Y" onde X e Y não estão numa escala real ou significativa.

**Voz passiva e fragmentos sem sujeito**

Problema: a IA esconde o agente ou suprime o sujeito ("No configuration file needed", "The results are preserved automatically").

---

### Padrões de estilo

**Abuso do travessão**

Problema: a IA usa travessões com frequência maior que humanos, imitando escrita "incisiva". A maioria pode ser reescrita com vírgula, ponto ou parênteses.

**Excesso de negrito**

Problema: destaques mecânicos de frases em negrito sem critério.

**Listas com cabeçalhos em negrito seguidos de dois-pontos**

Problema: a IA produz listas onde cada item começa com cabeçalho em negrito seguido de dois-pontos antes do conteúdo real.

**Title Case em títulos**

Problema: a IA capitaliza todas as palavras principais em cabeçalhos.

**Emojis decorativos**

Problema: emojis decorando cabeçalhos ou marcadores de lista.

**Aspas curvas**

Problema: uso de aspas curvas ("...") em vez de retas ("...").

---

### Padrões de comunicação

**Artefatos de chat**

Palavras a observar: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

Problema: texto de resposta de chatbot colado como conteúdo.

**Avisos de corte de conhecimento**

Palavras a observar: as of [date], Up to my last training update, While specific details are limited, based on available information.

Problema: disclaimers da IA sobre informação incompleta deixados no texto.

**Tom serviçal e bajulador**

Problema: linguagem excessivamente positiva e complacente ("Great question!", "You're absolutely right!", "That's an excellent point").

---

### Preenchimentos e hedging

**Frases de enchimento**

- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

**Hedging excessivo**

Problema: qualificação excessiva de afirmações ("could potentially possibly be argued that... might have some effect").

**Conclusões positivas genéricas**

Problema: finais vagos e otimistas ("The future looks bright", "Exciting times lie ahead", "This represents a major step in the right direction").

**Hifenização excessiva de pares comuns**

Palavras a observar: third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end.

Problema: a IA hifen iza pares comuns com consistência perfeita. Humanos raramente fazem isso de forma uniforme.

**Tropos de autoridade persuasiva**

Palavras a observar: The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter.

Problema: a IA usa essas frases para fingir que está cortando o ruído e chegando a uma verdade mais profunda, quando a frase seguinte apenas reafirma um ponto ordinário com cerimônia extra.

**Sinalizações e anúncios**

Palavras a observar: Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado.

Problema: a IA anuncia o que vai fazer em vez de simplesmente fazer.

**Cabeçalhos fragmentados**

Problema: cabeçalho seguido de uma frase que apenas reafirma o cabeçalho antes do conteúdo real começar.

---

## Processo de Execução

1. Ler o texto com atenção
2. Identificar todos os padrões listados acima
3. Reescrever cada seção problemática
4. Garantir que o texto revisado:
   - Soa natural quando lido em voz alta
   - Varia a estrutura de frases de forma natural
   - Usa detalhes específicos em vez de afirmações vagas
   - Mantém tom adequado ao contexto
   - Usa construções simples ("é", "tem", "faz") onde cabem
5. Apresentar rascunho humanizado
6. Aplicar auditoria: "O que torna o texto abaixo obviamente gerado por IA?"
7. Responder brevemente com os resíduos restantes
8. Apresentar versão final revisada

---

## Formato de Saída

1. Rascunho reescrito
2. Auditoria resumida: "O que ainda soa como IA?" (bullets breves)
3. Versão final
4. Resumo das alterações feitas (opcional, quando útil)

---

## Referência

Baseado em [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), mantido pelo WikiProject AI Cleanup.

Princípio central da Wikipedia: "LLMs usam algoritmos estatísticos para adivinhar o que vem a seguir. O resultado tende para o resultado estatisticamente mais provável que se aplica à maior variedade de casos possível."
