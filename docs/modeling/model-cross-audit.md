# Auditoria Cruzada da Modelação — ConecTA

## 1. Objectivo
Verificar que requisitos finais possuem representação suficiente na modelação e que nenhuma funcionalidade central foi introduzida sem requisito.

## 2. Cobertura por macro requisito

| Macro requisito | RF | Casos de uso | Classes/agregados | Actividade/Sequência | Estados |
|---|---|---|---|---|---|
| Conta/perfis/confiança | RF01–RF06 | UC01–UC06 | User, WorkerProfile, EmployerProfile, ProfessionalEvidence, VerificationCase | fluxo simples; sem diagrama dedicado | VerificationCase a detalhar na implementação se necessário |
| Descoberta/oportunidades | RF07–RF10 | UC07–UC10 | Opportunity, profiles | DA01 / DS01 | Opportunity |
| Proposta/negociação/acordo | RF11–RF14 | UC11–UC14 | Proposal, Engagement, AgreementVersion | DA01–DA02 / DS01–DS02 | Proposal, Engagement, AgreementVersion |
| Execução/rastreabilidade | RF15–RF17 | UC15–UC17 | Engagement, ExecutionRecord | DA02–DA03 / DS02–DS03 | Engagement |
| Pagamento | RF18–RF20 | UC18–UC20 | PaymentTerms, PaymentRecord, PaymentTransaction | DA03 / DS03 | PaymentRecord |
| Reputação/conflitos | RF21–RF25 | UC21–UC25 | Review, ReviewContest, Dispute, Evidence | DA04/DS04 para conflitos; reviews cobertos por UC/classes | Review, Dispute |
| Governação | RF26–RF28 | UC26–UC27 + UC06 | ModerationAction, VerificationCase | DA04/DS04 parcialmente | estados dos alvos + Dispute |

## 3. Verificação RF → modelo
- RF01–RF06: cobertos por actores/UC e classes. Não exigem diagramas de actividade próprios para provar CRUD.
- RF07–RF20: cobertura forte ponta-a-ponta em UC, classes, actividades, sequências e estados.
- RF21–RF23: Review/ReviewContest + UC21–UC23 + máquina Review; suficiente sem sequência dedicada.
- RF24–RF25: cobertura completa em DA04/DS04/Dispute.
- RF26–RF28: governação coberta por actor Admin, UC, ModerationAction/VerificationCase e pontos administrativos; não implica arbitragem.

## 4. Verificação inversa — modelo → requisito
Todos os elementos centrais possuem origem:
- ProfessionalEvidence ← RF05/N02;
- VerificationCase ← RF06/RF28/N03;
- Opportunity ← RF07–RF10;
- Proposal ← RF11–RF12;
- Engagement/AgreementVersion ← RF13–RF17;
- ExecutionRecord ← RF15–RF17;
- PaymentTerms/Record/Transaction ← RF18–RF20;
- Review/Contest ← RF21–RF23;
- Dispute/Evidence ← RF24–RF25/N14;
- ModerationAction ← RF26–RF28/RN16.

Não foram promovidos a domínio central Assessment, escrow, advanced signature, algorithmic matching, universal geolocation, realtime chat ou notification.

## 5. Consistência entre artefactos
- papéis acumuláveis: consistente em actores, User/profiles e autorização;
- anti-self-contracting: consistente em RN, classe, DA01 e DS01;
- formalização proporcional: consistente em AgreementVersion e ausência de assinatura obrigatória;
- versionamento: consistente em RNF04, DA02, DS02 e estados;
- pagamento sem custódia: consistente em classes, DA03, DS03 e arquitectura;
- conflitos sem arbitragem: consistente em Dispute, DA04, DS04 e arquitectura;
- chat/notificações: auxiliares, não requisitos centrais.

## 6. Lacunas intencionais
- atributos finais/constraints de VerificationCase dependem do fluxo de verificação que efectivamente for implementado;
- RF20 é Could e PSP não é necessário para validar o núcleo;
- critérios quantitativos de performance/availability não existem porque não foram fundamentados;
- detalhes físicos de deployment serão fechados quando o protótipo integrado for implementado.

Estas lacunas não impedem a modelação do núcleo.

## 7. Gate final
**G-MODEL: PASS.**

A modelação está suficientemente coerente para orientar implementação e posterior escrita da secção de especificação/modelação da monografia.

Próximo macro-passo: **implementação/refactor do protótipo contra a baseline**, seguida de testes/validação. Antes de alterar código, deve ser criado um plano de migração AS-IS → TO-BE para evitar reescrita desnecessária.
