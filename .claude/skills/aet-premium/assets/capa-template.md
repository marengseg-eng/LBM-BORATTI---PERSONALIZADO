# CAPA PROFISSIONAL — Padrão LBM BORATTI

Padrão visual da **Seção 3.1 — Capa** de todas as AETs. Baseado no modelo canônico `AET-ELETROSERT-2025-001`.

---

## ⚠ LOGO OFICIAL LBM BORATTI — uso obrigatório

O logo oficial é um **JPEG panorâmico** (proporção ~3:1) com:
- Fundo navy em gradiente `#1a2f4e`
- Símbolo à esquerda: engrenagem estilizada com dois elementos de solda/ferramentas (azul claro)
- Texto "LBM" em branco (tipografia sans-serif bold, pesada)
- Texto "BORATTI" abaixo em azul claro (`#7dc4ff`)
- Linha horizontal laranja de destaque (`#e67e22`) separando o slogan
- Slogan: "Consultoria Personalizada em Segurança e Saúde no Trabalho"

**Arquivo de origem:** `assets/logo-original.png` (4400×1440 px, ~288 KB — **NÃO usar direto no HTML**)

**Arquivos prontos para uso (data URIs JPEG otimizados):**

| Arquivo | Versão | Dimensão | Peso | Uso recomendado |
|---|---|---|---|---|
| `assets/logo-base64.txt` | FULL | 900×295 | ~34 KB | **Capa** (obrigatório) |
| `assets/logo-base64-all.txt` | **3-em-1** | FULL + HEADER + SIG | ~62 KB | Quando precisar de múltiplas versões |

### Como usar no HTML gerado

1. Ler o conteúdo de `assets/logo-base64.txt` (apenas uma string longa `data:image/jpeg;base64,...`)
2. Colar o data URI completo dentro de `<img src="...">` na capa
3. Para header fixo menor e assinatura: ler `assets/logo-base64-all.txt`, extrair a seção `=== LOGO_HEADER ===` ou `=== LOGO_SIG ===`

### CSS recomendado para integrar o logo

```css
.logo-lbm { display:flex; justify-content:center; margin-bottom:24px; }
.logo-lbm img {
  max-width: 560px;     /* para capa */
  width: 100%;
  height: auto;
  border-radius: 6px;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.35));
}
.logo-lbm.logo-header img { max-width: 200px; border-radius: 4px; }
.logo-lbm.logo-sig img { max-width: 320px; border-radius: 5px; }
```

**Fundo recomendado para o logo:** navy sólido `#1a2f4e` ou branco `#ffffff` com padding.
Evitar fundos com outros gradientes que briguem com o gradiente interno do próprio logo.

---

## Estrutura visual da capa (HTML)

```html
<section class="capa" id="capa">
  <div class="capa-bg"></div>

  <!-- Nota metodológica (opcional, topo, fundo amarelo claro) -->
  <div class="nota-metodologica">
    ⚠️ Nota metodológica: [descrição breve da abordagem, correções ou limitações]
  </div>

  <!-- Bloco principal -->
  <header class="capa-header">
    <div class="logo-lbm">
      <img src="data:image/png;base64,{LOGO_BASE64}" alt="LBM BORATTI" />
    </div>
    <h6 class="capa-overline">AET</h6>
    <h1 class="capa-titulo">ANÁLISE ERGONÔMICA DO TRABALHO — NR-17</h1>
    <p class="capa-subtitulo">
      [N] Postos de Trabalho — Registro Fotográfico com Achados e
      Recomendações Específicas por Posto
    </p>
  </header>

  <!-- Identificação do cliente -->
  <div class="capa-cliente">
    <h2 class="cliente-nome">{NOME_EMPRESA_MAIUSCULO_ESPAÇADO}</h2>
    <p class="cliente-setores">
      {Setor 1} • {Setor 2} • {Setor 3} • {Setor 4}
    </p>
  </div>

  <!-- Grid de metadados (6 colunas) -->
  <div class="capa-metadados">
    <div class="meta-item">
      <span class="meta-label">DOCUMENTO</span>
      <span class="meta-valor">AET-{CLIENTE}-{ANO}-{SEQ}</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">VERSÃO</span>
      <span class="meta-valor">NR-17 — {Mês}/{Ano}</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">DATA</span>
      <span class="meta-valor">{Mês} / {Ano}</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">POSTOS</span>
      <span class="meta-valor">{N} fotos / {K} setores</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">RISCO GERAL</span>
      <span class="meta-valor risco-{nivel}">{emoji} {NIVEL} — {N} postos CRÍTICOS</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">RESPONSÁVEL</span>
      <span class="meta-valor">Marcelo L. Boratti Melo</span>
    </div>
  </div>

  <!-- Rodapé credenciais -->
  <footer class="capa-credenciais">
    <p>Engenheiro de Segurança do Trabalho — <strong>CREA-SP 5069572947</strong></p>
    <p>Fisioterapeuta & Ergonomista — <strong>CREFITO 3/209468-F</strong></p>
    <p>LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho</p>
  </footer>
</section>
```

---

## Paleta visual da capa

| Elemento | Cor | Uso |
|---|---|---|
| Fundo principal | `#1a2f4e` (navy) | Gradiente radial no centro — **já presente no PNG do logo oficial** |
| Acento laranja | `#e67e22` | Linha divisória no logo (o próprio logo traz uma linha laranja), overline AET |
| Acento teal | `#2dd4bf` | Badge de risco baixo |
| Acento azul-claro | `#7dc4ff` | Texto "BORATTI" do logo original |
| Texto claro | `#f5f5f5` | Títulos sobre navy |
| Texto dourado | `#e7b95c` | Nome da empresa (opcional, complementa o logo) |
| Nota metodológica BG | `#fef3c7` | Fundo amarelo claro |
| Nota metodológica text | `#92400e` | Âmbar escuro |

**Importante:** o logo oficial LBM BORATTI **já tem** gradiente navy embutido e linha laranja de destaque. Na capa, para evitar conflito visual, preferir **fundo sólido** `#1a2f4e` em vez de gradiente repetido — o logo se integra melhor.

---

## Tipografia da capa

- **Overline "AET"**: DM Sans, 11px, letter-spacing 0.4em, uppercase, laranja `#e67e22`
- **Título principal**: DM Serif Display, 42px, peso 400, entrelinha 1.1
- **Subtítulo**: DM Sans, 16px, peso 300, itálico, branco 85%
- **Nome empresa**: DM Serif Display, 34px, letter-spacing 0.15em
- **Meta-labels**: DM Sans, 10px, uppercase, letter-spacing 0.2em, branco 55%
- **Meta-valores**: DM Sans, 14px, peso 500

---

## Variantes permitidas

1. **Capa Executiva** (default) — layout descrito acima
2. **Capa Minimalista** — sem gradiente, fundo sólido `#1a2f4e`, sem nota metodológica
3. **Capa Compacta** (PDF 1 página) — tudo centralizado, metadados em lista vertical

---

## Regras obrigatórias

- Sempre incluir credenciais RT completas (CREA + CREFITO) no rodapé
- Número do documento sempre no formato `AET-{CLIENTE}-{ANO}-{SEQ3}` (ex: `AET-LBMBORATTI-2026-001`)
- Badge de risco geral usa emoji + cor conforme Matriz AIHA (🟢 Baixo / 🟡 Médio / 🟠 Alto / 🔴 Crítico)
- Se houver postos CRÍTICOS, destacar o número em vermelho
- Nota metodológica é **opcional** mas recomendada quando há limitações, correções de análise anterior ou escopo restrito

---

## Exemplo real aplicado (Eletrosert)

```
AET
ANÁLISE ERGONÔMICA DO TRABALHO — NR-17
20 Postos de Trabalho — Registro Fotográfico com Achados e
Recomendações Específicas por Posto

ELETROSERT SERVICE LTDA
Laboratório de Manutenção Eletrônica • Setor Administrativo • Almoxarifado • Recepção

DOCUMENTO         VERSÃO              DATA
AET-ELETROSERT-2025-001   NR-17 — Março/2025   Março / 2025

POSTOS            RISCO GERAL         RESPONSÁVEL
20 fotos / 4 setores   🟠 ALTO — 4 postos CRÍTICOS   Marcelo L. Boratti Melo
```
