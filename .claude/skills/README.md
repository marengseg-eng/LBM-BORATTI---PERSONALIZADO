# Skills — backup versionado

Backup das skills da LBM BORATTI. Servem a dois propósitos: **backup** (o container das sessões do
Claude é efêmero e a pasta sincronizada é recriada do zero a cada sessão) e **uso** — o Claude Code
carrega automaticamente as skills daqui quando esta pasta do projeto está aberta.

Última sincronização: **18/08/2026** · 21 skills · ~5 MB

## O que está aqui

| Skill | O que faz | Atualizada em |
|---|---|---|
| `aet-premium` | Cria Análises Ergonômicas do Trabalho (AET) completas para LBM BORATTI Consultoria Personalizada em Segurança e Saúde no Trabalho, conforme NR-17, NR-… | 16/07/2026 |
| `apr-pop-sst` | Gera APR (Análise Preliminar de Riscos) e POP (Procedimento Operacional Padrão) no nível de UMA tarefa ou atividade específica, para LBM BORATTI, anco… | 07/07/2026 |
| `cipa-eleicao` | Gera documentos completos de CIPA — Comissão Interna de Prevenção de Acidentes e de Assédio (CIPA+A) para LBM BORATTI Consultoria em SST, conforme NR-… | 07/07/2026 |
| `conselheiro-estrategico-sst` | Atua como conselheiro estratégico de negócios para consultoria SST: posicionamento de mercado, precificação, expansão de portfólio, prospecção, difere… | 07/07/2026 |
| `consultor-de-nrs-sst` | Interpreta e aplica Normas Regulamentadoras a casos reais | 07/07/2026 |
| `dds-sst` | Gera Diálogos Diários de Segurança (DDS) completos e profissionais para LBM BORATTI Consultoria Personalizada em Segurança e Saúde no Trabalho | 19/07/2026 |
| `frontend-design` | Crie interfaces front-end distintas e de nível profissional com alta qualidade de design | 14/05/2026 |
| `humanizer` | Revisa e reescreve textos gerados por IA para soarem naturais e humanos, removendo padrões típicos de LLMs | 03/06/2026 |
| `investigador-de-acidentes-sst` | Conduz investigação de acidente ou quase-acidente de forma estruturada usando Árvore de Causas e 5 Porquês | 07/07/2026 |
| `parecer-tecnico-nr01-nr17` | Parecer Técnico conclusivo de Fatores de Riscos Psicossociais + AEP/AET (NR-01 e NR-17), em 2 folhas A4 | 18/08/2026 |
| `pdf-a4-optimizer` | otimizar e normalizar arquivos pdf para saida profissional em folha iso a4, corrigindo tamanho de pagina, escala, orientacao, margens, centralizacao,… | 28/05/2026 |
| `pericia-trabalhista-pro` | Skill AUTOSSUFICIENTE de Perícia Trabalhista (LBM BORATTI / SST) | 16/07/2026 |
| `ppp-ltcat-lbm` | Gera e revisa PPP (Perfil Profissiográfico Previdenciário, Anexo XV) e LTCAT (Laudo Técnico das Condições Ambientais do Trabalho) para a LBM BORATTI C… | 12/07/2026 |
| `prompt-master` | Gera prompts otimizados para qualquer ferramenta de IA | 17/05/2026 |
| `proposta-comercial-sst` | Cria Propostas Técnicas comerciais para a LBM BORATTI Consultoria Personalizada em Segurança e Saúde no Trabalho | 16/07/2026 |
| `psicossocial-nr01` | Gera avaliações completas de Fatores de Riscos Psicossociais para LBM BORATTI Consultoria em SST, em conformidade com NR-01 revisada (Portaria MTE 1.4… | 07/07/2026 |
| `relatorio-inspecao-sst` | Gera Relatórios de Inspeção de Segurança do Trabalho (RIS) para LBM BORATTI Consultoria em SST, conforme NR-01, NR-06, NR-10, NR-12, NR-13, NR-15, NR-… | 16/07/2026 |
| `resumo-psicossocial` | Gera uma folha-resumo HTML (one-pager A4) da Avaliação de Fatores de Risco Psicossociais para LBM BORATTI Consultoria em SST | 07/07/2026 |
| `skill-generator` | Cria pacotes de Skill completos para Claude Code com SKILL.md, examples.md, playbook.md e scripts/. | 19/04/2026 |
| `skill-planner` | Mentor que conduz um usuário iniciante, passo a passo, no planejamento e na criação da sua primeira skill para o Claude, com linguagem simples em port… | 07/06/2026 |
| `treinamentos-sst` | Cria treinamentos e apresentações de SST para LBM BORATTI Consultoria em SST: roteiros completos por NR com estrutura pedagógica focada em mudança de… | 07/07/2026 |

## O que NÃO está aqui, de propósito

As skills mantidas pela Anthropic — `brand-guidelines`, `canvas-design`, `docx`, `morning`, `pdf`, `pptx`, `skill-creator`, `web-artifacts-builder`, `xlsx` — ficaram de fora. São redistribuídas por eles
e reaparecem sozinhas em cada sessão; versioná-las custaria ~10 MB de schemas XSD e fontes TTF sem
nada a proteger.

## Onde cada cópia vive

| Local | Sincroniza sozinho? | Sobrevive à máquina? |
|---|---|---|
| Conta claude.ai (Settings → Capabilities → Skills) | sim, para toda sessão | sim |
| `~/.claude/skills/` no PC | não | não |
| `.claude/skills/` deste repo (aqui) | não, mas carrega neste projeto | sim |

A conta claude.ai continua sendo a fonte de verdade para o dia a dia. Este repo é a rede de
segurança: se algo sumir de lá, o conteúdo está aqui.

## Como atualizar este backup

Depois de editar uma skill em claude.ai, peça numa sessão do Claude Code:

> ressincroniza o backup das skills no repo

Ou manualmente, dentro de uma sessão remota:

```bash
cp -r /root/.claude/skills/synced/<nome-da-skill> .claude/skills/
git add .claude/skills && git commit -m "Atualiza backup da skill <nome>"
```

## Skills que só existem no PC

Skill criada direto em `~/.claude/skills/` no VS Code **não** aparece na conta claude.ai e **não**
chega aqui sozinha. Para trazer, do terminal do VS Code (Windows):

```powershell
robocopy "$env:USERPROFILE\.claude\skills\<nome>" ".claude\skills\<nome>" /E
git add .claude/skills && git commit -m "Adiciona skill <nome> vinda do VS Code" && git push
```
