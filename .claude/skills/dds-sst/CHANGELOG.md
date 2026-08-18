# CHANGELOG — dds-sst

## v2.0.0 (2026-07-16) — Correções cirúrgicas por auditoria
- [CORRIGE] Logo fantasma: SKILL.md mandava carregar assets/logo_lbm_base64.txt,
  mas a pasta assets não existia (QA exigia logo em todas as folhas — impossível).
  Asset real bundlado (35KB, copiado da aet-premium), carregamento tolerante a
  prefixo data: e regra de fallback textual quando inacessível.
- [ADD] Regra anti-invenção de dados: estatística só com fonte real citada no texto
  (AEAT/MTE, Fundacentro, OIT); sem certeza → alerta normativo qualitativo ou
  {{DADO_ESTATISTICO_A_CONFIRMAR}}. DDS é assinado por trabalhadores com CREA no
  rodapé — estatística fabricada era o maior risco da skill.
- [CORRIGE] Razão social oficial em todas as ocorrências (título, identificação,
  rodapés do template).
- [MANTIDO] Integralmente: engenharia de impressão validada (@page fora do @media
  print, height 297mm p/ flex:1, anti-espaço-branco, lição POWER), fluxo
  briefing → "gera o HTML", template completo com {{VARS}}, tabela de temas +
  fallback, DDS validados de referência.

## v1.x
Versão validada em campo (NEW PRO 3 folhas / POWER 4 folhas), com o asset do logo
ausente e sem regra anti-estatística.
