# Plano de Migração AS-IS → TO-BE — ConecTA

## 1. Baselines auditadas
Backend master: `6617ddf1d6dc29ccdebef6adb91602cecafe26ab`.
Frontend master: `f41d72e8ace6c716e799131cb46ce425a1a4c215`.

Este plano transforma o protótipo existente na solução definida por G-REQ/G-MODEL sem reescrita total.

## 2. Estratégia
1. estabilizar fundações;
2. corrigir identidade/perfis;
3. implementar marketplace real;
4. implementar contratação/versionamento;
5. implementar execução/pagamento;
6. reputação/conflitos/governação;
7. substituir mockApi/localStorage por API real;
8. validar RF/RNF.

Cada incremento deve entregar modelo + API + autorização + testes antes de depender dele no frontend.

## 3. O que manter/refactor/remover

| Área | AS-IS | Decisão |
|---|---|---|
| Django/DRF | base funcional | MANTER |
| User | funcional | REFACTOR incremental |
| Worker/Employer OneToOne | boa base para perfis acumuláveis | MANTER/RENOMEAR semanticamente quando seguro |
| JWT/auth endpoints | existentes | MANTER e integrar |
| React/Vite/TS/Tailwind | protótipo rico | MANTER |
| páginas/cards existentes | úteis como UI base | REFACTOR |
| mockApi/localStorage | fonte de dados principal | SUBSTITUIR progressivamente |
| role worker/employer/admin singular no frontend | conflita com RN01 | REMOVER/REFACTOR |
| Assessment >=50 | conflita com baseline | REMOVER do núcleo |
| Document exclusivo Employer | unilateral | REFACTOR para VerificationCase |
| Offer/Proposal vazios | placeholders | IMPLEMENTAR como Opportunity/Proposal |
| Contract/Signature vazios | sem domínio | SUBSTITUIR por Engagement/AgreementVersion |
| payments/reviews | placeholders | IMPLEMENTAR segundo baseline |
| messaging/notifications | não-core | ADIAR; manter apenas se auxiliar |
| .venv/__pycache__/db.sqlite3 versionados | higiene deficiente | REMOVER do controlo de versão |

## 4. Incrementos/PRs

### PR-B01 — Repository & test baseline
Objectivo: tornar backend seguro para evolução.
- ampliar .gitignore;
- retirar .venv, __pycache__, .DS_Store e DB local do tracking;
- confirmar settings/env;
- criar estrutura de testes e smoke test;
- documentar comandos de setup/test.
Gate: projecto inicia/migra/testa sem artefactos locais versionados.

### PR-B02 — Identity & accumulable profiles
RF01–RF05.
- preservar User como identidade;
- WorkerProfile e EmployerProfile opcionais/acumuláveis;
- eliminar qualquer role global exclusivo na API;
- modelar ProfessionalEvidence;
- serializers/endpoints/permissões;
- testes: worker-only, employer-only, ambos.
Gate: mesmo User pode activar ambos sem nova conta.

### PR-B03 — Verification redesign
RF06/RF28.
- substituir semântica Document-only-employer por VerificationCase;
- finalidade/status/decisão/auditoria;
- acesso privado;
- retirar Assessment do caminho de aprovação.
Gate: nenhuma competência depende de score >=50.

### PR-B04 — Opportunities
RF07–RF10.
- Opportunity + estados;
- CRUD orientado a estados;
- pesquisa/filtros contextuais;
- perfis consultáveis;
- autorização do proprietário;
- testes de OPEN/PAUSED/CLOSED/MODERATION_HOLD.
Gate: apenas OPEN recebe propostas.

### PR-B05 — Proposals
RF11–RF12.
- Proposal + estados;
- submit/withdraw/accept/reject;
- anti-self-contracting;
- atomicidade na aceitação.
Gate: proposta aceite pode originar apenas uma contratação.

### PR-B06 — Engagement & agreement versioning
RF13–RF14/RF17–RF18.
- Engagement;
- AgreementVersion;
- PaymentTerms;
- fluxo PENDING_AGREEMENT → ACTIVE;
- versões imutáveis/históricas;
- testes de rejeição/aceitação/alteração.
Gate: mudança material nunca sobrescreve acordo aceite.

### PR-B07 — Execution & delivery
RF15–RF17.
- ExecutionRecord;
- actualizações;
- delivery/completion;
- transições ACTIVE → DELIVERED → COMPLETED.
Gate: histórico identifica autor/timestamp.

### PR-B08 — Payment records
RF18–RF19.
- PaymentRecord;
- report/confirm/dispute;
- separar conclusão do serviço de confirmação financeira.
RF20 PSP fica fora deste PR por ser Could.
Gate: zero custódia/saldo ConecTA.

### PR-B09 — Reputation
RF21–RF23.
- Review bilateral/contextual;
- elegibilidade;
- ReviewContest;
- impedir auto-review/duplicação indevida.
Gate: reputação rastreável a Engagement.

### PR-B10 — Disputes & moderation
RF24–RF28.
- Dispute/Evidence;
- estados;
- ModerationAction;
- oportunidade reportada;
- user measures com reason;
- sem arbitragem.
Gate: acções administrativas auditáveis.

### PR-F01 — API foundation/auth
- cliente HTTP configurável;
- JWT real;
- AuthContext deixa de usar identidade mock;
- tratamento uniforme 401/403/validation.
Gate: login/registo contra backend.

### PR-F02 — Multi-profile UX
- remover role singular;
- permitir activar/completar WorkerProfile e EmployerProfile;
- navegação por capacidades.
Gate: utilizador com ambos alterna contexto sem trocar conta.

### PR-F03 — Marketplace integration
- OffersList → Opportunities;
- WorkersList/ProfileDetail via API;
- criar/editar/publicar oportunidade;
- proposal flows reais.
Gate: DA01 executável E2E.

### PR-F04 — Engagement/agreement UX
- contratação;
- condições;
- versionamento/aceitação;
- histórico.
Gate: DA02 executável E2E.

### PR-F05 — Delivery/payment UX
- execution/delivery/completion;
- PaymentTerms/PaymentRecord;
- sem simular custódia.
Gate: DA03 executável E2E.

### PR-F06 — Reputation/disputes/admin UX
- review/contest;
- report/follow dispute;
- superfícies administrativas necessárias.
Gate: DA04 + review executáveis.

### PR-F07 — Remove mock domain
- eliminar dependência funcional de mockApi/localStorage para RF finais;
- seed/demo apenas por mecanismo explicitamente de desenvolvimento;
- remover/ocultar features não suportadas como core.
Gate: protótipo validável usa backend real.

### PR-I01 — Optional PSP
Somente se houver tempo/evidência para RF20.
- Adapter;
- provider sandbox;
- PaymentTransaction;
- testes de falha/sucesso/idempotência.
Não bloqueia validação do núcleo.

## 5. Ordem e dependências
B01 → B02 → B03
B02 → B04 → B05 → B06 → B07/B08 → B09/B10
F01 pode iniciar após B02.
F02 após B02.
F03 após B04/B05.
F04 após B06.
F05 após B07/B08.
F06 após B09/B10.
F07 após integrações.
PSP só depois de PaymentRecord estável.

## 6. Estratégia de testes
Cada PR backend:
- model/domain tests para invariantes;
- API permission tests;
- state-transition tests;
- negative paths;
- migration check.

Integração:
- cenários DA01–DA04;
- utilizador com ambos os perfis;
- tentativa de self-contracting;
- alteração de acordo preserva histórico;
- conclusão ≠ pagamento;
- contestação/review/dispute.

Frontend:
- build/typecheck;
- fluxos essenciais;
- responsividade nos viewports definidos na validação.

## 7. Mapeamento para validação da monografia
- Cenário V01: registar/activar perfis → RF01–RF05.
- V02: publicar/pesquisar/propor/aceitar → RF07–RF12.
- V03: formalizar/alterar → RF13–RF14/RF18.
- V04: executar/entregar/histórico → RF15–RF17.
- V05: pagamento registado/confirmado → RF18–RF19.
- V06: avaliar/contestar → RF21–RF23.
- V07: reportar/acompanhar conflito → RF24–RF25.
- V08: governação/verificação → RF06/RF26–RF28.
RF20 é opcional e não deve contaminar conclusão se não implementado.

## 8. Primeiro incremento
**Começar por PR-B01, não pelo frontend.**

Razão: o backend contém artefactos locais versionados e praticamente todos os módulos centrais estão vazios. Criar funcionalidades antes de estabelecer baseline de testes/migrações aumentaria o risco de refactor regressivo.

## 9. Gate
**G-MIGRATION-PLAN: PASS.**

A implementação pode iniciar incrementalmente. Cada PR deve ser confrontado com esta matriz e com G-REQ antes de merge.
