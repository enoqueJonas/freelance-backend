# ConecTA — Backend ↔ Frontend Integration Contract (working draft)

**Status:** two separate backend PRs, no frontend API adapter yet. Back-end branch
`feat/conecta-backend-contracts-agreements` builds on
`feat/conecta-backend-foundation-auth-marketplace`.

## Implemented endpoints (real Django database)

| Action | Method/route | Authorization |
|---|---|---|
| Register | POST /api/accounts/auth/register/ | Public, password validators |
| Login | POST /api/auth/login/ | Public, credentials `username` (or email) + `password` |
| Refresh JWT | POST /api/auth/refresh/ | Refresh token |
| Current account | GET /api/accounts/me/ | Authenticated |
| Create/view/edit worker | POST/GET/PATCH /api/accounts/me/worker/ | Account owner |
| Create/view/edit employer | POST/GET/PATCH /api/accounts/me/employer/ | Account owner |
| List/search workers | GET /api/accounts/workers/ | Public |
| Opportunities | GET/POST /api/marketplace/offers/ | Public read; employer write |
| Own opportunities | GET /api/marketplace/offers/mine/ | Employer owner |
| Offer detail/edit | GET/PATCH /api/marketplace/offers/{id}/ | Public active read; owner edit |
| Close offer | POST /api/marketplace/offers/{id}/close/ | Owner |
| Submit/view proposals | POST/GET /api/marketplace/offers/{id}/proposals/ | Worker submit; employer read |
| Own proposals | GET /api/marketplace/proposals/mine/ | Worker owner |
| Accept proposal + create pending contract | POST /api/contracts/from-proposal/{proposal_id}/ | Offer employer |
| Own contracts | GET /api/contracts/mine/ | Either contracting party |
| Contract detail | GET /api/contracts/{contract_id}/ | Either contracting party |
| Versions | GET /api/contracts/{contract_id}/versions/ | Either party |
| Edit draft terms | PATCH /api/contracts/versions/{version_id}/ | Draft author |
| Submit for bilateral acceptance | POST /api/contracts/versions/{version_id}/submit/ | Draft author |
| Approve same published version | POST /api/contracts/versions/{version_id}/approve/ | Either party (once per role) |
| Reject version | POST /api/contracts/versions/{version_id}/reject/ | Either party; `reason` required |
| Propose amendment | POST /api/contracts/{contract_id}/amend/ | Either party; active contract |
| Renegotiate rejected initial agreement | POST /api/contracts/{contract_id}/renegotiate/ | Either party; pending contract |
| Complete service | POST /api/contracts/{contract_id}/complete/ | Employer, only when active |

## Contract and agreement state

```text
Offer.ACTIVE --[employer accepts proposal]--> Offer.CLOSED
                    |
                    +--> Contract.PENDING + AgreementVersion(1).DRAFT
DRAFT --[author submits validated terms]--> PENDING_APPROVAL
PENDING_APPROVAL --[both distinct parties approve]--> ACTIVE
PENDING_APPROVAL --[one party rejects]--> REJECTED
ACTIVE --[both approve v2]--> SUPERSEDED; v2 ACTIVE
Contract.ACTIVE --[employer completes]--> Contract.COMPLETED
```

All approval identities are derived from the JWT subject and contract foreign keys;
client-supplied `userId`, `role`, `status`, `signedBy...` are ignored/not writable.
The database enforces uniqueness of accepted worker proposals and agreement versions.

### Example: PATCH version draft

```json
{
  "terms": {
    "title": "Portal de serviços TI",
    "scope": "Construção de um portal com pesquisa, propostas e notificações.",
    "deliverables": "Código-fonte, documentação e demonstração funcional.",
    "acceptance_criteria": "Login, pesquisa e propostas validados nos casos acordados.",
    "budget": "23000.00",
    "start_date": "2026-11-11",
    "end_date": "2026-12-20",
    "payment_conditions": [
      {"id": "advance", "stage": "ADVANCE", "amount": "5000.00",
       "method": "M-Pesa", "moment": "Depois da aprovação bilateral"},
      {"id": "final", "stage": "FINAL", "amount": "18000.00",
       "method": "Transferência Bancária", "moment": "Após aceitação da entrega"}
    ]
  }
}
```

When POST `.../submit/` succeeds, terms are frozen for that version.
`/approve/` records user, role, timestamp and event. One approval is **not**
a signature/activation; both are required. This is **not a certified e-signature**.

## Frontend adaptation backlog — do NOT skip

1. **Credentials:** existing React `mockApi.auth.login(emailOrUsername)` does
   not take a password. Replace the login/register screens to use real
   credentials, errors and reset policy. Do not keep a passwordless fallback
   enabled alongside real API operations.
2. **Payloads:** backend uses snake_case (`required_skills`,
   `proposed_amount`, `timeline_days`, `acceptance_criteria`,
   `payment_conditions`); UI currently uses camelCase and different models.
   Introduce an explicitly tested `apiClient`/DTO mapper.
3. **Account profile fields:** Django `Worker.skills` is a string and the
   backend profile lacks the frontend's `title`, `bio`, `location`,
   portfolio evidence, verification status and rating. Add migrations and
   ownership-safe serializers before claiming profile parity.
4. **Role state:** backend accounts have no exclusive `role` column.
   Roles derive from existence of `Worker` and `Employer`; `role` in
   frontend must be a **display context only**, not an authorization token.
5. **Status handling:** server owns offer/proposal/contract status and
   agreement approvals; frontend must reload authoritative server state after
   mutations rather than writing `localStorage` directly.
6. **Finances and disputes:** Django payments/disputes/notifications remain
   scaffolding. **Do not connect the frontend payment/conflict UI to fictitious
   endpoints** or claim transaction or arbitration support.
7. **Identity, verification and audit:** client-supplied evidence and
   timestamps are not trusted. Implement secure uploads, ownership checks
   and server-side histories before storing real personal documents.
8. **Browser security:** CORS is allowlisted, not authorization.
   Use bearer JWT via HTTPS; design refresh/session handling carefully,
   avoid long-lived tokens in readable browser storage, and never log tokens.
9. **E2E evidence:** run worker and employer flows in separate browser contexts
   using synthetic accounts. Include forbidden actions (self proposal,
   outsider reading private contract, duplicate approval, modification of
   published versions) in API and browser acceptance tests.

## Next backend slices

- Profile richness and evidence, without overclaiming identity verification
- External payment declarations and confirmations (RN09/RN10), no custody
- Administrative dispute reporting/history (RN13/RF24/RF25), no arbitration
- Notifications/messaging/reviews backed by PostgreSQL (or SQLite in tests)
- Frontend API adapter and browser E2E tests

## Verification

CI runs Django check, committed migration drift check and **36 explicitly
discovered tests** on the contracts branch. The `master` branch was not
modified. No React/Django integration has yet been demonstrated.
