"""Account API: registration, JWT-authenticated self-service and public profiles."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employer, Worker
from .serializers import (
    EmployerCreateSerializer,
    EmployerSerializer,
    EmployerPublicSerializer,
    RegisterSerializer,
    UserSerializer,
    WorkerCreateSerializer,
    WorkerSerializer,
)

User = get_user_model()


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                user = serializer.save()
        except IntegrityError:
            return Response(
                {"detail": "Username ou email já está em uso."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class MyProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response(UserSerializer(user).data)


class UserList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response(UserSerializer(User.objects.all(), many=True).data)


class EmployerList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        profiles = Employer.objects.select_related("user").order_by("-id")
        return Response(EmployerSerializer(profiles, many=True).data)


class EmployerDetail(APIView):
    # Public business metadata only; authenticated owners/staff see private fields.
    permission_classes = [AllowAny]

    def get(self, request, pk):
        profile = get_object_or_404(
            Employer.objects.select_related("user"), pk=pk
        )
        serializer = (
            EmployerSerializer
            if request.user.is_staff or profile.user_id == request.user.id
            else EmployerPublicSerializer
        )
        return Response(serializer(profile).data)


class MyEmployer(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Employer, user=request.user)
        return Response(EmployerSerializer(profile).data)

    def post(self, request):
        if Employer.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "Este perfil de empregador já existe."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = EmployerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                profile = serializer.save(user=request.user)
        except IntegrityError:
            return Response(
                {"detail": "Este perfil de empregador já existe."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            EmployerSerializer(profile).data,
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        profile = get_object_or_404(Employer, user=request.user)
        serializer = EmployerCreateSerializer(
            profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(EmployerSerializer(profile).data)


class WorkerList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profiles = Worker.objects.select_related("user").order_by("-id")
        skill = request.query_params.get("skills", "").strip()
        if skill:
            profiles = profiles.filter(skills__icontains=skill)
        return Response(WorkerSerializer(profiles, many=True).data)


class WorkerDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        profile = get_object_or_404(
            Worker.objects.select_related("user"), pk=pk
        )
        return Response(WorkerSerializer(profile).data)


class MyWorker(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Worker, user=request.user)
        return Response(WorkerSerializer(profile).data)

    def post(self, request):
        if Worker.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "Este perfil de trabalhador já existe."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = WorkerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                profile = serializer.save(user=request.user)
        except IntegrityError:
            return Response(
                {"detail": "Este perfil de trabalhador já existe."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            WorkerSerializer(profile).data,
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        profile = get_object_or_404(Worker, user=request.user)
        serializer = WorkerCreateSerializer(
            profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(WorkerSerializer(profile).data)
