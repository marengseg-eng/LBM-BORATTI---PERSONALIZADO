---
tipo: norma
titulo: NR-01 — Disposições Gerais e Gerenciamento de Riscos Ocupacionais
nr: NR-01
status: vigente
verificado_em: 2026-08-18
tags: [sst/norma/nr-01, sst/pgr]
---

# NR-01 — Disposições Gerais e GRO

A NR-01 é o guarda-chuva. Toda outra NR pendura nela: é ela que obriga a organização a
**identificar perigos, avaliar riscos, definir medidas de controle e acompanhar o
resultado** — o ciclo do GRO. O PGR é o documento que prova que esse ciclo existe.

## Campo de aplicação

Todas as organizações com empregados regidos pela CLT. MEI é dispensado do PGR; ME e EPP
de grau de risco 1 e 2 têm tratamento simplificado (podem dispensar o PGR quando não
identificarem exposições que exijam medidas de controle, comprovado por declaração
conforme os anexos da norma).

## O que exige, na prática

### 1. Inventário de riscos
Para cada GHE / função / ambiente:
- perigo identificado (fonte, circunstância, tarefa)
- lesão ou agravo possível
- avaliação: severidade × probabilidade → nível de risco
- medidas de controle existentes e sua eficácia
- necessidade de monitoramento quantitativo (aí entra a [[NR-09 — Avaliação e Controle das Exposições]])

### 2. Plano de ação
Cada risco não tolerável vira ação **com responsável e prazo**. Plano de ação sem nome e
sem data é o achado mais fácil de uma auditoria.

### 3. Hierarquia de medidas
Eliminação → substituição → controle de engenharia → administrativo/organizacional →
EPI. Documento que salta direto para EPI sem justificar por que as anteriores são
inviáveis é frágil em perícia.

### 4. Riscos psicossociais
A revisão da NR-01 incorporou os fatores de risco psicossocial ao GRO: eles devem ser
identificados, avaliados e tratados dentro do mesmo ciclo, não em documento paralelo.
Ver [[Riscos Psicossociais - NR-01 e ISO 45003]] e a skill `psicossocial-nr01`.

> [!warning] Vigência do capítulo psicossocial
> A exigência teve prazo escalonado e fase inicial de caráter orientativo. Confirme a
> data-limite aplicável ao cliente antes de afirmar que ele está em infração —
> e registre a fonte na nota do cliente.

### 5. Análise de acidentes e de quase-acidentes
Todo acidente e doença relacionada ao trabalho é analisado, e o resultado **retroalimenta
o inventário**. Ver [[T - Acidente]] e a skill `investigador-de-acidentes-sst`.

### 6. Informação e capacitação
Treinamento inicial, periódico e eventual; ordens de serviço; comunicação dos riscos ao
trabalhador de forma compreensível.

## Prazos e periodicidade

| Item | Prazo |
|---|---|
| Revisão do PGR | até **2 anos**; até **3 anos** para organizações com certificação em sistema de gestão de SST conforme previsto na norma |
| Revisão extraordinária | após acidente grave/fatal, mudança de processo, layout, maquinário, nova exigência legal ou identificação de novo risco |
| Retenção dos documentos | mínimo de **20 anos** para os registros do GRO |
| Plano de ação | prazos individuais por ação; acompanhamento contínuo |

## O que gera autuação

- Não possuir PGR (quando obrigatório)
- PGR sem inventário de riscos ou sem plano de ação
- Plano de ação sem prazo ou sem responsável
- Não implementar as medidas previstas no próprio plano
- Não analisar acidente ocorrido
- Não capacitar / não emitir ordem de serviço

## Erros comuns que eu vejo em campo

1. **PGR de prateleira**: comprado pronto, com GHE que não existe na empresa.
2. **Inventário sem tarefa**: risco descrito por função genérica, sem a atividade que gera
   a exposição. Perícia derruba.
3. **Plano de ação com "contínuo" no lugar de data**.
4. **PGR que não conversa com o PCMSO**: risco no PGR sem exame correspondente, ou exame
   sem risco declarado. É o cruzamento mais explorado pela fiscalização e pelo perito.
5. **Medida de controle listada como implantada, sem evidência** (foto, nota fiscal, ART).

## Cruzamentos

- [[NR-09 — Avaliação e Controle das Exposições]] — quantificação da exposição
- [[NR-07 — PCMSO]] — o programa médico se baseia no inventário
- [[NR-05 — CIPA e CIPA+A]] — a CIPA participa do processo e do mapa de risco
- [[NR-17 — Ergonomia]] — a AET alimenta o inventário na parte ergonômica
- LTCAT/PPP — a caracterização do PGR precisa bater com a previdenciária ([[MOC - Entregáveis]])

## Checklist rápido de conformidade

- [ ] PGR existente e vigente (data de revisão dentro do prazo)
- [ ] Inventário cobre todos os GHE e todas as tarefas críticas
- [ ] Nível de risco calculado com critério declarado
- [ ] Plano de ação com responsável, prazo e status
- [ ] Evidência de implantação das medidas concluídas
- [ ] Análise de acidentes do período incorporada
- [ ] Riscos psicossociais avaliados e tratados no mesmo ciclo
- [ ] Ordens de serviço entregues e assinadas
- [ ] Documentos retidos e acessíveis
