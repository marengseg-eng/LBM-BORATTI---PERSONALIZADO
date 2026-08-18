---
name: relatorio-inspecao-sst
version: 2.0.0
description: "Gera Relatórios de Inspeção de Segurança do Trabalho (RIS) para LBM BORATTI Consultoria em SST, conforme NR-01, NR-06, NR-10, NR-12, NR-13, NR-15, NR-17, NR-18, NR-23, NR-26, NR-33 e NR-35. Use SEMPRE que mencionar: relatório de inspeção, inspeção de segurança, RIS, vistoria de segurança, auditoria de campo, walkthrough, walkdown, check-list NR, diagnóstico SST, gap analysis, inspeção BBS, observação comportamental, ato inseguro, condição insegura, não-conformidade SST, NC SST, levantamento de EPI, fotos de campo, registro fotográfico SST, visita técnica de segurança, inspeção NR-06/NR-10/NR-11/NR-12/NR-13/NR-17/NR-18/NR-23/NR-26/NR-33/NR-35. Acionar também para fotos de área operacional para análise de risco, setores como linha de produção, oficina mecânica, almoxarifado, canteiro de obras, área química, casa de bombas. Outputs: HTML Premium Full-Edit Engine (azul #1a2f4e / laranja #e67e22), Word (.docx) e impressão A4 em 4 folhas."
author: LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
---

# SKILL: Relatório de Inspeção SST — LBM BORATTI

Gera Relatórios Técnicos de Inspeção em Segurança e Saúde no Trabalho com força probatória
técnica e rastreabilidade documental para fins de PGR/GRO (NR-01), eSocial S-2240 e defesa
em fiscalização MTE. Histórico de versões em `CHANGELOG.md`.

---

## 0. REGRAS ABSOLUTAS ANTES DE GERAR

1. **NUNCA mencionar PPRA** — documento vigente é PGR conforme NR-01 revisada.
2. **Sempre citar NR + item exato** ao classificar achados (ex.: "NR-12 item 12.38.2").
3. **Sinalizar incertezas** com ⚠️ quando a norma exata não for confirmável; os itens
   listados em `references/normas_inspecao.md` são referência rápida e devem ser
   confirmados na redação vigente (gov.br) antes do documento final — várias NRs
   foram renumeradas nos últimos anos.
4. **Assinatura e rodapé sempre presentes**:
   - Marcelo Luis Boratti Melo
   - Engenheiro de Segurança do Trabalho — CREA-SP: 5069572947
   - Fisioterapeuta e Ergonomista — CREFITO 3/209468-F
   - LBM BORATTI — Consultoria Personalizada em Segurança e Saúde no Trabalho
   - marengseg@gmail.com | (16) 99338-8989
5. **NR-01 é base sempre** — todo achado deve ser enquadrável no inventário de riscos do PGR.
6. **Numeração de NC**: NC-001, NC-002, NC-003… em ordem de criticidade (Crítico primeiro).
7. **RASTREABILIDADE DO ACHADO (rótulos obrigatórios):**
   - `OBSERVADO` — visto em foto/vídeo enviado ou relatado por Boratti na sessão.
     **Só achado OBSERVADO entra como não-conformidade constatada.**
   - `[MODELO — editar conforme observado]` — item típico pré-preenchido para
     agilizar edição em campo. Aparece com esse marcador visível no card e NÃO
     entra na contagem de NCs do sumário até ser confirmado/editado.
   - Sem fotos e sem relato → o documento sai como **relatório-modelo** com itens
     típicos rotulados e aviso no sumário executivo: "Versão-modelo para preenchimento
     em campo — achados pendentes de constatação". **Nunca apresentar item típico
     como achado constatado.**

---

## 1. MODOS DE OPERAÇÃO

### MODO 1 — Inspeção Geral SST (padrão)
Para inspeções gerais de campo cobrindo múltiplas categorias de risco.
**Estrutura**: 9 seções (ver § 3). **Quando usar**: não há NR específica mencionada.

### MODO 2 — Inspeção Modular por NR
Inspeção focada em uma NR específica (ex.: "quero inspecionar NR-12").
**Estrutura**: mesmas 9 seções, com checklist e achados filtrados pela NR citada.

### MODO 3 — Walkthrough Survey (pré-AET / pré-auditoria)
Levantamento expedito para alimentar AET ou auditoria ISO 45001.
**Estrutura**: Dados Gerais → Achados → Foto → Encaminhamentos.
**Saída**: HTML compacto (2 páginas A4) + bloco JSON para a skill aet-premium.

### MODO 4 — Inspeção Comportamental BBS
Observação de comportamentos (atos inseguros × comportamentos seguros).
**Estrutura**: adiciona seção de Análise Comportamental (taxa de segurança, top 3
comportamentos críticos). **Referência**: OSHA BBS Guidelines + NR-01 (participação
dos trabalhadores).

---

## 2. FLUXO DE TRABALHO

```
INPUT DO USUÁRIO
      │
      ▼
[Extrair dados do contexto] ← sempre antes de perguntar
      │
      ├── Dados suficientes? ──SIM──► GERAR HTML
      │
      └── Não ──► PERGUNTAR (1 mensagem, máx. 5 campos)
                        │
                        ▼
                  GERAR HTML COMPLETO
                        │
                        ▼
                  OFERECER Word (.docx) se solicitado
```

**Dados mínimos obrigatórios:** empresa · área/setor · data · tipo (rotineira /
programada / pós-acidente / não programada).
**Opcionais:** responsável pela área, nº trabalhadores, fotos, CNPJ, GR (1/2/3/4).

---

## 3. ESTRUTURA DO DOCUMENTO (9 SEÇÕES)

1. **CAPA** — Logo LBM (injeção por script; indisponível → fallback textual) + logo do
   cliente (botão 🏢) · título "RELATÓRIO DE INSPEÇÃO DE SEGURANÇA DO TRABALHO" ·
   empresa / área / data / **inspetor** / GR / tipo.
2. **SUMÁRIO EXECUTIVO** — síntese + 4 KPIs: Total NCs | Críticas | Médias | Baixas.
   KPIs contam apenas achados `OBSERVADO`; se houver itens `[MODELO]`, exibir aviso
   de versão-modelo.
3. **DADOS GERAIS** — tabela editável (empresa, CNPJ, endereço, área, data, horário,
   inspetor, método, nº trabalhadores, GR, CNAE).
4. **VERIFICAÇÃO DE EPIs (NR-06)** — tabela: EPI | CA válido? | Conservação | Uso
   correto? | NC — badge auto-colorido.
5. **ATOS INSEGUROS (AI)** — cards: NC-XXX | descrição | foto | criticidade | NR+item |
   causa raiz | prazo | rótulo de rastreabilidade.
6. **CONDIÇÕES INSEGURAS (CI)** — cards: NC-XXX | descrição | foto | criticidade |
   NR+item | custo estimado | prazo | rótulo.
7. **REGISTROS FOTOGRÁFICOS** — grid com caption editável, NC vinculado e badge.
8. **PLANO DE AÇÃO 5W2H** — cards por NC: What | Why | Who | When | Where | How |
   How Much · semáforo de prazo (vermelho vencido / amarelo próximo / verde ok).
9. **CONCLUSÃO E ASSINATURAS** — parecer técnico (contenteditable) + campos de
   assinatura (bloco da Regra 4).

---

## 4. HTML FULL-EDIT ENGINE — ESPECIFICAÇÕES

### 4.1 Padrão Visual LBM
```css
--azul:    #1a2f4e;
--laranja: #e67e22;
--critico: #c0392b;
--alto:    #d35400;
--medio:   #956d00;
--baixo:   #1e8449;
--info:    #2a4f7c;
```
(CRÍTICO e ALTO têm cores distintas — badges precisam ser distinguíveis.)

### 4.2 Print CSS + paginação dinâmica (regra crítica)
```css
@page { size: A4; margin: 0; }
@media print {
  .pagina { height: 297mm; overflow: hidden; page-break-after: always; break-after: page; }
  .toolbar, .no-print { display: none !important; }
  print-color-adjust: exact;
  -webkit-print-color-adjust: exact;
}
```
**⚠ Conteúdo dinâmico:** os botões ➕ adicionam cards — página cheia + `overflow:hidden`
= conteúdo cortado em silêncio na impressão. Obrigatório: função JS que, ao adicionar
card, verifica a altura útil da `.pagina` corrente e **cria nova `.pagina`** (herdando
cabeçalho da seção) quando exceder. Nunca deixar card entrar em página sem espaço.

### 4.3 Toolbar (oculta no print)
🖨️ Imprimir/PDF | ➕ Ato Inseguro | ➕ Condição Insegura | ➕ Ação 5W2H | 📷 Foto | 🏢 Logo Empresa

### 4.4 Logos e fotos — regra de injeção
- **Logo LBM:** embutido por **script** a partir do asset (nunca digitado como base64
  pelo modelo). Asset indisponível → fallback textual "LBM BORATTI" + comentário HTML.
- **Logo do cliente:** botão 🏢 com FileReader (código abaixo).
- **Fotos enviadas pelo usuário:** o modelo NÃO consegue reproduzir imagem como
  base64 "de cabeça". Fluxo obrigatório: localizar o arquivo em
  `/mnt/user-data/uploads/`, converter via script (`base64` no bash ou Python) e
  injetar no HTML com marcadores `__FOTO_01__` substituídos programaticamente.
  Sem acesso ao arquivo → placeholder clicável 📷 para o usuário inserir depois.

```javascript
function insertLogoEmpresa() {
  const inp = document.createElement('input');
  inp.type = 'file'; inp.accept = 'image/*';
  inp.onchange = e => {
    const fr = new FileReader();
    fr.onload = ev => {
      const img = document.querySelector('.capa-logo-cliente img');
      if (img) {
        img.src = ev.target.result;
        img.style.cssText = 'max-height:60px;background:#fff;padding:6px 10px;border-radius:4px;';
      }
    };
    fr.readAsDataURL(e.target.files[0]);
  };
  inp.click();
}
```

### 4.5 Conteúdo editável
- Campos de texto: `contenteditable="true"` · tabelas com linhas adicionáveis/removíveis ·
  cards AI/CI/5W2H adicionáveis/removíveis (com paginação da 4.2) · fotos trocáveis por
  clique no placeholder.
- Ao editar um card `[MODELO]`, o marcador deve poder ser removido por clique
  (confirmando o achado) — aí ele passa a contar nos KPIs.
- NÃO usar `filter: brightness(0) invert(1)` no logo (quebra impressão).

---

## 5. CLASSIFICAÇÃO DE CRITICIDADE E PRAZOS

| Nível | Cor | Prazo | Critério |
|-------|-----|-------|----------|
| CRÍTICO | `--critico` #c0392b | Imediato / interdição | Risco de morte ou lesão grave iminente |
| ALTO | `--alto` #d35400 | ≤ 7 dias | Risco de lesão com afastamento |
| MÉDIO | `--medio` #956d00 | ≤ 30 dias | Risco de lesão sem afastamento / multa |
| BAIXO | `--baixo` #1e8449 | ≤ 90 dias | Melhoria de conformidade / preventivo |

Matriz P×C completa e badges: `references/criterios_severidade.md`.

---

## 6. CITAÇÃO NORMATIVA OBRIGATÓRIA

Todo achado DEVE citar NR + item: `"[Descrição] — em desconformidade com [NR-XX item XX.XX.XX]"`.
Lista de itens frequentes: `references/normas_inspecao.md` (referência rápida —
**confirmar na redação vigente antes do documento final**).
⚠️ Sinalizar "⚠️ confirmar item exato" quando houver incerteza.

---

## 7. INTEGRAÇÃO COM OUTRAS SKILLS

| Situação | Encaminhar para |
|----------|----------------|
| Inspeção revela necessidade de AET | aet-premium |
| Achados geram ação PGR | gestao-sst-completa |
| Achado NR-15 → insalubridade | pericia-trabalhista-pro |
| CIPA deficiente | cipa-eleicao |
| Virar proposta comercial | proposta-comercial-sst |

---

## 8. ANTI-PADRÕES

- ❌ Nunca apresentar item típico/pré-preenchido como achado constatado — usar o
  rótulo `[MODELO — editar conforme observado]` (Regra 7)
- ❌ Nunca citar PPRA
- ❌ Nunca omitir o bloco de assinatura da Regra 4
- ❌ Nunca perguntar em múltiplas rodadas — uma pergunta com todos os campos
- ❌ Nunca digitar base64 de logo/foto no output — injeção por script
- ❌ Nunca deixar card novo ser cortado por `overflow:hidden` na impressão

---

## 9. OUTPUTS

| Formato | Quando usar |
|---------|-------------|
| HTML Full-Edit | Sempre (padrão) — A4 print-ready, paginação dinâmica |
| Word (.docx) | Envio formal / assinatura física — ler `/mnt/skills/public/docx/SKILL.md` antes |
| PDF | Entrega final via botão imprimir |

Ambiente sem geração de arquivo → entregar conteúdo estruturado; nunca fingir que o
arquivo foi gerado; nunca alegar leitura de asset inacessível.
