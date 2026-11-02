"""D53: real API read-model authorization tests for the React integration."""
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.contracts.models import Engagement
from apps.marketplace.models import Opportunity, Proposal

User = get_user_model()


class UIReadModelTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        def make(username, phone):
            return User.objects.create_user(
                username=username, email=username + "@example.test",
                name=username, phone=phone, password="TestOnly123!D53"
            )
        cls.employer = make("owner_d53", "+258841234567")
        cls.worker = make("worker_d53", "+258821234567")
        cls.other = make("other_d53", "+258831234567")
        employer = Employer.objects.create(
            user=cls.employer, company_name="D53 Labs", address="Maputo"
        )
        worker = Worker.objects.create(
            user=cls.worker, skills="Django", experience="3 anos"
        )
        cls.opportunity = Opportunity.objects.create(
            employer=employer, title="Website", description="Portal",
            status=Opportunity.Status.CLOSED
        )
        cls.proposal = Proposal.objects.create(
            opportunity=cls.opportunity, worker=worker, description="Vou fazer",
            status=Proposal.Status.ACCEPTED
        )
        cls.engagement = Engagement.objects.create(proposal=cls.proposal)

    def test_owner_can_list_proposals_and_worker_display_name(self):
        self.client.force_authenticate(self.employer)
        response = self.client.get(
            f"/api/marketplace/opportunities/{self.opportunity.pk}/proposals/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["worker_name"], "worker_d53")
        self.assertEqual(response.data[0]["id"], self.proposal.pk)
        self.assertNotIn("email", response.data[0])

    def test_worker_cannot_enumerate_other_workers_proposals(self):
        self.client.force_authenticate(self.worker)
        response = self.client.get(
            f"/api/marketplace/opportunities/{self.opportunity.pk}/proposals/"
        )
        self.assertEqual(response.status_code, 403)

    def test_unrelated_user_cannot_enumerate_proposals(self):
        self.client.force_authenticate(self.other)
        response = self.client.get(
            f"/api/marketplace/opportunities/{self.opportunity.pk}/proposals/"
        )
        self.assertEqual(response.status_code, 403)

    def test_anonymous_cannot_read_proposals_or_engagements(self):
        self.client.force_authenticate(user=None)
        self.assertEqual(
            self.client.get(
                f"/api/marketplace/opportunities/{self.opportunity.pk}/proposals/"
            ).status_code, 401
        )
        self.assertEqual(
            self.client.get("/api/contracts/engagements/").status_code, 401
        )

    def test_employer_and_worker_can_find_same_engagement(self):
        for user in (self.employer, self.worker):
            with self.subTest(user=user.username):
                self.client.force_authenticate(user)
                response = self.client.get("/api/contracts/engagements/")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]["id"], self.engagement.pk)
                self.assertEqual(
                    response.data[0]["status"], Engagement.Status.PENDING_AGREEMENT
                )

    def test_outsider_cannot_discover_other_users_engagements(self):
        self.client.force_authenticate(self.other)
        response = self.client.get("/api/contracts/engagements/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
