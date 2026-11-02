"""D50: API regression tests of the ACTUAL Django accounts endpoints.

These tests are designed to run with Django/DRF and a disposable test database.
They do not exercise the React mock or the unimplemented contracts domain.
"""
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from apps.accounts.models import Employer, Worker


User = get_user_model()
PASSWORD = "D50-test-pass-Only!123"


class AccountsApiRegressionTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="qa_worker",
            email="worker@example.test",
            password=PASSWORD,
            name="QA Worker",
            phone="+258841234567",
        )
        cls.other = User.objects.create_user(
            username="qa_other",
            email="other@example.test",
            password=PASSWORD,
            name="QA Other",
            phone="+258821234567",
        )
        cls.admin = User.objects.create_user(
            username="qa_staff",
            email="staff@example.test",
            password=PASSWORD,
            name="QA Staff",
            phone="+258831234567",
            is_staff=True,
        )

    def login_as(self, user):
        self.client.force_authenticate(user=user)

    def test_registration_normalizes_mozambican_phone(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            "/api/accounts/auth/register/",
            {
                "username": "qa_new",
                "name": "New Account",
                "email": "new@example.test",
                "phone": "84 123 4567",
                "password": PASSWORD,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created = User.objects.get(username="qa_new")
        self.assertEqual(created.phone, "+258841234567")
        self.assertNotIn("password", response.data)

    def test_registration_rejects_invalid_phone(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            "/api/accounts/auth/register/",
            {
                "username": "qa_bad_phone",
                "name": "Invalid Phone",
                "email": "badphone@example.test",
                "phone": "111",
                "password": PASSWORD,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("phone", response.data)
        self.assertFalse(User.objects.filter(username="qa_bad_phone").exists())

    def test_real_jwt_login_returns_tokens(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            "/api/auth/login/",
            {"username": "qa_worker", "password": PASSWORD},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_anonymous_cannot_read_private_me(self):
        response = self.client.get("/api/accounts/me/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anonymous_cannot_create_worker_profile(self):
        response = self.client.post(
            "/api/accounts/me/worker/",
            {"skills": "Python", "experience": "2 anos"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Worker.objects.count(), 0)

    def test_anonymous_cannot_create_employer_profile(self):
        response = self.client.post(
            "/api/accounts/me/employer/",
            {"company_name": "Empresa A", "address": "Maputo"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Employer.objects.count(), 0)

    def test_regular_user_cannot_enumerate_private_users(self):
        self.login_as(self.user)
        response = self.client.get("/api/accounts/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_can_list_users(self):
        self.login_as(self.admin)
        response = self.client.get("/api/accounts/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_regular_user_cannot_retrieve_other_user_details(self):
        self.login_as(self.user)
        response = self.client.get(f"/api/accounts/users/{self.other.pk}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_worker_profile_create_and_read(self):
        self.login_as(self.user)
        created = self.client.post(
            "/api/accounts/me/worker/",
            {"skills": "Python", "experience": "2 anos"},
            format="json",
        )
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        read = self.client.get("/api/accounts/me/worker/")
        self.assertEqual(read.status_code, status.HTTP_200_OK)
        self.assertEqual(read.data["skills"], "Python")
        self.assertEqual(Worker.objects.get(user=self.user).skills, "Python")

    def test_duplicate_worker_profile_rejected_with_400(self):
        self.login_as(self.user)
        payload = {"skills": "Python", "experience": "2 anos"}
        self.assertEqual(
            self.client.post("/api/accounts/me/worker/", payload, format="json").status_code,
            status.HTTP_201_CREATED,
        )
        repeated = self.client.post("/api/accounts/me/worker/", payload, format="json")
        self.assertEqual(repeated.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Worker.objects.filter(user=self.user).count(), 1)

    def test_worker_endpoint_is_scoped_to_authenticated_user(self):
        Worker.objects.create(user=self.other, skills="Java", experience="3 anos")
        self.login_as(self.user)
        response = self.client.get("/api/accounts/me/worker/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_one_account_can_have_both_profiles(self):
        self.login_as(self.user)
        worker = self.client.post(
            "/api/accounts/me/worker/",
            {"skills": "Python", "experience": "2 anos"},
            format="json",
        )
        employer = self.client.post(
            "/api/accounts/me/employer/",
            {"company_name": "Empresa A", "address": "Maputo"},
            format="json",
        )
        self.assertEqual(worker.status_code, status.HTTP_201_CREATED)
        self.assertEqual(employer.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Worker.objects.filter(user=self.user).exists())
        self.assertTrue(Employer.objects.filter(user=self.user).exists())
        self.assertEqual(self.client.get("/api/accounts/me/worker/").status_code, 200)
        self.assertEqual(self.client.get("/api/accounts/me/employer/").status_code, 200)

    def test_duplicate_employer_profile_rejected(self):
        self.login_as(self.user)
        payload = {"company_name": "Empresa A", "address": "Maputo"}
        self.assertEqual(
            self.client.post("/api/accounts/me/employer/", payload, format="json").status_code,
            status.HTTP_201_CREATED,
        )
        second = self.client.post("/api/accounts/me/employer/", payload, format="json")
        self.assertEqual(second.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employer.objects.filter(user=self.user).count(), 1)

    def test_staff_can_list_employers(self):
        Employer.objects.create(user=self.user, company_name="Empresa A", address="Maputo")
        self.login_as(self.admin)
        response = self.client.get("/api/accounts/employers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["company_name"], "Empresa A")
        self.assertEqual(response.data[0]["employer_name"], "QA Worker")

    def test_non_staff_cannot_list_employers(self):
        self.login_as(self.user)
        response = self.client.get("/api/accounts/employers/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_workers_list_requires_authentication(self):
        response = self.client.get("/api/accounts/workers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_workers_list_filters_skills(self):
        Worker.objects.create(user=self.user, skills="Python", experience="2 anos")
        Worker.objects.create(user=self.other, skills="Java", experience="3 anos")
        self.login_as(self.admin)
        response = self.client.get("/api/accounts/workers/?skills=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["skills"], "Python")


if __name__ == "__main__":
    import unittest
    unittest.main()
