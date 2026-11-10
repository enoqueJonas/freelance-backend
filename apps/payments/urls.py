from django.urls import path
from .views import ExternalPaymentsForContract, ExternalPaymentRespond

urlpatterns = [
    path("contracts/<int:contract_id>/", ExternalPaymentsForContract.as_view(),
         name="payments-by-contract"),
    path("<int:payment_id>/respond/", ExternalPaymentRespond.as_view(),
         name="payments-respond"),
]
