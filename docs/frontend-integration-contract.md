# ConecTA — Backend ↔ Frontend Integration Contract (working draft)

**Status:** staged backend branches (PR #8 → #9 → #10 → profile/evidence).
The React frontend has not been connected to the API. See
[profile/evidence API](profile-evidence-api.md) and
[external payments/disputes API](payment-dispute-api.md).

## Implemented endpoints (real Django database)

| Action | Method/route | Authorization |
|---|---|---|
| Register | POST /api/accounts/auth/register/ | Public, password validators |
| Login | POST /api/auth/login/ | Public, credentials `username` (or email) + `password` |
| Refresh JWT | POST /api/auth/refresh/ | Refresh token |
| Current account | GET /api/accounts/me/ | Authenticated |
| Create/view/edit worker | POST/GET/PATCH /api/accounts/me/worker/ | Account owner |
| Create/view/edit employer | POST/GET/PATCH /api/accounts/me/employer/ | Account owner |
| Business detail | GET /api/accounts/employers/{id}/ | Public safe subset; owner/staff see contact |
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
3. **Account profile fields:** worker and employer public metadata now exist,
   including biography, location, portfolio URLs and industry. Legacy
   `Worker.skills` is still stored as text; `skills_list` is provided
   for a typed frontend adapter. Trusted ratings/completed-job aggregates,
   legal identity verification and secure document uploads **do not yet exist**.
   Do not transform documentary `REVIEWED` into an identity verified badge.
4. **Role state:** backend accounts have no exclusive `role` column.
   Roles derive from existence of `Worker` and `Employer`; `role` in
   frontend must be a **display context only**, not an authorization token.
5. **Status handling:** server owns offer/proposal/contract status and
   agreement approvals; frontend must reload authoritative server state after
   mutations rather than writing `localStorage` directly.
6. **Finances and disputes:** payment declaration and dispute follow-up
   endpoints now exist on the `feat/conecta-backend-payments-disputes`
   branch. Connect through DTO mappers and JWT-aware service adapters.
   Never claim actual transfer, escrow, bank confirmation or binding arbitration.
   See [API details](payment-dispute-api.md).
7. **Evidence reviews:** the backend can collect private metadata/HTTPS
   references for portfolio, declared certificates and organisations;
   administrative decisions include reviewer, timestamp and reason.
   This is **not** legal identity verification or qualified certification.
   Never send BI/passport scans or financial KYC through this API.
8. **Browser security:** CORS is allowlisted, not authorization.
   Use bearer JWT via HTTPS; design refresh/session handling carefully,
   avoid long-lived tokens in readable browser storage, and never log tokens.
9. **E2E evidence:** run worker and employer flows in separate browser contexts
   using synthetic accounts. Include forbidden actions (self proposal,
   outsider reading private contract, duplicate approval, modification of
   published versions) in API and browser acceptance tests.

## Next backend slices

- Real identity-verification design (private storage, consent, retention and deletion), if required
- Trusted ratings/completed-job aggregation and messaging/notifications, with ownership checks
- Frontend API adapter and browser E2E tests

## Verification

CI in the profiles/evidence branch requires **84 explicitly
discovered tests**, Django checks and committed migration checks, including
ownership and privacy tests for employer/worker data and staff evidence review.
A passing test suite is **not** evidence of legal identity verification or
React/Django end-to-end integration. The `master` branch is unmodified.
