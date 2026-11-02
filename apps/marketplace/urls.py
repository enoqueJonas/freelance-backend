from django.urls import path
from . import views

urlpatterns = [
    path("opportunities/", views.opportunities, name="opportunities"),
    path("opportunities/<int:opportunity_id>/publish/", views.publish_opportunity, name="publish-opportunity"),
    path("opportunities/<int:opportunity_id>/proposals/", views.submit_proposal, name="submit-proposal"),
    path("proposals/<int:proposal_id>/accept/", views.accept_proposal, name="accept-proposal"),
]
