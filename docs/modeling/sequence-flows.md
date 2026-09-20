# Fluxos de Sequência Representativos — ConecTA

## 1. Princípio

Os diagramas de sequência são derivados dos quatro fluxos de actividade aprovados. O objectivo é mostrar responsabilidades e colaboração entre camadas, sem fingir que a arquitectura-alvo já está implementada no backend actual.

Participantes lógicos:
- **Actor** — Trabalhador, Empregador ou Administrador;
- **UI/API Boundary** — interface web/API;
- **Application Service** — coordena o caso de uso;
- **Domain** — entidades/agregados e regras;
- **Repository** — persistência;
- **PSP Adapter** — apenas na integração opcional de pagamento.

A autorização deve usar capacidades/perfis e relação com o recurso, não um role global mutuamente exclusivo.

---

## 2. DS01 — Publicar oportunidade e seleccionar proposta

### Participantes
Empregador → UI/API → OpportunityService → OpportunityRepository  
Trabalhador → UI/API → ProposalService → OpportunityRepository / ProposalRepository  
Empregador → UI/API → ProposalService → EngagementService → Repositories

### Sequência — publicar oportunidade
1. Empregador → UI/API: solicitar criação/publicação.
2. UI/API → OpportunityService: createOpportunity(actor, data).
3. OpportunityService → Domain: validar capacidade EmployerProfile e dados.
4. Domain → OpportunityService: Opportunity(DRAFT).
5. OpportunityService → OpportunityRepository: save(DRAFT).
6. Empregador → UI/API: publish(opportunityId).
7. UI/API → OpportunityService: publish(actor, id).
8. OpportunityService → OpportunityRepository: get(id).
9. OpportunityService → Domain Opportunity: publish(actor).
10. Domain valida autoria/estado e muda DRAFT → OPEN.
11. OpportunityService → OpportunityRepository: save(OPEN).
12. UI/API ← OpportunityService: oportunidade publicada.

### Sequência — submeter proposta
13. Trabalhador → UI/API: submitProposal(opportunityId, data).
14. UI/API → ProposalService.
15. ProposalService → OpportunityRepository: get(opportunityId).
16. ProposalService → Domain: validar Opportunity OPEN, WorkerProfile e regra anti-self-contracting.
17. **alt inválido:** devolver erro sem persistir Proposal.
18. **else válido:** Domain cria Proposal SUBMITTED.
19. ProposalService → ProposalRepository: save(proposal).
20. UI/API ← ProposalService: proposta submetida.

### Sequência — aceitar proposta
21. Empregador → UI/API: acceptProposal(proposalId).
22. UI/API → ProposalService.
23. ProposalService → ProposalRepository: get(proposalId).
24. ProposalService → OpportunityRepository: get(proposal.opportunity).
25. Domain valida autoria do empregador e estado SUBMITTED.
26. Domain: Proposal SUBMITTED → ACCEPTED.
27. ProposalService → ProposalRepository: save.
28. ProposalService → EngagementService: startFromAcceptedProposal(proposal).
29. EngagementService → Domain: criar Engagement PENDING_AGREEMENT.
30. EngagementService → EngagementRepository: save.
31. UI/API ← serviços: proposta aceite / contratação iniciada.

**RF:** RF07–RF12.  
**Invariantes críticas:** Opportunity OPEN; autor != proponente; apenas empregador proprietário aceita.

---

## 3. DS02 — Formalizar e alterar condições

### Participantes
Trabalhador/Empregador → UI/API → AgreementService → EngagementRepository / AgreementRepository

### Sequência — acordo inicial
1. Parte → UI/API: proposeAgreement(engagementId, conditions).
2. UI/API → AgreementService.
3. AgreementService → EngagementRepository: get(engagementId).
4. Domain valida que actor é parte do Engagement e estado = PENDING_AGREEMENT.
5. AgreementService → Domain: createVersion(v1, conditions, proposedBy).
6. Domain cria AgreementVersion PROPOSED.
7. AgreementService → AgreementRepository: save(v1).
8. Contraparte → UI/API: acceptAgreement(versionId).
9. UI/API → AgreementService.
10. AgreementService → AgreementRepository: get(versionId).
11. Domain valida contraparte/elegibilidade e regista aceitação.
12. **alt faltam aceitações:** persistir e manter PENDING_AGREEMENT.
13. **else condições aceites:** AgreementVersion → ACCEPTED; Engagement → ACTIVE.
14. AgreementService → AgreementRepository: save.
15. AgreementService → EngagementRepository: save.
16. UI/API ← AgreementService: acordo vigente.

### Sequência — alteração
17. Parte → UI/API: proposeChange(engagementId, changedConditions).
18. AgreementService obtém Engagement ACTIVE e versão vigente.
19. Domain cria AgreementVersion vN+1 PROPOSED a partir da versão vigente + alterações.
20. AgreementRepository: save(newVersion); versão anterior permanece intacta.
21. Contraparte → UI/API: accept/reject(newVersion).
22. AgreementService carrega nova versão.
23. **alt rejeita:** newVersion → REJECTED; versão anterior continua vigente.
24. **else aceita:** newVersion → ACCEPTED; passa a ser vigente; versão anterior permanece histórica.
25. Repositories persistem estados.
26. UI/API recebe resultado.

**RF:** RF13, RF14, RF17, RF18.  
**RNF:** RNF04.  
**Regra arquitectural:** versionamento é responsabilidade do domínio, não da UI.

---

## 4. DS03 — Entrega e pagamento

### Participantes
Trabalhador → UI/API → EngagementService → EngagementRepository / ExecutionRepository  
Empregador → UI/API → EngagementService  
Partes → PaymentService → PaymentRepositories → PSPAdapter (opcional)

### Sequência — entrega
1. Trabalhador → UI/API: registerDelivery(engagementId, evidence/data).
2. UI/API → EngagementService.
3. EngagementService → EngagementRepository: get.
4. Domain valida actor, Engagement ACTIVE e acordo vigente.
5. Domain cria ExecutionRecord(type=DELIVERY, author, timestamp).
6. Domain muda Engagement ACTIVE → DELIVERED.
7. ExecutionRepository: save(record).
8. EngagementRepository: save(DELIVERED).
9. Empregador → UI/API: confirmCompletion(engagementId).
10. EngagementService carrega Engagement.
11. **alt problema material:** não conclui; pode iniciar alteração ou Dispute.
12. **else aceite:** Domain DELIVERED → COMPLETED; repository save.

### Sequência — registo manual/externo do pagamento
13. Parte autorizada → UI/API: reportPayment(paymentTermsId, data).
14. UI/API → PaymentService.
15. PaymentService carrega PaymentTerms e Engagement relacionado.
16. Domain valida actor e condições.
17. Domain cria/actualiza PaymentRecord → REPORTED_PAID.
18. PaymentRepository: save.
19. Contraparte → UI/API: confirmPayment(paymentRecordId).
20. PaymentService → Domain: REPORTED_PAID → CONFIRMED.
21. PaymentRepository: save.

### Sequência opcional — PSP
22. Parte → UI/API: initiateExternalPayment(paymentTermsId).
23. PaymentService valida RF20/configuração.
24. PaymentService → PSPAdapter: initiate(payment data).
25. PSPAdapter → PSP externo: request.
26. PSP externo → PSPAdapter: externalReference/status.
27. PSPAdapter → PaymentService.
28. PaymentService cria/actualiza PaymentTransaction e PaymentRecord.
29. **alt falha:** PaymentRecord → FAILED.
30. **else confirmação fiável:** PaymentRecord → CONFIRMED.
31. Repository: save.

**RF:** RF15–RF20.  
**Limite:** PaymentService não mantém saldo nem custódia; PSPAdapter isola o domínio do fornecedor.

---

## 5. DS04 — Reportar e acompanhar conflito

### Participantes
Trabalhador/Empregador → UI/API → DisputeService → EngagementRepository / DisputeRepository  
Administrador → UI/API → DisputeService / ModerationService → Repositories

### Sequência
1. Parte → UI/API: reportDispute(engagementId, category, description, evidence).
2. UI/API → DisputeService.
3. DisputeService → EngagementRepository: get.
4. Domain valida que actor participa no Engagement.
5. Domain cria Dispute OPEN.
6. Para cada evidência válida, cria DisputeEvidence associada.
7. DisputeRepository: save(dispute/evidence).
8. Quando aplicável, EngagementService/Domain sinaliza Engagement IN_DISPUTE ou PaymentRecord DISPUTED sem destruir estado/histórico anterior.
9. Administrador → UI/API: reviewDispute(disputeId).
10. UI/API → DisputeService.
11. DisputeService → DisputeRepository: get.
12. Domain valida capacidade administrativa.
13. Dispute OPEN → UNDER_REVIEW.
14. **alt informação insuficiente:** UNDER_REVIEW → WAITING_INFORMATION; regista pedido.
15. Parte → UI/API: submitEvidence(disputeId, evidence).
16. DisputeService valida participação e associa evidência.
17. WAITING_INFORMATION → UNDER_REVIEW.
18. Administrador → UI/API: closeDispute(outcome, note).
19. **alt resolução registada:** Dispute → RESOLVED.
20. **else encerramento administrativo:** Dispute → CLOSED.
21. Moderation/Dispute service regista actor, motivo/nota e timestamp.
22. Repositories persistem histórico.
23. Estado operacional do Engagement é restaurado/encerrado conforme regra válida, sem inferir decisão jurídica automática.

**RF:** RF17, RF24–RF27.  
**Limite:** administrador acompanha e aplica políticas; não arbitra juridicamente a prestação.

---

## 6. Padrões arquitecturais revelados pelas sequências

As sequências indicam uma arquitectura coerente para o protótipo:

**Presentation/API → Application Services → Domain → Repositories/Adapters**

### Serviços de aplicação candidatos
- OpportunityService
- ProposalService
- EngagementService
- AgreementService
- PaymentService
- DisputeService
- ModerationService
- Profile/VerificationService

Estes nomes são responsabilidades lógicas; não obrigam a criar uma classe Django Service para cada item se uma implementação mais simples preservar as mesmas fronteiras.

### Repositories
Nos diagramas são abstrações de persistência. Em Django, ORM/model managers podem cumprir esta responsabilidade. Não é necessário introduzir repository pattern artificial apenas para fazer o código parecer com o diagrama.

### Eventos auxiliares
Transições como ProposalAccepted, AgreementAccepted, DeliveryRegistered, PaymentConfirmed e DisputeOpened podem futuramente disparar notificações. Notification não participa da decisão central e não deve bloquear a transição.

---

## 7. Relação com o backend actual

O backend actual não possui ainda estas interacções completas:
- marketplace Offer/Proposal são placeholders;
- contracts Contract/Dispute/Signature estão vazios;
- payments/reviews/messaging/notifications estão essencialmente vazios;
- accounts é a área mais implementada;
- verification contém Document e Assessment, mas a semântica diverge da baseline.

Logo, estes diagramas representam **arquitectura/modelo-alvo do protótipo reconstruído**, e não documentação AS-IS.

---

## 8. Gate

**G-MODEL-SEQUENCE: PASS.**

Os quatro fluxos de sequência são coerentes com casos de uso, actividades, estados e modelo conceptual. Próximo passo: consolidar o modelo de estados em representação UML e definir a arquitectura lógica/física da solução; depois efectuar auditoria cruzada de toda a modelação para fechar **G-MODEL**.
