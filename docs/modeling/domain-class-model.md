# Modelo Conceptual / Classes do Domínio — ConecTA

## 1. Princípio
Este é o modelo-alvo derivado de G-REQ e dos estados do domínio. Não descreve o backend actual como se já estivesse implementado. O AS-IS é confrontado separadamente.

## 2. Agregados
**Identity/Profile:** User, WorkerProfile, EmployerProfile, ProfessionalEvidence, VerificationCase.
**Marketplace:** Opportunity, Proposal.
**Engagement:** Engagement, AgreementVersion, ExecutionRecord.
**Payment:** PaymentTerms, PaymentRecord e, opcionalmente, PaymentTransaction.
**Reputation/Governance:** Review, ReviewContest, Dispute, DisputeEvidence, ModerationAction.

## 3. Classes e responsabilidades

| Classe | Responsabilidade principal |
|---|---|
| User | identidade, autenticação e estado da conta; não contém papel exclusivo worker/employer |
| WorkerProfile | informação profissional do utilizador enquanto prestador |
| EmployerProfile | informação do utilizador enquanto contratante |
| ProfessionalEvidence | evidência de competência: portfólio, projecto, referência, certificação, ligação externa ou outro tipo permitido |
| VerificationCase | pedido/estado/decisão de verificação proporcional de identidade/perfil |
| Opportunity | necessidade de serviço publicada por EmployerProfile e respectivo ciclo |
| Proposal | proposta de WorkerProfile para uma Opportunity |
| Engagement | agregado da contratação entre EmployerProfile e WorkerProfile |
| AgreementVersion | versão imutável das condições propostas/aceites da contratação |
| ExecutionRecord | registo relevante de execução, alteração factual, entrega ou confirmação |
| PaymentTerms | condições de pagamento associadas à versão vigente do acordo |
| PaymentRecord | registo do estado de cumprimento de uma obrigação/etapa de pagamento |
| PaymentTransaction | referência opcional à transacção efectuada por PSP externo |
| Review | avaliação bilateral contextualizada por Engagement |
| ReviewContest | contestação/moderação de uma Review |
| Dispute | conflito reportado no contexto de Engagement |
| DisputeEvidence | evidência associada ao conflito |
| ModerationAction | acção administrativa auditável sobre utilizador/oportunidade/verificação/review quando aplicável |

## 4. Cardinalidades essenciais

- User 1 — 0..1 WorkerProfile.
- User 1 — 0..1 EmployerProfile.
- WorkerProfile 1 — 0..* ProfessionalEvidence.
- User 1 — 0..* VerificationCase.
- EmployerProfile 1 — 0..* Opportunity.
- Opportunity 1 — 0..* Proposal.
- WorkerProfile 1 — 0..* Proposal.
- Proposal 0..1 — 0..1 Engagement como proposta seleccionada/origem.
- Engagement 1 — 1 EmployerProfile.
- Engagement 1 — 1 WorkerProfile.
- Engagement 1 — 1..* AgreementVersion.
- Engagement 1 — 0..* ExecutionRecord.
- AgreementVersion 1 — 0..* PaymentTerms.
- PaymentTerms 1 — 0..* PaymentRecord.
- PaymentRecord 1 — 0..1 PaymentTransaction.
- Engagement 1 — 0..2 Review, no máximo uma por perspectiva/parte quando elegível.
- Review 1 — 0..* ReviewContest.
- Engagement 1 — 0..* Dispute.
- Dispute 1 — 0..* DisputeEvidence.
- User/Admin 1 — 0..* ModerationAction como actor da acção.

## 5. Invariantes

1. User pode ter WorkerProfile, EmployerProfile ou ambos.
2. Engagement.worker.user != Engagement.employer.user.
3. Proposal.worker.user != Proposal.opportunity.employer.user.
4. Proposal só pode ser submetida a Opportunity OPEN.
5. Uma Proposal ACCEPTED pode originar no máximo um Engagement.
6. Engagement ACTIVE requer uma AgreementVersion ACCEPTED vigente.
7. AgreementVersion aceite não é sobrescrita; alteração cria nova versão.
8. PaymentTerms pertencem a condições acordadas, não a uma configuração global.
9. PaymentTransaction nunca representa fundos custodiados pela ConecTA.
10. Review exige Engagement elegível e identifica autor, destinatário/perspectiva e contexto.
11. Dispute não concede automaticamente autoridade arbitral ao administrador.
12. ModerationAction deve preservar actor, alvo, motivo, acção e data/hora.
13. Localização em Opportunity/Perfil é opcional/contextual, não requisito universal.
14. ProfessionalEvidence não possui tipo único obrigatório nem depende de Assessment.

## 6. Atributos conceptuais mínimos

**User:** id, name, email, phone, account_status, created_at.

**WorkerProfile:** id, user_id, headline/area, bio, experience_summary, location_optional.

**EmployerProfile:** id, user_id, display/company_name, description_optional, location_optional.

**ProfessionalEvidence:** id, worker_profile_id, type, title, description, reference/url/file, created_at.

**VerificationCase:** id, user_id, purpose, status, submitted_at, decided_at, decided_by, decision_reason.

**Opportunity:** id, employer_profile_id, title, description/scope, service_category, location_mode/location_optional, budget_or_price_optional, status, created_at.

**Proposal:** id, opportunity_id, worker_profile_id, proposed_scope, proposed_price_optional, proposed_deadline, message/conditions, status, created_at.

**Engagement:** id, opportunity_id, accepted_proposal_id, employer_profile_id, worker_profile_id, status, created_at, completed_at.

**AgreementVersion:** id, engagement_id, version, scope, deliverables_optional, deadline, other_terms_optional, status, proposed_by, proposed_at, accepted timestamps/actors.

**ExecutionRecord:** id, engagement_id, type, description/reference, created_by, created_at.

**PaymentTerms:** id, agreement_version_id, amount, method, due/milestone, sequence, conditions.

**PaymentRecord:** id, payment_terms_id, status, reported_by, reported_at, confirmed_at.

**PaymentTransaction:** id, payment_record_id, provider, external_reference, provider_status, occurred_at.

**Review:** id, engagement_id, author_user_id, subject_user_id, perspective, rating, comment, status, created_at.

**ReviewContest:** id, review_id, opened_by, reason, status, resolution_note, created_at.

**Dispute:** id, engagement_id, opened_by, category, description, status, created_at, closed_at.

**DisputeEvidence:** id, dispute_id, submitted_by, type, reference/file, description, created_at.

**ModerationAction:** id, actor_admin_id, target_type, target_id, action, reason, created_at.

## 7. Decisões de desenho

### Skill não é uma string única
O AS-IS usa Worker.skills como CharField. O modelo-alvo deve permitir estrutura adequada (por exemplo Skill/WorkerSkill) se pesquisa por competências fizer parte do protótipo final. A representação exacta é decisão de implementação, mas uma string única não deve limitar o modelo conceptual.

### VerificationCase substitui verificação exclusiva do empregador
O AS-IS Document está ligado OneToOne a Employer. Isso conflita com confiança bilateral e verificação proporcional. Documentos, se necessários, tornam-se evidências privadas de um VerificationCase, com finalidade e acesso definidos.

### Assessment sai do núcleo
O AS-IS possui Assessment OneToOne com Worker e aprovação automática por score >= 50. A baseline científica não suporta este gate universal; não pertence ao modelo-alvo principal.

### Contract/Signature evolui
Os placeholders Contract/Signature não devem determinar o domínio. Engagement + AgreementVersion representam formalização proporcional e versionamento.

### Messaging/Notifications
Não entram como entidades centrais. Podem ser componentes auxiliares/event-driven se forem necessários para RF15/RNF01, sem alterar o domínio científico.

## 8. Confronto AS-IS

| AS-IS backend | Situação | Modelo-alvo |
|---|---|---|
| User | parcialmente aproveitável | User sem role exclusivo |
| Worker OneToOne User | boa base | WorkerProfile acumulável |
| Employer OneToOne User | boa base | EmployerProfile acumulável |
| Worker.skills CharField | insuficiente para pesquisa/evidência rica | competências/evidências estruturáveis |
| Employer company/address | parcial | EmployerProfile contextual |
| Document OneToOne Employer | demasiado restritivo | VerificationCase + evidências privadas |
| Assessment Worker score >=50 | não suportado | retirar do núcleo |
| Offer/Proposal placeholders | por implementar | Opportunity/Proposal com estados |
| Contract/Signature placeholders | sem domínio real | Engagement/AgreementVersion |
| Payments app vazia | por implementar | Terms/Record/Transaction separados |
| Review placeholder | por implementar | Review bilateral/contextual |
| Dispute placeholder | por implementar | Dispute + Evidence |
| Messaging placeholders | não-core | auxiliar se necessário |
| Notifications vazia | não-core | auxiliar/eventos se necessário |

## 9. Diagrama textual de referência

User
- 0..1 WorkerProfile
  - 0..* ProfessionalEvidence
  - 0..* Proposal
- 0..1 EmployerProfile
  - 0..* Opportunity
    - 0..* Proposal

Accepted Proposal → Engagement
Engagement
- 1 WorkerProfile
- 1 EmployerProfile
- 1..* AgreementVersion
  - 0..* PaymentTerms
    - 0..* PaymentRecord
      - 0..1 PaymentTransaction
- 0..* ExecutionRecord
- 0..2 Review
  - 0..* ReviewContest
- 0..* Dispute
  - 0..* DisputeEvidence

## 10. Gate
**G-MODEL-CLASS: PASS.**

O modelo conceptual suporta a baseline de RF e os ciclos de estado sem depender das limitações do código actual. Próximo: diagramas de actividade dos fluxos representativos e, em seguida, sequências.
