from django.urls import path
from . import views

urlpatterns = [
    path("from-proposal/<int:proposal_id>/", views.AcceptProposal.as_view(),
         name="contracts-from-proposal"),
    path("mine/", views.MyContracts.as_view(), name="contracts-mine"),
    path("<int:contract_id>/", views.ContractDetail.as_view(), name="contracts-detail"),
    path("<int:contract_id>/versions/", views.AgreementVersions.as_view(),
         name="contracts-versions"),
    path("versions/<int:version_id>/", views.AgreementDraftEdit.as_view(),
         name="contracts-draft-edit"),
    path("versions/<int:version_id>/submit/", views.AgreementSubmit.as_view(),
         name="contracts-submit"),
    path("versions/<int:version_id>/approve/", views.AgreementApprove.as_view(),
         name="contracts-approve"),
    path("versions/<int:version_id>/reject/", views.AgreementReject.as_view(),
         name="contracts-reject"),
    path("<int:contract_id>/amend/", views.AgreementAmend.as_view(),
         name="contracts-amend"),
    path("<int:contract_id>/renegotiate/", views.AgreementRenegotiate.as_view(),
         name="contracts-renegotiate"),
    path("<int:contract_id>/complete/", views.ContractComplete.as_view(),
         name="contracts-complete"),
]
