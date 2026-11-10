"""Account regressions: credentials, privacy and independent contextual profiles."""
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()
PASSWORD = "Valid-Test-Password_374!"


class AccountApiTests(APITestCase):
    def create_account(self, suffix="1"):
        return User.objects.create_user(
            username=f"qa_{suffix}", name=f"Pessoa {suffix}",
            email=f"qa_{suffix}@example.test", phone=f"+25884100000{suffix}",
            password=PASSWORD,
        )

    def test_register_stores_hashed_password_and_normalized_phone(self):
        response = self.client.post("/api/accounts/auth/register/", {
            "username": "qa_new",
            "name": "Ana Teste",
            "email": "ANA.TESTE@EXAMPLE.TEST",
            "phone": "84 123 4567",
            "password": PASSWORD,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        user = User.objects.get(username="qa_new")
        self.assertNotEqual(user.password, PASSWORD)
        self.assertTrue(user.check_password(PASSWORD))
        self.assertEqual(user.phone, "+258841234567")
        self.assertEqual(user.email, "ana.teste@example.test")
        self.assertNotIn("password", response.data)
        self.assertEqual(response.data["roles"], [])

    def test_short_or_common_password_is_rejected(self):
        for pwd in ["1234567", "password123"]:
            response = self.client.post("/api/accounts/auth/register/", {
                "username": "weak_account",
                "name": "Pessoa Teste",
                "email": "weak@example.test",
                "phone": "841234567",
                "password": pwd,
            })
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username="weak_account").exists())

    def test_duplicate_case_insensitive_username_and_email_are_rejected(self):
        self.create_account("2")
        duplicate_email = self.client.post("/api/accounts/auth/register/", {
            "username": "other",
            "name": "Outra Pessoa",
            "email": "QA_2@EXAMPLE.TEST",
            "phone": "841234567",
            "password": PASSWORD,
        })
        self.assertEqual(duplicate_email.status_code, 400)
        duplicate_username = self.client.post("/api/accounts/auth/register/", {
            "username": "QA_2",
            "name": "Outra Pessoa",
            "email": "other@example.test",
            "phone": "841234567",
            "password": PASSWORD,
        })
        self.assertEqual(duplicate_username.status_code, 400)

    def test_invalid_phone_is_rejected(self):
        response = self.client.post("/api/accounts/auth/register/", {
            "username": "bad_phone",
            "name": "Pessoa Teste",
            "email": "bad@example.test",
            "phone": "999",
            "password": PASSWORD,
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("phone", response.data)

    def test_jwt_login_supports_username_or_email_and_rejects_bad_password(self):
        user = self.create_account("3")
        for identity in [user.username, user.email.upper()]:
            login = self.client.post("/api/auth/login/", {
                "username": identity,
                "password": PASSWORD,
            })
            self.assertEqual(login.status_code, 200, login.data)
            self.assertIn("access", login.data)
            self.assertIn("refresh", login.data)
        bad = self.client.post("/api/auth/login/", {
            "username": user.email, "password": "incorrect"
        })
        self.assertEqual(bad.status_code, 401)
        response = self.client.get("/api/accounts/me/")
        self.assertEqual(response.status_code, 401)
        login = self.client.post("/api/auth/login/", {
            "username": user.email, "password": PASSWORD
        })
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + login.data["access"])
        self.assertEqual(self.client.get("/api/accounts/me/").status_code, 200)

    def test_same_user_can_create_both_profiles_but_cannot_duplicate_either(self):
        user = self.create_account("4")
        self.client.force_authenticate(user=user)
        worker = self.client.post("/api/accounts/me/worker/", {
            "skills": "Python, Django", "experience": "3 anos"
        })
        self.assertEqual(worker.status_code, 201, worker.data)
        self.assertEqual(worker.data["user_id"], user.id)
        employer = self.client.post("/api/accounts/me/employer/", {
            "company_name": "TI Exemplo", "address": "Maputo"
        })
        self.assertEqual(employer.status_code, 201, employer.data)
        self.assertEqual(employer.data["user_id"], user.id)
        profile = self.client.get("/api/accounts/me/")
        self.assertEqual(profile.status_code, 200)
        self.assertEqual(profile.data["roles"], ["worker", "employer"])
        self.assertEqual(self.client.get("/api/accounts/me/worker/").status_code, 200)
        self.assertEqual(self.client.get("/api/accounts/me/employer/").status_code, 200)
        self.assertEqual(self.client.post("/api/accounts/me/worker/", {
            "skills": "New", "experience": "10"
        }).status_code, 409)
        self.assertEqual(self.client.post("/api/accounts/me/employer/", {
            "company_name": "Duplicate", "address": "Maputo"
        }).status_code, 409)

    def test_update_profile_can_only_modify_own_profile(self):
        a = self.create_account("5")
        b = self.create_account("6")
        self.client.force_authenticate(user=a)
        self.client.post("/api/accounts/me/worker/", {
            "skills": "SQL", "experience": "2"
        })
        self.client.force_authenticate(user=b)
        response = self.client.patch("/api/accounts/me/worker/", {
            "skills": "changed"
        })
        self.assertEqual(response.status_code, 404)
        self.client.force_authenticate(user=a)
        edited = self.client.patch("/api/accounts/me/worker/", {
            "skills": "PostgreSQL"
        })
        self.assertEqual(edited.status_code, 200)
        self.assertEqual(edited.data["skills"], "PostgreSQL")

    def test_private_user_directory_requires_admin(self):
        user = self.create_account("7")
        self.assertEqual(self.client.get("/api/accounts/users/").status_code, 401)
        self.client.force_authenticate(user=user)
        self.assertEqual(self.client.get("/api/accounts/users/").status_code, 403)
        self.assertEqual(self.client.get(f"/api/accounts/users/{user.pk}/").status_code, 403)
        admin = User.objects.create_superuser(
            username="qa_admin", email="admin@example.test", password=PASSWORD,
            name="Admin Teste", phone="+258841000008",
        )
        self.client.force_authenticate(user=admin)
        self.assertEqual(self.client.get("/api/accounts/users/").status_code, 200)

    def test_public_worker_card_hides_contacts_and_passwords(self):
        user = self.create_account("8")
        self.client.force_authenticate(user=user)
        profile = self.client.post("/api/accounts/me/worker/", {
            "skills": "Python", "experience": "1 ano"
        }).data
        self.client.force_authenticate(user=None)
        response = self.client.get(f"/api/accounts/workers/{profile['id']}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], user.name)
        self.assertNotIn("email", response.data)
        self.assertNotIn("phone", response.data)
        self.assertNotIn("password", response.data)

    def test_browser_cors_is_limited_to_allowlisted_origins(self):
        allowed = self.client.options(
            "/api/accounts/workers/",
            HTTP_ORIGIN="http://localhost:3000",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="GET",
        )
        # Origins come from the explicit CORS_ALLOWED_ORIGINS setting; check actual
        # configured origin only when present (CI uses the same allowlist).
        from django.conf import settings
        if "http://localhost:3000" in settings.CORS_ALLOWED_ORIGINS:
            self.assertEqual(
                allowed.headers.get("Access-Control-Allow-Origin"),
                "http://localhost:3000",
            )
        forbidden = self.client.options(
            "/api/accounts/workers/",
            HTTP_ORIGIN="https://untrusted.example.test",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="GET",
        )
        self.assertNotIn("Access-Control-Allow-Origin", forbidden.headers)
