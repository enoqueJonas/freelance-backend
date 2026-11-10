# ConecTA — professional profiles and reference review (backend)

Branch: `feat/conecta-profiles-evidence-review` (based on PR #10).
No authenticated frontend integration has yet been demonstrated.

## Profile API (RN01/RN03/RN04/RN15, RF03–RF06)

Authenticated users can own **both** a worker profile and an employer profile.
The API uses ownership from JWT; the selected UI role is not an authorization credential.

| Method | Path | Access |
|---|---|---|
| GET/POST/PATCH | `/api/accounts/me/worker/` | Owner |
| GET/POST/PATCH | `/api/accounts/me/employer/` | Owner |
| GET | `/api/accounts/workers/` | Public (no email/phone) |
| GET | `/api/accounts/workers/{id}/` | Public (no email/phone) |
| GET | `/api/accounts/employers/{id}/` | Public business metadata; private contact fields only to owner/staff |

Worker fields: `skills` (legacy comma-separated text; accepts a list on write),
`skills_list` (read-only list), `experience` (legacy text),
`title`, `bio`, `location`, `experience_years`,
`github_url`, `portfolio_url`. Location and prior experience are optional;
links are **self-declared**, not independently validated qualifications.

Employer fields: `company_name`, `address` (private, optional),
`contact_name` (private), `description`, `industry`, `location`,
`website_url`. Only public business fields are returned for unrelated users.

Example professional profile:

```json
{
  "skills": ["Django", "React", "PostgreSQL"],
  "title": "Desenvolvedora Web",
  "bio": "Desenvolvimento de interfaces e APIs.",
  "location": "Maputo",
  "experience_years": 3,
  "github_url": "https://github.com/example",
  "portfolio_url": "https://portfolio.example.test"
}
```

`skills` is stored as legacy string during this compatibility stage; the future
frontend adapter should use `skills_list` when reading. Job counts and ratings
must come from completed records/reviews—not client-supplied profile data.

## Reference-review API (NOT identity verification)

**Only metadata and public HTTPS reference URLs.** This is a documentary review
mechanism for portfolio links, declared certificates and organization references.
**Do not upload BI/passports, selfies, tax/financial data, KYC proofs or sensitive
personal information.** The service does not fetch evidence URLs.

| Method | Path | Permission |
|---|---|---|
| GET/POST | `/api/verification/reviews/` | Current user; own records/submissions |
| GET | `/api/verification/reviews/{id}/` | Owner or staff |
| GET | `/api/verification/reviews/pending/` | Staff only |
| POST | `/api/verification/reviews/{id}/decision/` | Staff excluding own submissions |

Submit a worker portfolio reference:

```json
{
  "profile_role": "worker",
  "kind": "PORTFOLIO",
  "description": "Projectos publicados que ilustram experiência em desenvolvimento web.",
  "reference_url": "https://portfolio.example.test/projects"
}
```

Valid evidence kinds are `PORTFOLIO`/`CERTIFICATE` for workers
and `BUSINESS_REFERENCE` for employers.

Review decision:

```json
{
  "decision": "REVIEWED",
  "note": "A referência foi analisada manualmente; não constitui validação legal de identidade."
}
```

Or `decision: "REJECTED"` with a reason. A decision is final for that
request; the owner may submit a new one after decision, while the previous
record remains available in history. At most one pending reference per profile
is enforced in the database. Reviewers cannot approve their own evidence.

**Review state semantics:**
- `PENDING`: metadata submitted for administrative review.
- `REVIEWED`: a reviewer recorded a documentary examination.
- `REJECTED`: reviewer declined the reference with explanation.

`REVIEWED` must **never** be mapped to the frontend `documentStatus=approved`
or displayed as an identity/qualification "Verified" badge. There is no
identity verification procedure, secure document storage, externally certified
qualification validation or financial KYC in this phase.

## Frontend integration gaps

- Frontend `WorkerProfile` uses `userId/title/bio/skills[]/experienceYears/
  githubLink/portfolioLink`; API uses `user_id/title/bio/skills_list/
  experience_years/github_url/portfolio_url`.
- Frontend `EmployerProfile` uses `companyName/contactName/industry/location/
  website`; API uses `company_name/contact_name/industry/location/website_url`.
- Backend does **not** populate `completedJobs`, `averageRating`, or
  `documentStatus` from trusted sources yet. Do not invent these values.
- Future BI/identity verification requires separate privacy/security design,
  private file storage, retention/deletion rules, audit, and minimum lawful purpose.
- Integration must call real endpoints under JWT and keep the mock disabled in
  any purportedly integrated environment.

## Tests

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test \
  apps.accounts.tests apps.accounts.test_profiles \
  apps.marketplace.tests apps.contracts.tests \
  apps.payments.tests apps.contracts.test_disputes \
  apps.verification.tests --verbosity 2
```

CI must report **at least 84 actually executed tests** and pass all checks.
This proves specified backend behavior in test fixtures, **not** full integration
or real-world identity validation.
