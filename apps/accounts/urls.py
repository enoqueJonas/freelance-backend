"""API endpoints for the account module."""
from django.urls import path
from . import views

urlpatterns = [
    path("me/", views.MyProfile.as_view(), name="accounts-me"),
    path("auth/register/", views.Register.as_view(), name="accounts-register"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="accounts-user-detail"),
    path("users/", views.UserList.as_view(), name="accounts-user-list"),
    path("workers/", views.WorkerList.as_view(), name="accounts-workers"),
    path("workers/<int:pk>/", views.WorkerDetail.as_view(), name="accounts-worker-detail"),
    path("employers/", views.EmployerList.as_view(), name="accounts-employers"),
    path("employers/<int:pk>/", views.EmployerDetail.as_view(), name="accounts-employer-detail"),
    path("me/employer/", views.MyEmployer.as_view(), name="accounts-my-employer"),
    path("me/worker/", views.MyWorker.as_view(), name="accounts-my-worker"),
]
