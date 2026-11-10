"""Evidence-review tests: reference handling, privacy and reviewer controls."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from .models import ProfileEvidenceReview

User = get_user_model()
PASSWORD = "Demo-Review-Account_987!"


class EvidenceReviewApiTests(APITestCase):
    def setUp(self):
        self.worker = User.objects.create_user(
            username="worker_v", name="Profissional Exemplo",
            email="worker@example.test", phone="+258841000001", password=PASSWORD,
        )
        self.employer = User.objects.create_user(
            username="employer_v", name="Empregador Exemplo",
            email="employer@example.test", phone="+258841000002", password=PASSWORD,
        )
        self.staff = User.objects.create_user(
            username="staff_v", name="Revisor Exemplo",
            email="staff@example.test", phone="+258841000003",
            password=PASSWORD, is_staff=True,
        )
        self.other = User.objects.create_user(
            username="other_v", name="Terceiro Exemplo",
            email="other@example.test", phone="+258841000004", password=PASSWORD,
        )
        self.wp = Worker.objects.create(
            user=self.worker, skills="Django", experience="2 anos"
        )
        self.ep = Employer.objects.create(
            user=self.employer, company_name="Empresa Exemplo", address=""
        )
        self.worker_payload = {
            "profile_role": "worker", "kind": "PORTFOLIO",
            "description": "Portefólio com projectos publicados pela profissional.",
            "reference_url": "https://portfolio.example.test/projects",
        }
        self.employer_payload = {
            "profile_role": "employer", "kind": "BUSINESS_REFERENCE",
            "description": "Website demonstrativo da organização contratante.",
            "reference_url": "https://company.example.test",
        }
        self.url = "/api/verification/reviews/"

    def submit_worker(self, user=None, payload=None):
        self.client.force_authenticate(user=user or self.worker)
        return self.client.post(self.url, payload or self.worker_payload, format="json")

    def test_anonymous_cannot_submit_or_read_evidence_reviews(self):
        self.assertEqual(self.client.post(
            self.url, self.worker_payload, format="json"
        ).status_code, 401)
        self.assertEqual(self.client.get(self.url).status_code, 401)

    def test_owner_creates_pending_worker_reference_without_identity_claim(self):
        response = self.submit_worker()
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["status"], "PENDING")
        self.assertEqual(response.data["submitted_by_user_id"], self.worker.id)
        self.assertEqual(response.data["worker_id"], self.wp.id)
        self.assertIsNone(response.data["employer_id"])
        self.assertIsNone(response.data["reviewed_at"])
        for key in ["identity_verified", "document_url", "verification_badge"]:
            self.assertNotIn(key, response.data)

    def test_business_reference_is_separate_from_worker_profile(self):
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(self.url, self.employer_payload, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["profile_role"], "employer")
        self.assertEqual(response.data["employer_id"], self.ep.id)
        self.assertIsNone(response.data["worker_id"])

    def test_user_cannot_submit_for_a_profile_they_do_not_hold(self):
        self.client.force_authenticate(user=self.other)
        result = self.client.post(self.url, self.worker_payload, format="json")
        self.assertEqual(result.status_code, 403)
        self.assertEqual(ProfileEvidenceReview.objects.count(), 0)

    def test_kind_and_reference_must_match_scope_and_public_https(self):
        for bad in [
            {**self.worker_payload, "kind": "BUSINESS_REFERENCE"},
            {**self.worker_payload, "reference_url": "http://example.test"},
            {**self.worker_payload, "reference_url": "https://localhost/resource"},
            {**self.worker_payload, "description": "curta"},
        ]:
            r = self.submit_worker(payload=bad)
            self.assertEqual(r.status_code, 400, (bad, r.data))
        self.assertEqual(ProfileEvidenceReview.objects.count(), 0)

    def test_only_one_pending_request_per_worker_even_after_duplicate_post(self):
        self.assertEqual(self.submit_worker().status_code, 201)
        self.assertEqual(self.submit_worker().status_code, 409)
        self.assertEqual(ProfileEvidenceReview.objects.count(), 1)

    def test_history_is_private_to_owner_and_staff(self):
        record = self.submit_worker().data
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.get(self.url).data, [])
        self.assertEqual(self.client.get(
            f"/api/verification/reviews/{record['id']}/"
        ).status_code, 404)
        self.client.force_authenticate(user=self.staff)
        queue = self.client.get("/api/verification/reviews/pending/")
        self.assertEqual(queue.status_code, 200)
        self.assertEqual(queue.data[0]["reference_url"], self.worker_payload["reference_url"])
        self.assertEqual(self.client.get(
            f"/api/verification/reviews/{record['id']}/"
        ).status_code, 200)
        self.client.force_authenticate(user=self.worker)
        self.assertEqual(len(self.client.get(self.url).data), 1)

    def test_non_staff_cannot_access_review_queue_or_make_decision(self):
        record = self.submit_worker().data
        self.client.force_authenticate(user=self.worker)
        self.assertEqual(self.client.get(
            "/api/verification/reviews/pending/"
        ).status_code, 403)
        self.assertEqual(self.client.post(
            f"/api/verification/reviews/{record['id']}/decision/",
            {"decision": "REVIEWED", "note": "A referência foi analisada."},
        ).status_code, 403)

    def test_staff_review_records_reviewer_time_and_reason_once(self):
        record = self.submit_worker().data
        self.client.force_authenticate(user=self.staff)
        path = f"/api/verification/reviews/{record['id']}/decision/"
        review = self.client.post(path, {
            "decision": "REVIEWED",
            "note": "Referência examinada manualmente, sem autenticação de identidade.",
        })
        self.assertEqual(review.status_code, 200, review.data)
        self.assertEqual(review.data["status"], "REVIEWED")
        self.assertEqual(review.data["reviewed_by_user_id"], self.staff.id)
        self.assertTrue(review.data["reviewed_at"])
        self.assertEqual(self.client.post(path, {
            "decision": "REJECTED", "note": "Tentativa repetida de decisão.",
        }).status_code, 409)
        self.assertEqual(self.client.get(
            "/api/verification/reviews/pending/"
        ).data, [])

    def test_rejected_reference_can_be_resubmitted_without_erasing_history(self):
        original = self.submit_worker().data
        self.client.force_authenticate(user=self.staff)
        rejected = self.client.post(
            f"/api/verification/reviews/{original['id']}/decision/",
            {
                "decision": "REJECTED",
                "note": "Referência não contém informação suficiente para análise.",
            },
        )
        self.assertEqual(rejected.status_code, 200)
        self.assertEqual(rejected.data["status"], "REJECTED")
        another = self.submit_worker()
        self.assertEqual(another.status_code, 201, another.data)
        self.assertEqual(ProfileEvidenceReview.objects.count(), 2)
        self.client.force_authenticate(user=self.worker)
        history = self.client.get(self.url)
        self.assertEqual(len(history.data), 2)

    def test_staff_cannot_review_own_reference(self):
        own_profile = Worker.objects.create(
            user=self.staff, skills="Python", experience="4 anos"
        )
        submitted = self.submit_worker(user=self.staff)
        self.assertEqual(submitted.status_code, 201, submitted.data)
        self.client.force_authenticate(user=self.staff)
        r = self.client.post(
            f"/api/verification/reviews/{submitted.data['id']}/decision/",
            {"decision": "REVIEWED", "note": "Auto-avaliação não permitida."},
        )
        self.assertEqual(r.status_code, 403)
        self.assertEqual(ProfileEvidenceReview.objects.get(
            id=submitted.data["id"]
        ).status, "PENDING")

    def test_database_refuses_review_associated_with_two_profiles(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ProfileEvidenceReview.objects.create(
                    worker=self.wp, employer=self.ep,
                    submitted_by=self.worker, kind="PORTFOLIO",
                    description="Ligação indevida a dois perfis.",
                    reference_url="https://example.test",
                )

    def test_cannot_forge_reviewer_or_approval_via_submission(self):
        result = self.submit_worker(payload={
            **self.worker_payload,
            "status": "REVIEWED",
            "reviewed_by_user_id": self.staff.id,
            "review_note": "Auto-aprovação indevida.",
            "worker_id": 999,
        })
        self.assertEqual(result.status_code, 201, result.data)
        self.assertEqual(result.data["status"], "PENDING")
        self.assertIsNone(result.data["reviewed_by_user_id"])
        self.assertEqual(result.data["worker_id"], self.wp.id)
