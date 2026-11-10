"""Rich profiles: role separation, compatibility, safe URLs and privacy."""
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()
PASSWORD = "Strong-Demo-Account_987!"


class RichProfileTests(APITestCase):
    def setUp(self):
        self.worker = User.objects.create_user(
            username="worker_demo", name="Ana Demo",
            email="ana@example.test", phone="+258841000001", password=PASSWORD,
        )
        self.owner = User.objects.create_user(
            username="owner_demo", name="Gestor Demo",
            email="owner@example.test", phone="+258841000002", password=PASSWORD,
        )
        self.other = User.objects.create_user(
            username="other_demo", name="Terceiro Demo",
            email="other@example.test", phone="+258841000003", password=PASSWORD,
        )

    def make_worker(self):
        self.client.force_authenticate(user=self.worker)
        result = self.client.post("/api/accounts/me/worker/", {
            "skills": ["Python", "Django", "React"],
            "title": "Programadora Web",
            "bio": "Criação de soluções de software e aplicações.",
            "location": "Maputo",
            "experience_years": 3,
            "github_url": "https://github.com/example",
            "portfolio_url": "https://portfolio.example.test",
        }, format="json")
        self.assertEqual(result.status_code, 201, result.data)
        return result.data

    def test_create_rich_worker_with_skills_array(self):
        data = self.make_worker()
        self.assertEqual(data["skills"], "Python, Django, React")
        self.assertEqual(data["skills_list"], ["Python", "Django", "React"])
        self.assertEqual(data["experience_years"], 3)
        self.assertEqual(data["experience"], "")

    def test_public_worker_excludes_private_contact_and_verification_claims(self):
        worker = self.make_worker()
        self.client.force_authenticate(user=None)
        result = self.client.get(f"/api/accounts/workers/{worker['id']}/")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data["name"], "Ana Demo")
        for field in ["email", "phone", "identity_verified", "document_url"]:
            self.assertNotIn(field, result.data)

    def test_legacy_skills_string_remains_supported(self):
        self.client.force_authenticate(user=self.worker)
        result = self.client.post("/api/accounts/me/worker/", {
            "skills": "PostgreSQL, Docker", "experience": "4 anos",
        })
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.data["skills_list"], ["PostgreSQL", "Docker"])

    def test_invalid_skills_and_portfolio_are_rejected(self):
        self.client.force_authenticate(user=self.worker)
        for data in [
            {"skills": ["React", "react"]},
            {"skills": ["Python"], "experience_years": 90},
            {"skills": ["Python"], "portfolio_url": "http://example.test"},
            {"skills": ["Python"], "portfolio_url": "https://localhost"},
            {"skills": ["Python"], "github_url": "https://other.example.test/x"},
        ]:
            result = self.client.post("/api/accounts/me/worker/", data, format="json")
            self.assertEqual(result.status_code, 400, (data, result.data))

    def test_only_owner_may_modify_professional_profile(self):
        self.make_worker()
        self.client.force_authenticate(user=self.other)
        result = self.client.patch("/api/accounts/me/worker/", {
            "title": "Not authorized",
        })
        self.assertEqual(result.status_code, 404)
        self.client.force_authenticate(user=self.worker)
        ok = self.client.patch("/api/accounts/me/worker/", {
            "title": "Backend Engineer",
        })
        self.assertEqual(ok.status_code, 200)
        self.assertEqual(ok.data["skills_list"], ["Python", "Django", "React"])

    def test_employer_profile_does_not_require_street_address(self):
        self.client.force_authenticate(user=self.owner)
        created = self.client.post("/api/accounts/me/employer/", {
            "company_name": "TI Exemplo", "industry": "Software",
            "location": "Maputo", "contact_name": "Responsável Interno",
        })
        self.assertEqual(created.status_code, 201, created.data)
        self.assertEqual(created.data["address"], "")
        self.assertEqual(created.data["industry"], "Software")

    def test_unrelated_accounts_cannot_see_private_employer_contacts(self):
        self.client.force_authenticate(user=self.owner)
        created = self.client.post("/api/accounts/me/employer/", {
            "company_name": "Consultoria Exemplo",
            "address": "Local particular de correspondência",
            "contact_name": "Contacto interno",
            "location": "Matola",
        })
        self.assertEqual(created.status_code, 201, created.data)
        self.client.force_authenticate(user=self.other)
        public = self.client.get(f"/api/accounts/employers/{created.data['id']}/")
        self.assertEqual(public.status_code, 200)
        self.assertEqual(public.data["location"], "Matola")
        for field in ["address", "contact_name", "employer_name", "email"]:
            self.assertNotIn(field, public.data)
        self.client.force_authenticate(user=self.owner)
        own = self.client.get(f"/api/accounts/employers/{created.data['id']}/")
        self.assertEqual(own.data["contact_name"], "Contacto interno")

    def test_employer_website_must_use_public_https(self):
        self.client.force_authenticate(user=self.owner)
        for url in ["http://example.test", "https://localhost/path"]:
            result = self.client.post("/api/accounts/me/employer/", {
                "company_name": "TI Exemplo", "website_url": url,
            })
            self.assertEqual(result.status_code, 400)

    def test_same_account_can_hold_both_profile_types(self):
        self.make_worker()
        created = self.client.post("/api/accounts/me/employer/", {
            "company_name": "Consultoria Individual", "location": "Maputo",
        })
        self.assertEqual(created.status_code, 201)
        current = self.client.get("/api/accounts/me/")
        self.assertEqual(current.data["roles"], ["worker", "employer"])

    def test_skills_filter_keeps_existing_api_behavior(self):
        self.make_worker()
        self.client.force_authenticate(user=None)
        yes = self.client.get("/api/accounts/workers/?skills=django")
        no = self.client.get("/api/accounts/workers/?skills=networking")
        self.assertEqual(len(yes.data), 1)
        self.assertEqual(len(no.data), 0)

    def test_frontend_cannot_appoint_itself_a_verification_status(self):
        self.make_worker()
        self.client.force_authenticate(user=self.worker)
        result = self.client.patch("/api/accounts/me/worker/", {
            "identity_verified": True,
            "title": "Developer",
            "user_id": self.other.id,
        }, format="json")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data["user_id"], self.worker.id)
        self.assertNotIn("identity_verified", result.data)
