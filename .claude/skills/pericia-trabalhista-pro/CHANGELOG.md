# CHANGELOG — pericia-trabalhista-pro

## v3.0.0 (2026-07-16) — Reconstrução autossuficiente por auditoria
- [ESTRUTURA] Skill tornada AUTOCONTIDA: os 17 arquivos externos que o SKILL.md
  referenciava (modules/, references/, agentes/, examples/, templates/) e que
  **nunca existiram** foram consolidados dentro do próprio SKILL.md. A "regra de
  fallback" deixa de ser o caminho padrão — a skill agora funciona plenamente sozinha.
- [CORRIGE — FACTUAL] Portaria MTE 2.021/2025 estava descrita errado como
  "modificação da NR-15". Correto (fontes gov.br/DOU): aprova o **Anexo V da NR-16**
  (motocicletas) e insere itens 15.4.1.3 (NR-15) e 16.3.1 (NR-16) sobre
  disponibilização de laudos; vigência do Anexo V em abril/2026.
- [CORRIGE — FACTUAL] Portaria MTE 1.411/2025 confirmada: Anexo VI da NR-16
  (agentes de trânsito), regulamenta Lei 14.684/2023 / art. 193, III CLT.
- [CORRIGE] Razão social: "Consultoria em Segurança e Saúde **do** Trabalho" →
  "Consultoria **Personalizada** em Segurança e Saúde **no** Trabalho" (forma oficial,
  alinhada à aet-premium). Crítico em peça judicial.
- [CONSOLIDA] Tabela-mestre NR-15 (anexos × quant/qual × NHO) trazida para o corpo,
  substituindo o `guia-agentes-nr15-nr16.md` inexistente.
- [CONSOLIDA] Estrutura dos 4 módulos (A-Impugnação, B-Quesitos, C-Parecer, D-Vistoria)
  escrita no SKILL.md, substituindo os `modules/*.md` inexistentes.
- [CONSOLIDA] Fundamentação jurídica ampliada com as entradas das novas portarias.
- [REMOVE] Notas de governança de skill ("remova a impugnador-pericial", "STATUS DOS
  ARQUIVOS: só o SKILL.md existe") — ruído operacional movido para cá.
- [ADD] Vibração: NHO-09 (corpo inteiro) e NHO-10 (mãos-braços) — antes citava
  "NHO-09/10" sem distinção.
- [ADD] Comportamento em ambiente limitado + logo por injeção programática (alinhado
  ao padrão da aet-premium v4.0).
- [MANTIDO] PASSO 0-B (verificação TST), regra de premissas explícitas, Vetores A-E,
  marcadores [CONFERIR TST], cautela da Súmula 228, alerta anti-OJ 278 SDI-1.

## v2.1.0 e anteriores
Regra de premissas explícitas (v2.1.0); PASSO 0-B, tabelas em Markdown, alertas de
portarias 2025, resolução de conflito com impugnador-pericial (v2.0.0); versão inicial
unificada com 4 módulos + Vetores A-E (v1.0.0). Todas operavam com os arquivos externos
ausentes (fallback permanente) — corrigido na v3.0.0.
