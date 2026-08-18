# FULL EDIT ENGINE v3 — AET Premium HTML

Este documento especifica o comportamento do **mecanismo de edição bidirecional**
embutido em todo AET gerado em formato HTML pelo MÉTODO LBM BORATTI.

Aplicar **sempre** quando o Output 1 (HTML Premium) for gerado.

---

## Princípios de design

1. **Edição inline em qualquer campo do documento** — sem sair do HTML, sem formulários externos
2. **Sincronização bidirecional S4↔S7** — qualquer alteração na Seção 4 (Caracterização)
   reflete automaticamente na Seção 7 (Análise NR-17) e vice-versa
3. **Persistência local** — todas as edições sobrevivem a reloads via `localStorage`
4. **Exportação dinâmica CSV/JSON** — usuário exporta dados editados a qualquer momento
5. **Indicador visual de edição** — sempre claro quando um campo foi modificado vs. original
6. **Zero dependências JavaScript externas** — tudo vanilla JS embutido no próprio HTML
   (⚠ **não** se estende a fontes web: DM Serif Display + DM Sans + JetBrains Mono são
   obrigatórias via Google Fonts ou `@font-face` base64 — ver seção "Tipografia premium")

---

## Implementação — 6 camadas

### Camada 1 — Campos `contenteditable` universais

Todos os campos editáveis recebem a classe `.editable` e atributo `contenteditable="true"`.
Elementos elegíveis:

- Campos de identificação (empresa, CNPJ, endereço, CBO, data)
- Descrições de tarefa prescrita/real
- Achados ergonômicos
- Scores RULA/REBA (manuais, caso o usuário queira sobrescrever)
- Células de tabelas (PAE, Matriz AIHA, Checklist NR-17)
- Conclusões e recomendações
- Notas do responsável técnico

```html
<span class="editable" data-field="empresa.nome" data-sync="s4,s7">
  ELETROSERT SERVICE LTDA
</span>
```

### Camada 2 — Mecanismo de sincronização S4↔S7

Cada campo editável tem atributo `data-sync` listando as seções que devem espelhá-lo.

```javascript
document.querySelectorAll('.editable[data-sync]').forEach(el => {
  el.addEventListener('input', (e) => {
    const field = e.target.dataset.field;
    const sections = e.target.dataset.sync.split(',');
    const value = e.target.textContent;
    sections.forEach(sec => {
      document.querySelectorAll(
        `[data-field="${field}"]:not([data-section="${e.target.dataset.section}"])`
      ).forEach(target => {
        if (target !== e.target) target.textContent = value;
      });
    });
    markAsModified(e.target);
    saveToLocalStorage();
  });
});
```

### Camada 3 — Persistência em `localStorage`

```javascript
const STORAGE_KEY = `aet-${DOCUMENT_ID}`;

function saveToLocalStorage() {
  const data = {};
  document.querySelectorAll('.editable[data-field]').forEach(el => {
    data[el.dataset.field] = el.textContent;
  });
  localStorage.setItem(STORAGE_KEY, JSON.stringify({
    data,
    lastModified: new Date().toISOString(),
    version: '3.0'
  }));
}

function restoreFromLocalStorage() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return;
  const { data } = JSON.parse(raw);
  Object.entries(data).forEach(([field, value]) => {
    document.querySelectorAll(`[data-field="${field}"]`).forEach(el => {
      if (el.textContent !== value) {
        el.textContent = value;
        markAsModified(el);
      }
    });
  });
}

window.addEventListener('DOMContentLoaded', restoreFromLocalStorage);
```

### Camada 4 — Indicador visual de edição

Campos modificados recebem uma classe `.modified` que aplica borda lateral laranja
(`#e67e22`) e tooltip "Modificado em [timestamp]".

```css
.editable {
  border-bottom: 1px dashed transparent;
  transition: all 200ms;
}
.editable:hover {
  border-bottom-color: #2dd4bf;
  background: rgba(45, 212, 191, 0.05);
}
.editable:focus {
  outline: 2px solid #e67e22;
  outline-offset: 2px;
  background: rgba(230, 126, 34, 0.05);
}
.editable.modified {
  border-left: 3px solid #e67e22;
  padding-left: 6px;
  position: relative;
}
.editable.modified::before {
  content: "●";
  color: #e67e22;
  position: absolute;
  left: -14px;
  font-size: 10px;
}
```

### Camada 5 — Menu de contexto em tabelas

Clique-direito em qualquer linha de tabela abre menu com:

- **Duplicar linha** — copia a linha clicada e insere logo abaixo
- **Remover linha** — remove com confirmação
- **Mover para cima / baixo** — reordena
- **Limpar campo** — zera o valor e remove marca `.modified`

```javascript
document.querySelectorAll('table.editable-table tr').forEach(row => {
  row.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    showContextMenu(e.pageX, e.pageY, row);
  });
});
```

### Camada 6 — Exportação CSV / JSON dinâmica

Botão flutuante no canto inferior direito abre menu de exportação:

- **📊 CSV** — baixa tabelas atuais (PAE, Matriz AIHA, Checklist) em CSV separados
- **📦 JSON** — baixa snapshot completo do documento (todos os campos editáveis)
- **📄 HTML atualizado** — baixa nova versão do HTML com os valores editados já embutidos
- **🖨️ Imprimir/PDF** — envia para `window.print()`

```javascript
function exportToCSV(tableId) {
  const rows = [];
  document.querySelectorAll(`#${tableId} tr`).forEach(tr => {
    const cells = Array.from(tr.querySelectorAll('th, td'))
      .map(c => `"${c.textContent.trim().replace(/"/g, '""')}"`);
    rows.push(cells.join(','));
  });
  const blob = new Blob([rows.join('\n')], { type: 'text/csv;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `${tableId}-${Date.now()}.csv`;
  a.click();
}

function exportToJSON() {
  const snapshot = {};
  document.querySelectorAll('.editable[data-field]').forEach(el => {
    snapshot[el.dataset.field] = el.textContent;
  });
  const blob = new Blob([JSON.stringify(snapshot, null, 2)],
    { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `aet-snapshot-${Date.now()}.json`;
  a.click();
}
```

---

## UI — Barra de controle flutuante

Barra fixa no topo do documento com 5 botões:

```html
<div class="edit-toolbar">
  <button data-action="toggle-edit" title="Alternar modo de edição (Ctrl+E)">
    ✏️ Editar
  </button>
  <button data-action="save" title="Salvar alterações">
    💾 Salvar
  </button>
  <button data-action="reset" title="Reverter para original">
    ↺ Resetar
  </button>
  <button data-action="export" title="Exportar">
    📤 Exportar
  </button>
  <button data-action="print" title="Imprimir / PDF (Ctrl+P)">
    🖨️ PDF
  </button>
</div>
```

### Atalhos de teclado obrigatórios

| Atalho | Ação |
|---|---|
| `Ctrl+E` | Alternar modo de edição |
| `Ctrl+S` | Salvar snapshot |
| `Ctrl+P` | Imprimir / PDF |
| `Ctrl+Z` (nativo) | Desfazer última edição no campo ativo |
| `/` | Abrir glossário (se presente) |
| `Esc` | Sair do modo de edição |

---

## Comportamento especial por seção

### Seção 3.4 (Caracterização) ↔ Seção 3.7 (NR-17)

Campos espelhados automaticamente:

| Campo | `data-field` | Onde aparece |
|---|---|---|
| Nome da empresa | `empresa.nome` | Capa, 3.2, 3.4 |
| CNPJ | `empresa.cnpj` | 3.2, 3.4 |
| Setor | `setor.nome` | 3.2, 3.4, 3.7 |
| Função/CBO | `funcao.nome` + `funcao.cbo` | 3.2, 3.4, 3.5 |
| Nº de trabalhadores | `posto.n_trabalhadores` | 3.4, 3.7 |
| Jornada | `posto.jornada` | 3.4, 3.7.6 |
| Pausas | `posto.pausas` | 3.4, 3.7.6 |
| Queixas relatadas | `posto.queixas` | 3.4, 3.10 |

### Tabela PAE (Seção 3.9)

- **Colunas editáveis:** Risco, Medida, Tipo, Responsável, Prazo, Custo, Indicador
- **Coluna calculada:** ID do PAE (`PAE-01`, `PAE-02`, ...) — recalcula automaticamente quando linhas são adicionadas/removidas
- **Validação visual:** se Nível de Risco for Alto/Crítico e PAE não tiver medida de Engenharia ou Eliminação, marcar célula em vermelho

---

## Regras obrigatórias de implementação

1. **Todo campo editável TEM `data-field`** (para sync e export)
2. **Campos críticos (empresa, RT, CNPJ) NÃO são editáveis por padrão** — requerem clique no cadeado 🔒 para destravar
3. **Scores RULA/REBA permitem sobrescrita manual** mas mantêm badge "estimativa" até usuário confirmar com click em "✓ Validado"
4. **Nunca perder dados** — `beforeunload` alerta se houver edições não salvas
5. **Sempre manter cópia do original** em `data-original` para permitir reset individual
6. **Todos os ícones de status** (🔴🟠🟡🟢 ✅❌⚠️) são atualizados automaticamente quando scores mudam

---

## Tipografia premium — OBRIGATÓRIA

> **ATENÇÃO — REGRA REFORÇADA NO PATCH v3.1.1**
>
> A identidade visual LBM BORATTI exige as fontes **DM Serif Display**, **DM Sans**
> e **JetBrains Mono**. Estas fontes **DEVEM** aparecer em todo HTML gerado, sem exceção.
>
> O princípio "self-contained" (sem CDN) aplica-se a **lógica JavaScript e dados**
> (scripts, bases, estilos próprios). **Não se estende a fontes web**: é aceitável e
> obrigatório carregar fontes do Google Fonts via `@import` ou `<link>`. Fontes de
> sistema (Segoe UI, San Francisco, Arial) **não são aceitáveis** para o visual premium.

### Implementação obrigatória — escolher UMA das 3 estratégias abaixo

**Estratégia A (padrão recomendado):** `<link rel="preconnect">` + `<link rel="stylesheet">` no `<head>`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Estratégia B:** `@import` dentro do próprio `<style>`

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
  /* ... resto do CSS ... */
</style>
```

**Estratégia C (offline 100%):** `@font-face` com base64 das 3 fontes embutidas
Usar apenas quando cliente exigir que HTML funcione **sem qualquer conexão** durante
a leitura (ex: auditoria em planta industrial sem wifi). Mais pesado (~350 KB extra),
mas totalmente offline.

### Aplicação no CSS

```css
:root {
  --font-display: 'DM Serif Display', Georgia, serif;
  --font-body: 'DM Sans', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
}

body { font-family: var(--font-body); }
h1, h2, .capa-titulo, .cliente-nome { font-family: var(--font-display); }
code, pre, .meta-valor, .score { font-family: var(--font-mono); }
```

### Fallback aceitável (só em modo de emergência)

Se por algum motivo as fontes Google não puderem ser carregadas (rede bloqueada,
prompt muito curto), **o HTML DEVE declarar os fallbacks de forma explícita** no
CSS (Georgia/serif, sans-serif, monospace) — **nunca** deixar só `Segoe UI`, que é
fonte de sistema Windows e quebra a identidade em Mac/Linux.

---

## Logo LBM BORATTI — EMBEDDING OBRIGATÓRIO

> **REGRA REFORÇADA NO PATCH v3.1.1**
>
> O logo LBM BORATTI **DEVE** aparecer visualmente em todo HTML gerado. O texto
> "LBM BORATTI" em tipo não substitui o logo — é elemento de identidade visual.

### Implementação obrigatória

Ler `assets/logo-base64.txt` e embutir o data URI em **pelo menos 2 pontos**:

1. **Capa** (obrigatório) — dentro do `.capa-header` acima do título
2. **Header fixo de navegação** (recomendado) — versão reduzida no topo durante scroll

```html
<!-- Capa -->
<div class="logo-lbm logo-capa">
  <img src="<data URI lido de assets/logo-base64.txt>"
       alt="LBM BORATTI Consultoria Personalizada em Segurança e Saúde no Trabalho"
       width="280" height="84" />
</div>

<!-- Header fixo -->
<div class="logo-lbm logo-header">
  <img src="<mesmo data URI>"
       alt="LBM BORATTI"
       width="120" height="36" />
</div>
```

**Alternativa válida:** usar `assets/logo-base64-all.txt` para obter as **3 versões otimizadas**
do logo oficial (FULL para capa, HEADER para topbar fixo, SIG para assinatura/rodapé) — cada
uma já redimensionada e comprimida em JPEG para peso mínimo no HTML final.

### Checklist visual do logo

- [ ] Logo aparece na capa (sempre)
- [ ] Logo aparece no header fixo durante scroll (recomendado)
- [ ] Logo é impresso em PDF (não `display:none` no `@media print`)
- [ ] Tamanho mínimo na capa: 240px largura
- [ ] Contraste adequado (fundo navy → logo em branco/claro; fundo claro → logo em navy)

---

## Regras obrigatórias de implementação (checklist consolidado)

1. **Todo campo editável TEM `data-field`** (para sync e export)
2. **Campos críticos (empresa, RT, CNPJ) NÃO são editáveis por padrão** — requerem clique no cadeado 🔒 para destravar
3. **Scores RULA/REBA permitem sobrescrita manual** mas mantêm badge "estimativa" até usuário confirmar com click em "✓ Validado"
4. **Nunca perder dados** — `beforeunload` alerta se houver edições não salvas
5. **Sempre manter cópia do original** em `data-original` para permitir reset individual
6. **Todos os ícones de status** (🔴🟠🟡🟢 ✅❌⚠️) são atualizados automaticamente quando scores mudam
7. **[v3.1.1] Fontes DM Serif Display + DM Sans + JetBrains Mono** são obrigatórias (via Google Fonts ou @font-face base64)
8. **[v3.1.1] Logo LBM** (data URI ou SVG inline) é obrigatório na capa

---

## Versão e compatibilidade

- **Versão:** 3.1.1 (FULL EDIT ENGINE + fontes obrigatórias + logo obrigatório)
- **Navegadores:** Chrome/Edge/Firefox/Safari recentes (ES6+)
- **Modo "sem rede":** Scripts, lógica e dados são 100% offline. Fontes Google Fonts
  requerem rede na primeira carga (depois são cacheadas). Para modo totalmente offline,
  usar Estratégia C (fontes embutidas em base64).
- **Mobile:** Funcional, mas edição é otimizada para desktop
- **Impressão:** Modo de edição é automaticamente desativado; badges `.modified` permanecem visíveis como indicador de audit trail; logo e fontes são impressos via `print-color-adjust: exact`
