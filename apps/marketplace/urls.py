from django.urls import path
from .views import (
    MyOffers, MyProposals, OfferClose, OfferDetail, OfferListCreate,
    OfferProposals,
)

urlpatterns = [
    path("offers/", OfferListCreate.as_view(), name="marketplace-offers"),
    path("offers/mine/", MyOffers.as_view(), name="marketplace-my-offers"),
    path("offers/<int:pk>/", OfferDetail.as_view(), name="marketplace-offer-detail"),
    path("offers/<int:pk>/close/", OfferClose.as_view(), name="marketplace-offer-close"),
    path("offers/<int:pk>/proposals/", OfferProposals.as_view(), name="marketplace-offer-proposals"),
    path("proposals/mine/", MyProposals.as_view(), name="marketplace-my-proposals"),
]
