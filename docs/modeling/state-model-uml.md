# Modelo de Estados UML — ConecTA

## 1. Âmbito
A ConecTA não possui um único estado global. Cada agregado mantém o seu próprio ciclo de vida. Esta separação evita estados ambíguos e permite que contratação, pagamento, conflito e avaliação evoluam independentemente.

## 2. Opportunity
`[*] → DRAFT → OPEN`
- OPEN ↔ PAUSED
- OPEN/PAUSED → CLOSED
- OPEN/PAUSED → CANCELLED
- OPEN/PAUSED → MODERATION_HOLD
- MODERATION_HOLD → OPEN
- MODERATION_HOLD → REMOVED
- CLOSED/CANCELLED/REMOVED → [*]

Guardas:
- apenas OPEN aceita novas Proposal;
- publicação exige dados mínimos válidos;
- MODERATION_HOLD/REMOVED dependem de acção de moderação registada.

## 3. Proposal
`[*] → DRAFT → SUBMITTED`
- SUBMITTED → WITHDRAWN
- SUBMITTED → REJECTED
- SUBMITTED → ACCEPTED
- SUBMITTED → SUPERSEDED
- estados terminais → [*]

Guardas:
- Opportunity deve estar OPEN na submissão;
- proponente não pode ser o próprio autor da Opportunity;
- ACCEPTED pode originar no máximo um Engagement.

## 4. Engagement
`[*] → PENDING_AGREEMENT → ACTIVE → DELIVERED → COMPLETED → [*]`
- PENDING_AGREEMENT → CANCELLED
- ACTIVE → CANCELLED quando permitido pelas condições/regras
- ACTIVE/DELIVERED → IN_DISPUTE
- IN_DISPUTE → ACTIVE, DELIVERED, COMPLETED ou CANCELLED conforme o estado operacional válido após acompanhamento.

Guardas:
- ACTIVE exige AgreementVersion ACCEPTED vigente;
- worker.user != employer.user;
- COMPLETED não implica PaymentRecord CONFIRMED.

## 5. AgreementVersion
`[*] → PROPOSED`
- PROPOSED → ACCEPTED
- PROPOSED → REJECTED
- PROPOSED → SUPERSEDED
- estados finais → [*]

Regra: uma versão aceite nunca é editada para representar nova condição; a alteração cria vN+1. A versão ACCEPTED mais recente é vigente.

## 6. PaymentRecord
`[*] → PENDING`
- PENDING → REPORTED_PAID
- PENDING/REPORTED_PAID → CANCELLED quando aplicável
- PENDING/REPORTED_PAID → FAILED quando houver tentativa externa falhada
- REPORTED_PAID → CONFIRMED
- PENDING/REPORTED_PAID/CONFIRMED → DISPUTED quando existe contestação válida
- DISPUTED → CONFIRMED, PENDING ou CANCELLED conforme o resultado registado.

PaymentRecord representa cumprimento/estado; PaymentTransaction, se existir, representa apenas referência à operação do PSP.

## 7. Dispute
`[*] → OPEN → UNDER_REVIEW`
- UNDER_REVIEW ↔ WAITING_INFORMATION
- UNDER_REVIEW → RESOLVED
- OPEN/UNDER_REVIEW/WAITING_INFORMATION → CLOSED quando aplicável
- RESOLVED/CLOSED → [*]

RESOLVED significa resolução registada no processo da plataforma, não decisão jurídica/arbitral.

## 8. Review
`[*] → DRAFT → PUBLISHED`
- PUBLISHED → CONTESTED
- CONTESTED → PUBLISHED
- CONTESTED → HIDDEN
- HIDDEN/PUBLISHED → [*] apenas segundo política/retenção.

Guardas:
- Review só pode ser publicada para Engagement elegível;
- avaliação identifica perspectiva/autor/destinatário;
- contestação não apaga automaticamente a avaliação.

## 9. Consistência entre máquinas
- Proposal.ACCEPTED inicia Engagement.PENDING_AGREEMENT.
- AgreementVersion.ACCEPTED pode activar Engagement.
- Delivery record conduz ACTIVE → DELIVERED.
- Dispute pode sinalizar Engagement.IN_DISPUTE sem destruir o estado operacional anterior necessário para retoma.
- PaymentRecord.DISPUTED pode originar Dispute, mas pagamento e conflito continuam agregados distintos.
- Review torna-se elegível conforme regra da contratação; não é consequência automática de COMPLETED.

## 10. Representação na monografia
Recomenda-se **um diagrama de estados principal para Engagement**, porque concentra o ciclo de contratação, acompanhado por um quadro resumido dos estados de Opportunity, Proposal, AgreementVersion, PaymentRecord, Dispute e Review. Isto evita uma figura ilegível com seis máquinas concorrentes.

O diagrama principal deve mostrar:
PENDING_AGREEMENT → ACTIVE → DELIVERED → COMPLETED,
com CANCELLED e IN_DISPUTE como desvios, e nota de que pagamento possui ciclo independente.

## 11. Gate
**G-MODEL-STATE-UML: PASS.**
