from django.urls import path
from .views import (
    EvidenceReviews, EvidenceReviewDetail,
    PendingEvidenceReviews, EvidenceReviewDecision,
)

urlpatterns = [
    path("reviews/", EvidenceReviews.as_view(), name="evidence-reviews"),
    path("reviews/pending/", PendingEvidenceReviews.as_view(),
         name="evidence-pending"),
    path("reviews/<int:pk>/", EvidenceReviewDetail.as_view(),
         name="evidence-detail"),
    path("reviews/<int:pk>/decision/", EvidenceReviewDecision.as_view(),
         name="evidence-decision"),
]
