# Arquitectura da Solução — ConecTA

## 1. Objectivo
A arquitectura deve suportar o protótipo web e preservar separação entre interface, coordenação de casos de uso, regras do domínio, persistência e serviços externos. É arquitectura-alvo; o backend/frontend existentes serão refactorizados incrementalmente.

## 2. Vista lógica

### Presentation
- React/TypeScript Web UI;
- formulários, navegação e apresentação;
- cliente HTTP/API;
- não decide transições de domínio.

### API/Application
- Django REST Framework;
- autenticação/autorização;
- validação de entrada;
- coordenação dos casos de uso: Profile/Verification, Opportunity, Proposal, Engagement/Agreement, Payment, Review/Dispute/Moderation.

### Domain
- entidades/agregados e invariantes;
- estados/transições;
- regras anti-self-contracting;
- versionamento do acordo;
- elegibilidade de review;
- limites de pagamento/moderação.

### Persistence
- Django ORM;
- PostgreSQL como alvo;
- transacções para alterações consistentes;
- ficheiros/evidências tratados com controlo de acesso quando aplicável.

### External Adapters
- PSP externo opcional;
- armazenamento/serviços auxiliares quando necessários;
- notificações como efeito auxiliar, não dependência para concluir a regra de negócio.

## 3. Vista de componentes

`Browser / React UI`
→ HTTPS/JSON
→ `Django REST API`
→ `Application/Domain modules`
→ `Django ORM`
→ `PostgreSQL`

Integrações opcionais:
`PaymentService → PSP Adapter → External Payment Provider`

Notificações:
`Domain/Application event → Notification mechanism` sem bloquear a transição principal.

## 4. Módulos de domínio recomendados

- accounts/profiles
- verification
- marketplace (opportunities/proposals)
- engagements (engagement/agreement/execution)
- payments
- reputation (reviews/contests)
- disputes/moderation

Os nomes físicos podem diferir. O importante é a separação de responsabilidades.

## 5. Segurança/autorização
- User é identidade autenticável;
- WorkerProfile e EmployerProfile concedem capacidades contextuais;
- autorização verifica actor + perfil/capacidade + relação com recurso;
- dados de verificação/evidência privada não são públicos por omissão;
- acções administrativas devem ser auditáveis;
- segredos/configuração não devem ser versionados no código.

## 6. Persistência e consistência
Operações como aceitar Proposal, activar Engagement, aceitar AgreementVersion e alterar estados relacionados devem ser atomicamente consistentes no backend. Histórico de AgreementVersion e acções auditáveis não deve ser sobrescrito.

## 7. Pagamentos
A arquitectura separa:
PaymentTerms (acordo) → PaymentRecord (estado) → PaymentTransaction (integração real opcional).
ConecTA não mantém carteira/saldo/custódia. PSP específico fica atrás de Adapter.

## 8. Implantação do protótipo

### Alvo lógico
- cliente: navegador web;
- frontend React servido estaticamente/CDN ou servidor web;
- backend Django/DRF;
- PostgreSQL;
- HTTPS;
- PSP externo apenas se RF20 entrar no incremento validado.

Não se afirma cloud/provider específico sem decisão de implementação.

## 9. Confronto AS-IS
Frontend actual é protótipo interactivo com mockApi/localStorage e não consome o backend de forma real. Backend possui accounts parcialmente funcional, verification parcial/divergente e grande parte dos restantes módulos como placeholders. Logo, a arquitectura-alvo exige integração real frontend↔API e implementação/refactor dos agregados antes de ser descrita como solução implementada.

## 10. Gate
**G-MODEL-ARCH: PASS.**
