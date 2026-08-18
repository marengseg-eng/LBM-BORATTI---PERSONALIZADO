# CHANGELOG — relatorio-inspecao-sst

## v2.0.0 (2026-07-16) — Correções cirúrgicas por auditoria
- [CRÍTICO] Rastreabilidade de achados (Regra 7): achado constatado (OBSERVADO, de
  foto ou relato) vs. item pré-preenchido [MODELO — editar conforme observado].
  Sem fotos/relato → relatório-modelo com aviso; KPIs contam só OBSERVADO. Corrige
  o Caso 1 dos examples, que ensinava a fabricar achados (corrosão/CRÍTICO sem foto)
  em documento com força probatória — contradizendo o próprio anti-padrão nº 1.
- [CRÍTICO] Paginação dinâmica: botões ➕ + height:297mm/overflow:hidden cortavam
  cards novos em silêncio na impressão. Agora JS cria nova .pagina ao exceder altura.
- [CORRIGE] ALTO ganhou cor própria (--alto #d35400) — antes compartilhava #c0392b
  com CRÍTICO e não existia variável CSS, tornando badges indistinguíveis.
- [CORRIGE] "8 seções" no MODO 1 vs 9 seções reais → 9 em todo o documento.
- [CORRIGE] "Inspector" → "inspetor"; razão social oficial; nome do RT no bloco de
  assinatura (antes só credenciais).
- [ADD] Fotos e logos por injeção de script (modelo não digita base64; fotos de
  /mnt/user-data/uploads convertidas por bash/Python com marcadores __FOTO_XX__).
- [ADD] Aviso de verificação de vigência no topo de normas_inspecao.md (NRs
  renumeradas recentemente; lista é referência rápida, texto vigente prevalece).
- [ADD] Comportamento em ambiente limitado (nunca fingir geração de arquivo).
- [MANTIDO] 4 modos, fluxo rápido (1 pergunta máx. 5 campos), matriz P×C,
  integração com outras skills, 5W2H, toolbar, badges automáticos.

## v1.0.0
Versão inicial — estrutura sólida (todos os arquivos de apoio existentes), com os
defeitos pontuais corrigidos acima.
