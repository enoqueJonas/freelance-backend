# ConecTA — Django Backend

This repository is the **backend prototype** for connecting independent IT
workers and employers in Maputo. The main branch originally contained mostly
scaffolding. Build changes are staged in pull requests rather than pushed to
`master`.

## Environment

Requires Python 3.12+ and Django 6.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit DJANGO_SECRET_KEY; never use the placeholder in production.
python manage.py migrate
python manage.py runserver
```

The default developer database is SQLite; set `DATABASE_URL` for PostgreSQL.
Do not commit `.env`, user data or database files. A previously committed
development secret and database must be treated as compromised and replaced.
Only run with `DJANGO_DEBUG=1` locally. A real deployment needs trusted hosts,
HTTPS and secure cookie/proxy configuration.

## Implemented backend foundation (this branch)

- Real password-validated user registration, hashed passwords and JWT login.
- Both worker and employer profiles on the **same** account.
- JWT-protected account self-service and ownership-guarded profile changes.
- Public worker catalogue without private email or phone fields.
- Persistent opportunities and proposals.
- Owner-controlled publication, editing and closure; applicants cannot edit offers.
- RN02: no proposal to an opportunity published by the **same user**, even if
  that account has both profiles.
- Unique proposals per worker and offer, positive budget and timeline checks.
- Explicit, origin-allowlisted CORS to permit later React integration.

**Not implemented yet:** contract creation from accepted proposals, bilateral
agreement versions, evidence/uploads, payment declarations and dispute workflow.
These still require server-side APIs, models, migrations and tests **before**
removing the `mockApi` from the frontend.

## API endpoints

| Method | Route | Access |
|---|---|---|
| POST | `/api/accounts/auth/register/` | Public |
| POST | `/api/auth/login/` | Public; JSON `username`, `password`; username or email |
| POST | `/api/auth/refresh/` | Refresh token |
| GET | `/api/accounts/me/` | JWT required |
| GET/POST/PATCH | `/api/accounts/me/worker/` | Own worker profile |
| GET/POST/PATCH | `/api/accounts/me/employer/` | Own employer profile |
| GET | `/api/accounts/workers/` | Public |
| GET | `/api/accounts/workers/{id}/` | Public |
| GET | `/api/accounts/users/` | Admin only |
| GET | `/api/marketplace/offers/` | Public, active offers |
| POST | `/api/marketplace/offers/` | JWT + employer profile |
| GET | `/api/marketplace/offers/mine/` | JWT; own offers |
| GET/PATCH | `/api/marketplace/offers/{id}/` | Public active detail; PATCH owner only |
| POST | `/api/marketplace/offers/{id}/close/` | Owner |
| GET | `/api/marketplace/offers/{id}/proposals/` | Owner/admin |
| POST | `/api/marketplace/offers/{id}/proposals/` | Worker profile, not own offer |
| GET | `/api/marketplace/proposals/mine/` | Own proposals |

JWT login returns `access` and `refresh`. Use
`Authorization: Bearer <access>` when calling authenticated endpoints.
Do not store tokens in public screenshots, repos or logs.

Example register:
```json
{
  "username": "ana_demo",
  "name": "Ana Exemplo",
  "email": "ana@example.test",
  "phone": "841234567",
  "password": "choose-a-strong-unique-password"
}
```

Example offer:
```json
{
  "title": "Desenvolvimento de portal",
  "description": "Criar um portal para uma empresa com autenticação e relatórios.",
  "category": "Desenvolvimento Web",
  "required_skills": ["Django", "React"],
  "budget": "25000.00",
  "location": "Maputo"
}
```

Example proposal:
```json
{
  "description": "Implementarei a solução em duas fases com demonstração final.",
  "proposed_amount": "23000.00",
  "timeline_days": 21
}
```

## Quality gates

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test --verbosity 2
```

Until backend contract/payments/disputes endpoints are finished, the
frontend remains a separate **demonstration** using localStorage. A successful
Django test suite does not establish end-to-end integration, production
security or empirical acceptance for the monograph.
