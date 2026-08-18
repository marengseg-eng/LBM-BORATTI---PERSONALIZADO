# Changelog

## 1.0.0 — 18/08/2026
Versão inicial, derivada do parecer `PT-NR17-GR-080826` (GR Montagens Industriais Guariba, REV. 05).

- Fluxo de 3 passos com trava: eco dos dados → briefing → HTML só após autorização expressa.
- Template A4 de 2 folhas: dashboard (donut de 12 fatias + ranking) e parecer (tabela de
  providências + conclusão técnica + assinatura).
- `scripts/calcular.py` — Σ, índice global, ranking, geometria do donut, faixas, data de
  reavaliação e regra de veredicto (favorável / com ressalvas / desfavorável).
- `scripts/montar.py` — preenche o template; bloqueia a emissão em caso de AEP inconsistente ou
  índice global divergente; avisa quando o texto do ciclo contradiz o status da AET.
- Referências: base normativa NR-01/NR-17, faixas de classificação e providências padrão.

### Convenções extraídas do documento original
- `Base visual` = **soma** dos escores exibidos (247 no caso GR), não a média.
- `Índice global` = `round(Σ ÷ nº de fatores)` → 247 ÷ 12 = 21%.
- Ranking em ordem decrescente do escore **não arredondado**.
- Código do parecer: `PT-NR17-{INICIAIS}-{DDMMAA}`.
- Data de reavaliação: `avaliação + 1 ano − 1 dia`.
