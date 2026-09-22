# Modelo de Estados do Domínio — ConecTA

## Princípios
Cada agregado possui ciclo próprio. Estados tornam explícitos actores, transições, evidência e estados terminais.

## Opportunity
Estados: DRAFT, OPEN, PAUSED, CLOSED, CANCELLED, MODERATION_HOLD, REMOVED.

Transições:
- DRAFT → OPEN: empregador publica.
- OPEN ↔ PAUSED: empregador pausa/retoma.
- OPEN/PAUSED → CLOSED ou CANCELLED.
- OPEN/PAUSED → MODERATION_HOLD: moderação suspende após reporte/análise.
- MODERATION_HOLD → OPEN ou REMOVED, com motivo registado.

Regras: apenas OPEN recebe novas propostas; preço pode ficar por definir quando houver diagnóstico prévio; localização é contextual; autor não pode propor à própria oportunidade.

## Proposal
Estados: DRAFT, SUBMITTED, WITHDRAWN, REJECTED, ACCEPTED, SUPERSEDED.

Transições:
- DRAFT → SUBMITTED.
- SUBMITTED → WITHDRAWN, REJECTED ou ACCEPTED.
- SUBMITTED → SUPERSEDED quando nova versão substitui condições ainda em negociação.

ACCEPTED cria a base da contratação, mas não significa que todas as condições finais já estejam formalizadas. Alterações posteriores pertencem ao Agreement.

## Engagement / Agreement
Recomenda-se Engagement como agregado da contratação e AgreementVersion para condições acordadas. Na monografia: Contratação/Acordo.

Estados do Engagement: PENDING_AGREEMENT, ACTIVE, DELIVERED, COMPLETED, CANCELLED, IN_DISPUTE.

Fluxo:
Proposal.ACCEPTED → PENDING_AGREEMENT → ACTIVE → DELIVERED → COMPLETED.
PENDING_AGREEMENT pode terminar em CANCELLED.
ACTIVE/DELIVERED podem passar a IN_DISPUTE; após encerramento do conflito, regressam ao estado operacional apropriado ou terminam em COMPLETED/CANCELLED conforme o caso.

AgreementVersion preserva versão, escopo, entregáveis quando aplicável, prazo, condições de pagamento, termos relevantes, proponente, data/hora e aceitação de cada parte.
Estados: PROPOSED → ACCEPTED | REJECTED | SUPERSEDED.
A versão ACCEPTED mais recente é vigente; alterações nunca apagam versões anteriores.

## Payment
Separar:
1. PaymentTerms — condições acordadas;
2. PaymentRecord — registo/estado de cumprimento;
3. PaymentTransaction — transacção real de PSP, apenas se houver integração.

PaymentRecord: PENDING, REPORTED_PAID, CONFIRMED, FAILED, CANCELLED, DISPUTED.

Regras: ConecTA não é custodiante; confirmação por API só com PSP real; pagamentos podem ser únicos, adiantados, parcelados ou por etapas; divergência pode originar Dispute.

## Dispute
Estados: OPEN, UNDER_REVIEW, WAITING_INFORMATION, RESOLVED, CLOSED.

Fluxo: OPEN → UNDER_REVIEW; UNDER_REVIEW ↔ WAITING_INFORMATION; UNDER_REVIEW → RESOLVED; OPEN/UNDER_REVIEW → CLOSED quando aplicável.

RESOLVED significa encerramento/registo na plataforma, não poder jurídico ou técnico de arbitragem da ConecTA.

## Review
Estados candidatos: DRAFT → PUBLISHED → CONTESTED → PUBLISHED ou HIDDEN.

Review associa-se a contratação elegível; é bilateral; preserva perspectiva/contexto; contestação não remove automaticamente; ocultação exige motivo.

## Dependências
User possui opcionalmente WorkerProfile e/ou EmployerProfile.
EmployerProfile cria Opportunity.
WorkerProfile cria Proposal para Opportunity.
Proposal ACCEPTED origina Engagement.
Engagement agrega AgreementVersion, PaymentTerms/PaymentRecord, registos de execução/entrega, Reviews e Disputes.

O mesmo User pode possuir ambos os perfis, mas não pode ocupar as duas partes da mesma contratação.

## Consequências para os RF
A modelação confirma gestão de oportunidade/proposta, condições acordadas, versionamento, entrega, histórico, condições/estado de pagamento, reputação contextual/bilateral, conflitos e moderação.

Ajustes de atomicidade:
- editar oportunidade integra gestão de Opportunity;
- gestão da proposta própria integra submissão/gestão;
- aceitar/rejeitar proposta permanece comportamento do empregador;
- aceitar condições integra formalização do Agreement;
- consultar contrato torna-se consulta de condições/histórico;
- confirmar/receber pagamento tornam-se transições de PaymentRecord;
- notificações são reacções auxiliares a transições;
- mensagens só entram se necessárias à rastreabilidade; histórico do Engagement é central.

## Gate
**G-DOMAIN-STATES: PASS.**

Próximo: atomicidade final dos RF, consolidação das RN, critérios verificáveis dos RNF e matriz final de rastreabilidade antes de G-REQ e UML.
