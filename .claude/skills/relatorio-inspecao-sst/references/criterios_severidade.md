# Critérios de Severidade e Sistema de Badges

Referência técnica para classificação de achados no Relatório de Inspeção SST — LBM BORATTI.

---

## 1. MATRIZ DE CRITICIDADE (Probabilidade × Consequência)

Alinhada com metodologia AIHA e RGI (MTE).

| | Improvável (1) | Remota (2) | Possível (3) | Provável (4) | Frequente (5) |
|---|---|---|---|---|---|
| **Baixo (1)** | 1 | 2 | 3 | 4 | 5 |
| **Médio (2)** | 2 | 4 | 6 | 8 | 10 |
| **Alto (3)** | 3 | 6 | 9 | 12 | 15 |
| **Crítico (4)** | 4 | 8 | 12 | 16 | 20 |

**Score → Nível de ação:**
- 1–4: BAIXO (prazo 90 dias)
- 5–9: MÉDIO (prazo 30 dias)
- 10–15: ALTO (prazo 7 dias)
- 16–25: CRÍTICO (imediato / interdição)

---

## 2. DEFINIÇÃO DOS NÍVEIS

### 🔴 CRÍTICO — Prazo: Imediato / Interdição
- Risco de morte ou lesão grave iminente
- NR-12: máquina sem proteção em operação
- NR-35: trabalho em altura sem EPI ou ancoragem
- NR-13: caldeira sem válvula de segurança
- NR-10: circuito energizado sem sinalização
- **Ação**: interditar o equipamento/área até correção comprovada

### 🟠 ALTO — Prazo: ≤ 7 dias
- Risco de lesão com afastamento (LT/LTI)
- EPI sem CA válido em atividade de risco
- Extintor vencido em área com carga de incêndio alta
- **Ação**: correção em prazo curto, comunicar SESMT/CIPA

### 🟡 MÉDIO — Prazo: ≤ 30 dias
- Risco de lesão sem afastamento (LTR)
- Sinalização faltando (NR-26)
- Organização precária com risco de tropeço
- EPI sendo usado incorretamente (sem lesão imediata)
- **Ação**: plano de ação com responsável e data

### 🟢 BAIXO — Prazo: ≤ 90 dias
- Não-conformidade administrativa / preventiva
- Melhorias de housekeeping
- Documentação desatualizada sem risco imediato
- **Ação**: incluir no plano de ação do PGR

---

## 3. MAPA DE BADGES AUTO-COLORIDOS

### 3.1 Tabela de Keywords → Classe CSS

| Palavras detectadas (substring, case-insensitive) | Classe CSS | Cor visual |
|---|---|---|
| `conforme`, `ok`, `aprovado`, `✓`, `check` | `badge-conf` | 🟢 Verde escuro #1e8449 |
| `baixo`, `low`, `leve` | `badge-baixo` | 🟢 Verde claro #1e8449 |
| `crítico`, `critico`, `imediato`, `fatal`, `grave`, `✗`, `reprovado` | `badge-alto` | 🔴 Vermelho #c0392b |
| `nc`, `n/c`, `não conforme`, `nao conforme` | `badge-nc` | 🔴 Vermelho escuro #922b21 |
| `médio`, `medio`, `parcial`, `atenção`, `atencao`, `moderado`, `prazo`, `dias` | `badge-medio` | 🟡 Amarelo #956d00 |
| `info`, `observa`, `nota` | `badge-info` | 🔵 Azul #2a4f7c |

**Regra de precedência**: a primeira regra que casar é aplicada, na ordem da tabela.
- `conforme` é verificado ANTES de `não conforme` para evitar falso negativo.

### 3.2 CSS Classes

```css
.badge { display:inline-flex; align-items:center; gap:4px; padding:3px 10px;
         border-radius:20px; font-size:0.78rem; font-weight:700; cursor:default; }
.badge-conf   { background:#d4efdf; color:#1e8449; border:1px solid #1e8449; }
.badge-baixo  { background:#d4efdf; color:#1e8449; border:1px solid #1e8449; }
.badge-alto   { background:#fadbd8; color:#c0392b; border:1px solid #c0392b; }
.badge-nc     { background:#f5b7b1; color:#922b21; border:1px solid #922b21; }
.badge-medio  { background:#fef9e7; color:#956d00; border:1px solid #f0c000; }
.badge-parcial{ background:#fdebd0; color:#935116; border:1px solid #e59866; }
.badge-info   { background:#d6eaf8; color:#2a4f7c; border:1px solid #2a4f7c; }
.badge .bt    { outline:none; min-width:40px; }
.badge .be    { opacity:0.6; font-size:0.7rem; cursor:pointer; }
.badge .be:hover { opacity:1; }
```

### 3.3 Função JavaScript de Auto-Color

```javascript
const BADGE_MAP = [
  { keys: ['conforme','ok','aprovado','\u2713','check'],                          cls: 'badge-conf'   },
  { keys: ['baixo','low','leve'],                                                  cls: 'badge-baixo'  },
  { keys: ['critico','crítico','imediato','fatal','grave','\u2717','reprovado'],  cls: 'badge-alto'   },
  { keys: ['nc','n/c','não conforme','nao conforme'],                             cls: 'badge-nc'     },
  { keys: ['medio','médio','parcial','atencao','atenção','moderado','dias','prazo','semanas'], cls: 'badge-medio' },
  { keys: ['parcial'],                                                             cls: 'badge-parcial'},
  { keys: ['info','observa','nota'],                                               cls: 'badge-info'   },
];
const ALL_BADGE_CLS = ['badge-nc','badge-conf','badge-parcial','badge-alto','badge-medio','badge-baixo','badge-info'];

function autoColorBadge(btEl) {
  const txt = (btEl.textContent || '').toLowerCase().trim();
  const badge = btEl.parentElement;
  if (!badge || !badge.classList.contains('badge')) return;
  for (const rule of BADGE_MAP) {
    if (rule.keys.some(k => txt.includes(k))) {
      ALL_BADGE_CLS.forEach(c => badge.classList.remove(c));
      badge.classList.add(rule.cls);
      return;
    }
  }
}

// Delegação global — captura qualquer badge editado na página
document.addEventListener('input', e => {
  if (e.target.classList.contains('bt')) autoColorBadge(e.target);
});
```

---

## 4. CÓDIGOS NC — PADRÃO DE NUMERAÇÃO

- Formato: `NC-001`, `NC-002`, `NC-003`…
- Ordenação: Crítico → Alto → Médio → Baixo
- Prefixo por área quando houver múltiplas: `NC-MECA-001`, `NC-ELET-001`
- Rastreabilidade: cada NC deve aparecer na seção AI/CI, na foto correspondente e no card 5W2H

---

## 5. PRAZO E SEMÁFORO 5W2H

```javascript
function atualizarSemaforo(prazoStr) {
  const hoje = new Date();
  const prazo = new Date(prazoStr);
  const diff = (prazo - hoje) / (1000 * 60 * 60 * 24); // dias
  if (diff < 0)   return { cor: '#c0392b', label: 'VENCIDO' };
  if (diff <= 7)  return { cor: '#e67e22', label: 'URGENTE' };
  if (diff <= 30) return { cor: '#f0c000', label: 'PRÓXIMO' };
  return { cor: '#1e8449', label: 'OK' };
}
```
