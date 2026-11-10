"""Root URL configuration for the ConecTA REST API."""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.accounts.auth import UsernameOrEmailTokenView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/marketplace/", include("apps.marketplace.urls")),
    path("api/contracts/", include("apps.contracts.urls")),
    path("api/auth/login/", UsernameOrEmailTokenView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
