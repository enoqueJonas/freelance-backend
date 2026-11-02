from django.urls import path
from . import views

urlpatterns = [
    path("engagements/", views.engagement_list, name="engagement-list"),
    path("engagements/<int:engagement_id>/", views.engagement_detail, name="engagement-detail"),
    path("engagements/<int:engagement_id>/agreements/", views.propose_initial_agreement, name="propose-initial-agreement"),
    path(
        "engagements/<int:engagement_id>/agreements/<int:version_id>/accept/",
        views.accept_agreement,
        name="accept-agreement",
    ),
    path(
        "engagements/<int:engagement_id>/agreements/<int:version_id>/reject/",
        views.reject_agreement,
        name="reject-agreement",
    ),
]
