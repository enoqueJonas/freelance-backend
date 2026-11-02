from django.urls import path
from . import views

urlpatterns = [
    path("engagements/<int:engagement_id>/", views.engagement_detail, name="engagement-detail"),
    path("engagements/<int:engagement_id>/agreements/", views.propose_initial_agreement, name="propose-initial-agreement"),
    path(
        "engagements/<int:engagement_id>/agreements/<int:version_id>/accept/",
        views.accept_agreement,
        name="accept-agreement",
    ),
]
