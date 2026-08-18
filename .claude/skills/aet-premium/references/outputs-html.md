# OUTPUTS — Especificação Completa (HTML Premium · Word · PDF)

Referência obrigatória do **Passo 4** da skill `aet-premium`.
Consolida e substitui as specs de output antes espalhadas no SKILL.md.

---

## OUTPUT 1 — HTML Premium (FULL EDIT ENGINE)

> Ler também: `references/full-edit-engine.md` (arquitetura de edição) e
> `assets/html-template.md` (estrutura visual base). Em caso de divergência entre
> arquivos, **este documento prevalece**.

### Identidade visual
- **Paleta:** `#1a2f4e` (navy principal) · `#e67e22` (laranja destaque) ·
  `#2dd4bf` (teal) · `#f5f5f5` (cinza claro)
- **Tipografia obrigatória:** `DM Serif Display` (títulos) + `DM Sans` (corpo) +
  `JetBrains Mono` (scores/código), sempre com fallbacks declarados
  (`Georgia, serif` / `Arial, sans-serif` / `monospace`).

### Princípio "self-contained" — definição precisa (resolve ambiguidade antiga)
- **Lógica JavaScript, CSS e dados: 100% embutidos.** Nenhuma biblioteca via CDN.
- **Fontes são a única exceção permitida:** carregar via Google Fonts (`<link>`)
  **ou** `@font-face` base64 quando for exigido offline total.
- **Ambiente sem acesso às fontes premium:** usar os fallbacks e registrar a
  limitação em comentário HTML — nunca declarar conformidade falsa.

### Logo LBM BORATTI — injeção programática (regra crítica)
- O logo é embutido como `data:image/jpeg;base64,...` a partir de
  `assets/logo-base64.txt` (ou `logo-base64-all.txt` para as versões FULL/HEADER/SIG).
- **PROIBIDO ao modelo digitar/reproduzir o conteúdo base64 no próprio output.**
  A injeção é feita por script. Padrão:

```bash
# 1. Gerar o HTML com o marcador __LOGO_LBM__ no lugar do data URI
# 2. Injetar via Python:
python3 - <<'EOF'
logo = open('assets/logo-base64.txt').read().strip()
html = open('/home/claude/aet.html').read()
open('/home/claude/aet.html','w').write(html.replace('__LOGO_LBM__', logo))
EOF
```

- Se `assets/logo-base64.txt` **não estiver acessível** na sessão: inserir
  `<!-- LOGO PENDENTE: assets/logo-base64.txt não acessível nesta sessão -->`
  + fallback textual "LBM BORATTI" estilizado. Nunca simular um data URI.

### Montagem por seções (anti-truncamento)
Documentos AET completos são longos. **Nunca** gerar o HTML inteiro em uma única
emissão de texto. Fluxo obrigatório:
1. Criar o esqueleto (head + CSS + nav) em arquivo.
2. Anexar seção a seção via `cat >> arquivo` ou script Python.
3. Injetar logo (acima) e fechar o documento.
4. Validar: arquivo termina com `</html>`; nenhuma tag aberta.

### Componentes obrigatórios
- Tabelas com zebra-striping, bordas elegantes, badges coloridos
- Dark/light toggle com persistência em `localStorage`
- Scroll progress bar + navegação ativa via IntersectionObserver
- Toast notifications + shimmer "MÉTODO LBM BORATTI"
- Menu hamburger + drawer lateral em telas `<900px`
  (`btn-hamburger` + `nav-drawer` + `drawer-overlay`)
- Botão "Voltar ao topo" (`btn-back-top`) flutuante após scroll `>500px`
- Botão "➕ Adicionar linha" em cada tabela editável (Matriz AIHA, PAE)
- Badge pulsante `.unsaved` no botão 💾 quando houver edições pendentes
- **FULL EDIT ENGINE:** `contenteditable` em todos os campos, sync S4↔S7,
  exportação CSV/JSON, menu de contexto em tabelas, indicador visual de edição
- Atalhos: `Ctrl+E` editar · `Ctrl+S` salvar · `Ctrl+P` PDF · `/` glossário · `Esc` sair
- Glossário com busca ao vivo (quando seção 3.12 incluída)

### Responsividade — definição única (resolve contradição 3 vs 4 breakpoints)
- **3 breakpoints responsivos:** `900px` (tablet) · `560px` (mobile) · `380px` (micro/iPhone SE)
- **+ 1 media query de impressão:** `@media print` (regras abaixo)
- **+** `@media (prefers-reduced-motion: reduce)` (acessibilidade)
- `aria-label` em todos os botões de ícone

### Regras de impressão / PDF (aplicam-se ao HTML e ao PDF final)
- `print-color-adjust: exact`; margens estáveis; área útil A4 compatível com tabelas
- Nenhum overflow horizontal em qualquer elemento
- Imagens redimensionadas proporcionalmente à largura útil
- Sem títulos órfãos no fim de página
- Sem quebra interna de: identificação, quadros de metodologia, scores, itens do PAE,
  foto+legenda, assinatura, blocos de checklist (`break-inside: avoid`)
- Tabelas longas: quebrar apenas entre linhas; repetir `<thead>` na página seguinte
- Nunca cortar conteúdo no rodapé; bloco que não couber vai inteiro para a próxima página
- **Integridade do documento > estética avançada**

---

## OUTPUT 2 — Word (.docx)

- **Ler antes:** `/mnt/skills/public/docx/SKILL.md`
- Estilos Heading 1/2/3 consistentes; numeração automática de seções
- Tabelas formatadas na paleta LBM
- Cabeçalho e rodapé com dados do RT (CREA + CREFITO) e paginação
- Placeholders `{{...}}` destacados (realce amarelo) para preenchimento posterior

---

## OUTPUT 3 — PDF

- **Ler antes:** `/mnt/skills/public/pdf/SKILL.md`
- Preferir renderização a partir do HTML (WeasyPrint/Chromium) — preserva o visual premium
- Metadados preenchidos: autor (RT), título, palavras-chave
- Aplicar integralmente as regras de impressão do Output 1
- Validar visualmente: nenhuma tabela/coluna cortada, nenhuma quebra indevida

---

## CHECKLIST DE QA DOS OUTPUTS (executar antes de entregar)

- [ ] Fontes: `grep "DM Serif Display"` presente no HTML (ou limitação registrada)
- [ ] Logo: `grep "data:image"` presente **ou** comentário `LOGO PENDENTE`
- [ ] Base64 injetado por script — não digitado pelo modelo
- [ ] `grep "__LOGO_LBM__"` → **0** (marcador substituído)
- [ ] HTML termina em `</html>` (sem truncamento)
- [ ] 3 breakpoints (900/560/380) + `@media print` + `prefers-reduced-motion` presentes
- [ ] Hamburger, back-top, "➕ Adicionar linha", badge `.unsaved` funcionais
- [ ] Export CSV/JSON e edição `contenteditable` funcionais
- [ ] Impressão A4: nada cortado, cabeçalhos de tabela repetidos, assinatura íntegra
