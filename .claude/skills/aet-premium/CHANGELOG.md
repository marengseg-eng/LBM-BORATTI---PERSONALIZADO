# CHANGELOG — aet-premium

## v4.0.0 (2026-07-16) — Reconstrução por auditoria de engenharia de prompt
- [REESTRUTURA] SKILL.md reduzido de ~25 KB para ~11 KB: só política; specs de output
  movidas para `references/outputs-html.md`; detalhe das 13 seções movido para
  `references/estrutura-relatorio.md`
- [CORRIGE] Contradição de breakpoints (4 vs 3): definição única — 3 breakpoints
  responsivos (900/560/380) + @media print + prefers-reduced-motion
- [CORRIGE] Contradição "self-contained sem CDN" vs Google Fonts: princípio definido
  com precisão (JS/CSS/dados embutidos; fontes são a única exceção)
- [CORRIGE] "Nota LBM" da matriz reescrita: rótulo "Alto" em vez de "Moderado" é
  APENAS nomenclatura da escala — classificação decorre só de Probabilidade × Severidade
- [NOVO] Injeção programática de logo/base64 por script — proibido o modelo digitar base64
- [NOVO] Montagem de HTML por seções via script (anti-truncamento)
- [NOVO] Schema de variáveis {{VARIAVEL}} substituindo [INSERIR DADO]
- [NOVO] Eco pré-geração (≤8 linhas, não bloqueante) antes de AET completa
- [NOVO] Mini-exemplos few-shot de rotulagem epistêmica (correto vs proibido)
- [NOVO] NR-17 ancorada (Portaria MTP 423/2021, com ressalva de confirmação oficial)
- [REMOVE] Tags de versão [v3.1.x] e changelog de dentro do prompt (movido para cá)
- [REMOVE] Duplicações de terminologia/credenciais/fontes — fonte única de verdade
- [MANTIDO] Hierarquia de prioridades (7 níveis), rótulos epistêmicos (5), regra de
  não bloqueio, roteamento Passos 0–5, tabela ERGOSTORE, regra das 4 metodologias
  para soldagem/caldeiraria, comportamento em ambiente limitado

## v3.2.0 e anteriores
Ver histórico embutido nas versões antigas do SKILL.md (hierarquia de prioridades,
rótulos epistêmicos, comportamento em ambiente limitado, não bloqueio, Full Edit
Engine v3.1.3, QA versionado v3.1.1–v3.1.4).
