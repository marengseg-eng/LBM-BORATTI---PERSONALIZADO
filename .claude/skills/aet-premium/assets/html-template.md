# Template HTML Premium — AET LBM BORATTI

## Padrão Visual

### Cores
```css
--azul-marinho: #1a2f4e;
--azul-medio: #2c5282;
--laranja: #e67e22;
--laranja-claro: #f39c12;
--cinza-claro: #f8f9fa;
--cinza-medio: #e9ecef;
--branco: #ffffff;
--texto-escuro: #2d3748;
--verde-risco: #27ae60;
--amarelo-risco: #f39c12;
--laranja-risco: #e67e22;
--vermelho-risco: #e74c3c;
```

### Estrutura HTML Base
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AET — [EMPRESA] — LBM BORATTI</title>

    <!-- ⚠ v3.1.1: Fontes Google OBRIGATÓRIAS (ou @font-face base64 se offline total) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

    <style>
        /* Reset e Base */
        * { margin: 0; padding: 0; box-sizing: border-box; }

        :root {
            --font-display: 'DM Serif Display', Georgia, 'Times New Roman', serif;
            --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace;
        }

        body {
            font-family: var(--font-body);
            font-size: 14px;
            color: #2d3748;
            background: #f8f9fa;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* Títulos e elementos de identidade usam DM Serif Display */
        h1, h2, h3, .capa h1, .capa h2, .cliente-nome, .secao-header h3,
        .assinatura .nome {
            font-family: var(--font-display);
            font-weight: 400;
            letter-spacing: -0.01em;
        }

        /* Números técnicos, códigos e scores em JetBrains Mono */
        .score-box .numero, code, pre, .doc-info p,
        .meta-valor, .numero-pae { font-family: var(--font-mono); }

        /* Container Principal */
        .container {
            max-width: 1100px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
        }

        /* CAPA */
        .capa {
            background: linear-gradient(135deg, #1a2f4e 0%, #2c5282 100%);
            color: white;
            padding: 60px 50px;
            text-align: center;
            position: relative;
        }

        /* ⚠ v3.1.1: Logo LBM — imagem embutida OBRIGATÓRIA (não apenas texto) */
        .logo-lbm {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
        }
        .logo-lbm img {
            max-width: 280px;
            height: auto;
            filter: drop-shadow(0 2px 8px rgba(0,0,0,0.25));
        }
        .logo-lbm.logo-header img { max-width: 120px; }
        .capa::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 6px;
            background: linear-gradient(90deg, #e67e22, #f39c12);
        }
        .capa .logo-area {
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 3px;
            opacity: 0.8;
            margin-bottom: 12px;
            font-family: var(--font-body);
            font-weight: 500;
        }
        .capa h1 {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .capa h2 {
            font-size: 20px;
            font-weight: 400;
            opacity: 0.9;
            margin-bottom: 40px;
        }
        .capa .doc-info {
            background: rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 20px;
            display: inline-block;
            text-align: left;
            min-width: 350px;
        }
        .capa .doc-info p { margin: 5px 0; font-size: 13px; }
        .capa .doc-info span { opacity: 0.7; }

        /* CABEÇALHO de Seção */
        .secao-header {
            background: #1a2f4e;
            color: white;
            padding: 15px 30px;
            margin: 30px 0 0 0;
            border-left: 5px solid #e67e22;
        }
        .secao-header h3 { font-size: 16px; text-transform: uppercase; letter-spacing: 1px; }

        /* Conteúdo */
        .secao-body {
            padding: 25px 30px;
            border-left: 1px solid #e9ecef;
            border-right: 1px solid #e9ecef;
        }

        /* Tabelas */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 13px;
        }
        thead tr {
            background: #1a2f4e;
            color: white;
        }
        thead th {
            padding: 10px 12px;
            text-align: left;
            font-weight: 600;
        }
        tbody tr:nth-child(even) { background: #f8f9fa; }
        tbody tr:hover { background: #e8f4f8; }
        tbody td { padding: 9px 12px; border-bottom: 1px solid #e9ecef; }

        /* Badges de Risco */
        .risco-badge {
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            display: inline-block;
        }
        .risco-baixo { background: #d4edda; color: #155724; }
        .risco-medio { background: #fff3cd; color: #856404; }
        .risco-alto { background: #ffe0b2; color: #e65100; }
        .risco-critico { background: #f8d7da; color: #721c24; }

        /* Score Box */
        .score-box {
            background: #1a2f4e;
            color: white;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            display: inline-block;
            min-width: 120px;
            margin: 10px;
        }
        .score-box .numero { font-size: 36px; font-weight: 700; color: #f39c12; }
        .score-box .label { font-size: 11px; text-transform: uppercase; opacity: 0.8; }

        /* PAE Card */
        .pae-card {
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 15px 20px;
            margin: 10px 0;
            border-left: 4px solid #e67e22;
        }
        .pae-card .pae-titulo { font-weight: 700; color: #1a2f4e; margin-bottom: 8px; }
        .pae-card .pae-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px; }
        .pae-card .pae-item span { font-weight: 600; color: #2c5282; }

        /* Assinatura */
        .assinatura {
            border-top: 3px solid #1a2f4e;
            padding: 30px;
            text-align: center;
            background: #f8f9fa;
        }
        .assinatura .linha { width: 300px; border-top: 1px solid #2d3748; margin: 20px auto 5px; }
        .assinatura .nome { font-weight: 700; font-size: 16px; color: #1a2f4e; }
        .assinatura .registro { font-size: 12px; color: #666; }

        /* Botão Imprimir */
        .btn-print {
            position: fixed;
            bottom: 30px; right: 30px;
            background: #e67e22;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(230,126,34,0.4);
            transition: all 0.2s;
        }
        .btn-print:hover { background: #d35400; transform: translateY(-2px); }

        @media print {
            .btn-print { display: none; }
            body { background: white; }
            .container { box-shadow: none; }
        }
    </style>
</head>
<body>
<div class="container">

    <!-- CAPA — ⚠ v3.1.1: logo em <img> (data URI lido de assets/logo-base64.txt) é OBRIGATÓRIO -->
    <div class="capa">
        <!-- Logo LBM — embutido como data URI (ler conteúdo de assets/logo-base64.txt e colar aqui) -->
        <div class="logo-lbm">
            <img src="[LOGO_DATA_URI_de_assets/logo-base64.txt]"
                 alt="LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho"
                 width="280" height="84" />
        </div>
        <div class="logo-area">Consultoria Personalizada em Segurança e Saúde no Trabalho</div>
        <h1>ANÁLISE ERGONÔMICA DO TRABALHO</h1>
        <h2>[FUNÇÃO/CARGO] — [EMPRESA]</h2>
        <div class="doc-info">
            <p><span>Documento:</span> AET-[CLIENTE]-[ANO]-[SEQ]</p>
            <p><span>Empresa:</span> [NOME DA EMPRESA]</p>
            <p><span>Setor:</span> [SETOR]</p>
            <p><span>Data:</span> [DATA]</p>
            <p><span>Revisão:</span> 00</p>
        </div>
    </div>

    <!-- SEÇÕES DO RELATÓRIO AQUI -->
    <!-- ... -->

    <!-- ASSINATURA -->
    <div class="assinatura">
        <div class="linha"></div>
        <div class="nome">Marcelo Luis Boratti Melo</div>
        <div class="registro">Engenheiro de Segurança do Trabalho — CREA-SP: 5069572947</div>
        <div class="registro">Fisioterapeuta e Ergonomista — CREFITO 3/209468-F</div>
        <div class="registro" style="margin-top:5px;color:#1a2f4e;font-weight:600;">
            LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
        </div>
    </div>

</div>

<button class="btn-print" onclick="window.print()">🖨️ Imprimir / PDF</button>

</body>
</html>
```

## Instruções de Uso do Template

1. Substituir todos os `[CAMPOS]` com dados reais
2. Adicionar seções usando o padrão `.secao-header` + `.secao-body`
3. Usar `.risco-badge` com classe adequada para cada nível
4. Usar `.score-box` para exibir scores das metodologias
5. Usar `.pae-card` para cada ação do PAE
6. O botão de impressão gera PDF via browser nativamente

---

## ⚠ Checklist OBRIGATÓRIO v3.1.1 — antes de entregar o HTML

### Fontes
- [ ] `<link>` para Google Fonts presente no `<head>` com **DM Serif Display + DM Sans + JetBrains Mono**
- [ ] CSS usa `var(--font-display)`, `var(--font-body)`, `var(--font-mono)` (não `'Segoe UI'`)
- [ ] Títulos (`h1`, `h2`, capa) usam DM Serif Display
- [ ] Texto corrido usa DM Sans
- [ ] Códigos, scores e números técnicos usam JetBrains Mono

### Logo LBM
- [ ] **Ler o conteúdo completo de `assets/logo-base64.txt`** (via `view` tool)
- [ ] Colar o data URI dentro do atributo `src` do `<img>` na capa
- [ ] **NÃO deixar o placeholder** `[LOGO_DATA_URI_de_assets/logo-base64.txt]` no HTML final
- [ ] (Recomendado) Repetir o logo, menor, no header fixo durante scroll
- [ ] Logo visível também em modo dark e na impressão

### Exemplo de como substituir o placeholder corretamente

```
# O arquivo assets/logo-base64.txt contém:
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciLi4u

# No HTML final, substituir:
<img src="[LOGO_DATA_URI_de_assets/logo-base64.txt]" .../>

# Por:
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0i..." .../>
```

### Se o logo não caber no prompt (muito grande)

Alternativa aceita: usar `assets/logo-base64-all.txt` que contém **3 versões** do logo
oficial (FULL 34 KB / HEADER 10 KB / SIG 19 KB) separadas por marcadores
`=== LOGO_FULL ===`, `=== LOGO_HEADER ===`, `=== LOGO_SIG ===`. Extrair apenas a versão
necessária para cada ponto do HTML.


---

## 🆕 v3.1.3 — Responsividade Mobile + 3 novos botões

### CSS obrigatório (adicionar ANTES do `@media print`)

```css
/* ============ v3.1.3 — RESPONSIVIDADE COMPLETA ============ */

/* Hamburger (mobile) — escondido em desktop */
.btn-hamburger {
  display:none; background:transparent; border:1px solid var(--cinza-1);
  border-radius:6px; padding:6px 10px; cursor:pointer; font-size:18px;
  color:var(--txt); line-height:1;
}
.btn-hamburger:hover { background:var(--navy); color:#fff; border-color:var(--navy); }

/* Drawer lateral (mobile) */
.nav-drawer {
  position:fixed; top:0; left:-320px; width:300px; height:100vh;
  background:var(--card); box-shadow:4px 0 20px rgba(0,0,0,0.15);
  z-index:1500; transition:left 0.3s ease; padding:20px 16px;
  overflow-y:auto;
}
.nav-drawer.open { left:0; }
.nav-drawer-header {
  display:flex; align-items:center; justify-content:space-between;
  padding-bottom:14px; margin-bottom:14px; border-bottom:1px solid var(--cinza-1);
}
.nav-drawer-header img { height:30px; }
.nav-drawer-close {
  background:transparent; border:none; font-size:22px; cursor:pointer;
  color:var(--txt); line-height:1;
}
.nav-drawer-links { display:flex; flex-direction:column; gap:2px; }
.nav-drawer-links a {
  padding:12px 14px; border-radius:8px; color:var(--txt-soft);
  text-decoration:none; font-size:14px; transition:all 0.15s;
  display:flex; align-items:center; gap:10px;
}
.nav-drawer-links a:hover, .nav-drawer-links a.active {
  background:var(--navy); color:#fff;
}
.nav-drawer-links a .num {
  font-family:var(--font-mono); font-size:11px; opacity:0.7; min-width:32px;
}

/* Overlay escuro atrás do drawer */
.drawer-overlay {
  position:fixed; inset:0; background:rgba(0,0,0,0.4); z-index:1400;
  opacity:0; pointer-events:none; transition:opacity 0.25s;
}
.drawer-overlay.show { opacity:1; pointer-events:auto; }

/* Back-to-top */
.btn-back-top {
  position:fixed; bottom:30px; left:30px; z-index:500;
  background:var(--navy); color:#fff; border:none;
  width:46px; height:46px; border-radius:50%; cursor:pointer;
  font-size:18px; box-shadow:0 4px 14px rgba(26,47,78,0.35);
  opacity:0; transform:translateY(20px); pointer-events:none;
  transition:all 0.3s;
}
.btn-back-top.show { opacity:1; transform:translateY(0); pointer-events:auto; }
.btn-back-top:hover { background:var(--navy-3); transform:translateY(-3px); }

/* Botão adicionar linha (+) em tabelas editáveis */
.add-row-wrap { text-align:right; margin-top:-10px; margin-bottom:12px; }
.btn-add-row {
  background:transparent; border:1px dashed var(--teal); color:var(--teal);
  padding:8px 14px; border-radius:6px; cursor:pointer; font-size:12px;
  font-family:var(--font-body); font-weight:500; transition:all 0.15s;
  display:inline-flex; align-items:center; gap:6px;
}
.btn-add-row:hover {
  background:var(--teal); color:#fff; border-style:solid;
}

/* Badge pulsante de "não salvo" no botão Salvar */
#btn-save.unsaved {
  background:var(--laranja) !important; color:#fff !important;
  border-color:var(--laranja) !important;
  animation:pulse-save 1.8s ease-in-out infinite;
}
@keyframes pulse-save {
  0%, 100% { box-shadow:0 0 0 0 rgba(230,126,34,0.5); }
  50% { box-shadow:0 0 0 6px rgba(230,126,34,0); }
}

/* Indicador de modo edição ativo na topbar */
body.editing #btn-edit {
  background:var(--laranja); color:#fff; border-color:var(--laranja);
}
body.editing::before {
  content:"✏️ Modo edição ativo — Esc para sair"; position:fixed;
  top:56px; right:20px; background:var(--laranja); color:#fff;
  padding:4px 12px; border-radius:12px; font-size:11px;
  font-weight:600; z-index:200; box-shadow:0 2px 8px rgba(230,126,34,0.35);
}

/* ============ BREAKPOINT TABLET — 900px ============ */
@media (max-width:900px) {
  .topbar .topbar-nav { display:none; }          /* esconde nav linear */
  .btn-hamburger { display:inline-block; }       /* mostra hamburger */
  .secao { padding:30px 28px; }
  .capa { padding:40px 30px 50px; }
  .capa h1.capa-titulo { font-size:clamp(26px, 5vw, 36px); }
  .cliente-nome { font-size:clamp(22px, 4vw, 30px); letter-spacing:0.08em; }
  .meta-grid { grid-template-columns:repeat(2, 1fr); }
  .scores-wrap { grid-template-columns:repeat(2, 1fr); }
  .pae-grid { grid-template-columns:1fr; }
  .hierarquia { grid-template-columns:repeat(3, 1fr); }
  .hierarquia .hier-item:nth-child(n+4) { grid-column:span 1; }
  /* Tabelas ganham scroll horizontal */
  .secao table {
    display:block; overflow-x:auto; white-space:nowrap;
    -webkit-overflow-scrolling:touch;
  }
  .secao table tbody td { white-space:normal; min-width:160px; }
}

/* ============ BREAKPOINT MOBILE — 560px ============ */
@media (max-width:560px) {
  body { font-size:13px; }
  .topbar { padding:8px 14px; gap:8px; }
  .topbar .logo-header img { height:28px; }
  .topbar-actions button { padding:5px 8px; font-size:11px; }
  .topbar-actions button#btn-save,
  .topbar-actions button#btn-reset { display:none; } /* migram pro FAB stack */
  .secao { padding:24px 18px; }
  .secao-header h3 { font-size:20px; }
  .capa { padding:30px 18px 40px; }
  .logo-lbm img { max-width:100%; }
  .capa h1.capa-titulo { font-size:clamp(22px, 6.5vw, 30px); line-height:1.15; }
  .capa-subtitulo { font-size:13px; }
  .cliente-nome { font-size:clamp(18px, 6vw, 26px); letter-spacing:0.06em; }
  .meta-grid { grid-template-columns:1fr; gap:10px; }
  .meta-item { padding:10px 12px; }
  .scores-wrap { grid-template-columns:1fr; }
  .score-box { padding:14px; }
  .score-box .score-num { font-size:32px; }
  .hierarquia { grid-template-columns:repeat(2, 1fr); }
  .pae-card { padding:14px 16px; }
  .pae-card .pae-titulo { font-size:13.5px; flex-wrap:wrap; }
  .fab-wrap { bottom:18px; right:14px; }
  .fab { width:46px; height:46px; font-size:17px; }
  .btn-back-top { bottom:18px; left:14px; width:40px; height:40px; font-size:15px; }
  .nav-drawer { width:85vw; left:-90vw; }
  .nav-drawer.open { left:0; }
  /* Assinatura compacta */
  .assinatura { padding:30px 18px; }
  .assinatura .linha { width:80%; }
  /* Capa-credenciais menor */
  .capa-credenciais { font-size:11px; }
  /* Progress bar mais fina */
  .progress-bar { height:2px; }
  /* Toast em mobile */
  .toast { bottom:80px; font-size:12px; padding:10px 16px; }
}

/* ============ BREAKPOINT MICRO — 380px (iPhone SE e similares) ============ */
@media (max-width:380px) {
  .topbar { padding:6px 10px; }
  .topbar-actions button#btn-edit span { display:none; } /* só ícone */
  .secao { padding:20px 14px; }
  .capa { padding:24px 14px 36px; }
  .meta-label { font-size:9px; letter-spacing:0.12em; }
  .meta-valor { font-size:12.5px; }
  .hierarquia .hier-item { font-size:10px; padding:8px 4px; }
}

/* ============ PREFERÊNCIAS DO USUÁRIO ============ */
@media (prefers-reduced-motion:reduce) {
  *, *::before, *::after { animation:none !important; transition:none !important; }
```

### HTML — elementos novos

```html
<!-- v3.1.3: Hamburger (aparece só em mobile via CSS) -->
<!-- Adicionar DENTRO de <nav class="topbar"> como PRIMEIRO filho -->
<button class="btn-hamburger" id="btn-hamburger" title="Menu de seções" aria-label="Abrir menu">☰</button>

<!-- v3.1.3: Ajustar botão Editar para ter span interno (rótulo some em <380px) -->
<button id="btn-edit" title="Alternar edição (Ctrl+E)"><span>✏️</span> <span class="btn-label">Editar</span></button>

<!-- v3.1.3: Drawer lateral + overlay (adicionar LOGO APÓS </nav>) -->
<aside class="nav-drawer" id="nav-drawer" aria-hidden="true">
  <div class="nav-drawer-header">
    <img src="[LOGO_DATA_URI_header]" alt="LBM BORATTI"/>
    <button class="nav-drawer-close" id="drawer-close" aria-label="Fechar menu">×</button>
  </div>
  <div class="nav-drawer-links">
    <a href="#s31"><span class="num">3.1</span>Capa</a>
    <a href="#s32"><span class="num">3.2</span>Identificação</a>
    <a href="#s33"><span class="num">3.3</span>Objetivo e Escopo</a>
    <a href="#s34"><span class="num">3.4</span>Caracterização</a>
    <a href="#s35"><span class="num">3.5</span>Biomecânica</a>
    <a href="#s36"><span class="num">3.6</span>Cognitiva/Psicossocial</a>
    <a href="#s37"><span class="num">3.7</span>Checklist NR-17</a>
    <a href="#s38"><span class="num">3.8</span>Matriz AIHA</a>
    <a href="#s39"><span class="num">3.9</span>PAE</a>
    <a href="#s310"><span class="num">3.10</span>Conclusão</a>
    <a href="#s311"><span class="num">3.11</span>Referências</a>
    <a href="#s312"><span class="num">3.12</span>Glossário</a>
    <a href="#s313"><span class="num">3.13</span>Assinatura</a>
  </div>
</aside>
<div class="drawer-overlay" id="drawer-overlay"></div>

<!-- v3.1.3: Botão "Voltar ao topo" (aparece após scroll >500px) -->
<button class="btn-back-top" id="btn-back-top" title="Voltar ao topo" aria-label="Voltar ao topo">⬆</button>

<!-- v3.1.3: Botão "Adicionar linha" (colocar APÓS cada tabela editável) -->
<div class="add-row-wrap">
  <button class="btn-add-row" data-target="tbl-aiha" title="Adicionar linha à Matriz AIHA">
    ➕ Adicionar fator de risco
  </button>
</div>
```

### JavaScript — adicionar ANTES da chamada `restoreSnapshot();`

```javascript
/* ============ v3.1.3 — 3 NOVOS CONTROLES ============ */

/* --- Hamburger + Drawer lateral (mobile) --- */
const drawer = document.getElementById('nav-drawer');
const drawerOverlay = document.getElementById('drawer-overlay');
const btnHamburger = document.getElementById('btn-hamburger');
const drawerClose = document.getElementById('drawer-close');

function openDrawer() {
  drawer.classList.add('open');
  drawerOverlay.classList.add('show');
  drawer.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}
function closeDrawer() {
  drawer.classList.remove('open');
  drawerOverlay.classList.remove('show');
  drawer.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

btnHamburger.addEventListener('click', openDrawer);
drawerClose.addEventListener('click', closeDrawer);
drawerOverlay.addEventListener('click', closeDrawer);

/* Fechar drawer ao clicar em qualquer link */
document.querySelectorAll('.nav-drawer-links a').forEach(a => {
  a.addEventListener('click', () => setTimeout(closeDrawer, 120));
});

/* Escape também fecha drawer */
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && drawer.classList.contains('open')) closeDrawer();
});

/* Sincronizar link ativo do drawer com IntersectionObserver */
const drawerLinks = document.querySelectorAll('.nav-drawer-links a');
const obsDrawer = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      const id = en.target.id;
      drawerLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + id));
    }
  });
}, { rootMargin: '-40% 0px -50% 0px' });
sections.forEach(s => obsDrawer.observe(s));

/* --- Back-to-top --- */
const btnBackTop = document.getElementById('btn-back-top');
let lastScrollCheck = 0;
window.addEventListener('scroll', () => {
  const now = performance.now();
  if (now - lastScrollCheck < 100) return;
  lastScrollCheck = now;
  btnBackTop.classList.toggle('show', window.scrollY > 500);
});
btnBackTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

/* --- Botão "Adicionar linha" em tabelas editáveis --- */
document.querySelectorAll('.btn-add-row').forEach(btn => {
  btn.addEventListener('click', () => {
    const tableId = btn.dataset.target;
    const tbody = document.querySelector(`#${tableId} tbody`);
    if (!tbody) return;
    const lastRow = tbody.querySelector('tr:last-child');
    if (!lastRow) return;
    // Clonar última linha
    const newRow = lastRow.cloneNode(true);
    // Limpar conteúdo mas manter estrutura
    newRow.querySelectorAll('td').forEach((td, idx) => {
      if (idx === 0) {
        // Primeira coluna = ID R-XX — auto-incrementar
        const match = lastRow.querySelector('td').textContent.match(/R-(\d+)/);
        td.textContent = match ? `R-${String(parseInt(match[1]) + 1).padStart(2, '0')}` : 'R-XX';
      } else if (td.querySelector('.badge')) {
        // Preservar badge mas zerar texto ao redor
        const badge = td.querySelector('.badge').outerHTML;
        td.innerHTML = badge;
      } else {
        td.textContent = '—';
      }
      td.setAttribute('contenteditable', 'true');
    });
    tbody.appendChild(newRow);
    // Scroll até a nova linha
    newRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
    newRow.querySelector('td:nth-child(2)').focus();
    toast('➕ Linha adicionada — edite os campos');
    markUnsaved();
  });
});

/* --- Badge pulsante de "não salvo" --- */
const btnSave = document.getElementById('btn-save');
function markUnsaved() {
  btnSave.classList.add('unsaved');
  btnSave.title = '⚠ Edições não salvas — clique para salvar (Ctrl+S)';
}
function markSaved() {
  btnSave.classList.remove('unsaved');
  btnSave.title = 'Salvar (Ctrl+S)';
}

/* Detectar qualquer edição e marcar como "não salvo" */
document.addEventListener('input', (e) => {
  if (e.target.isContentEditable || e.target.hasAttribute('contenteditable')) {
    markUnsaved();
  }
});

/* Atualizar markSaved após salvamento */
const originalSaveSnapshot = saveSnapshot;
saveSnapshot = function() {
  originalSaveSnapshot.apply(this, arguments);
  markSaved();
};

/* --- Detecção de viewport para ajustes JS --- */
function isMobile() { return window.matchMedia('(max-width:900px)').matches; }

/* Em mobile, botões Save/Reset migram visualmente pra não poluir */
/* Já tratado via CSS; aqui só emitimos info */
if (isMobile()) console.info('📱 Modo mobile detectado — hamburger ativo');

/* Fechar drawer se resize passar pra desktop */
window.addEventListener('resize', () => {
  if (!isMobile() && drawer.classList.contains('open')) closeDrawer();
});

/* --- Swipe para abrir/fechar drawer (touch) --- */
let touchStartX = 0;
document.addEventListener('touchstart', (e) => {
  touchStartX = e.touches[0].clientX;
}, { passive: true });

document.addEventListener('touchend', (e) => {
  if (!isMobile()) return;
  const touchEndX = e.changedTouches[0].clientX;
  const diff = touchEndX - touchStartX;
  // Swipe right da borda esquerda abre drawer
  if (touchStartX < 30 && diff > 80 && !drawer.classList.contains('open')) openDrawer();
  // Swipe left fecha drawer
  if (drawer.classList.contains('open') && diff < -80) closeDrawer();
}, { passive: true });

restoreSnapshot();
```

### Breakpoints

| Largura | Comportamento |
|---|---|
| **≥ 901 px** (desktop) | Layout completo · nav horizontal com 12 seções |
| **561–900 px** (tablet) | Hamburger ativo · meta-grid 2 colunas · tabelas com scroll horizontal |
| **381–560 px** (mobile) | Tudo 1 coluna · botões Save/Reset escondidos (acessíveis via atalho ou modo edição) · FAB redimensionado |
| **≤ 380 px** (micro) | Rótulo "Editar" vira ícone · paddings reduzidos |

### Acessibilidade incluída

- `prefers-reduced-motion` desativa animações para usuários com sensibilidade
- `aria-hidden` no drawer sincronizado com estado
- `aria-label` em todos os botões de ícone
- Foco visível em campos editáveis
- Swipe gestures não substituem botões (apenas complementam)

### Checklist obrigatório v3.1.3

- [ ] Hamburger `.btn-hamburger` dentro de `.topbar` como primeiro filho
- [ ] `<aside class="nav-drawer">` após `</nav>` da topbar
- [ ] `<div class="drawer-overlay">` após o `</aside>`
- [ ] `<button class="btn-back-top">` após o drawer-overlay
- [ ] Botão `.btn-add-row` colocado após cada tabela editável com `data-target="id-da-tabela"`
- [ ] CSS responsivo (@media 900, 560, 380) antes do @media print
- [ ] JavaScript v3.1.3 adicionado antes de `restoreSnapshot();`
- [ ] Ícone ☰ visível em telas <900px · invisível em desktop
- [ ] Ícone ⬆ aparece após scroll >500px
- [ ] Badge laranja pulsante em 💾 quando há edições não salvas
