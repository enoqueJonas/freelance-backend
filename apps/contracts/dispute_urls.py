from django.urls import path
from . import dispute_views as views

urlpatterns = [
    path("", views.Disputes.as_view(), name="disputes-list-create"),
    path("<int:pk>/", views.DisputeDetail.as_view(), name="dispute-detail"),
    path("<int:pk>/evidence/", views.DisputeAddEvidence.as_view(), name="dispute-evidence"),
    path("<int:pk>/begin-review/", views.DisputeBeginReview.as_view(), name="dispute-begin-review"),
    path("<int:pk>/request-information/", views.DisputeRequestInformation.as_view(), name="dispute-request-info"),
    path("<int:pk>/result/", views.DisputeRegisterResult.as_view(), name="dispute-result"),
    path("<int:pk>/close/", views.DisputeClose.as_view(), name="dispute-close"),
]
