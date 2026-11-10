"""Serializers for accounts and user-owned professional profiles."""
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Employer, Worker
from .utils.phone import normalize_mz_phone

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False, min_length=8)

    class Meta:
        model = User
        fields = ["username", "name", "email", "phone", "password"]

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Este email já está registado.")
        return email

    def validate_username(self, value):
        username = value.strip().lower()
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("Este utilizador já está registado.")
        return username

    def validate_phone(self, value):
        try:
            return normalize_mz_phone(value)
        except ValueError as exc:
            raise serializers.ValidationError(str(exc)) from exc

    def validate_name(self, value):
        name = value.strip()
        if len(name) < 2:
            raise serializers.ValidationError("Indique o seu nome.")
        return name

    def validate_password(self, value):
        temp = User(
            username=self.initial_data.get("username", ""),
            name=self.initial_data.get("name", ""),
            email=self.initial_data.get("email", ""),
        )
        try:
            password_validation.validate_password(value, user=temp)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages) from exc
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        return User.objects.create_user(password=password, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "phone", "roles"]
        read_only_fields = fields

    def get_roles(self, obj):
        roles = []
        if Worker.objects.filter(user_id=obj.id).exists():
            roles.append("worker")
        if Employer.objects.filter(user_id=obj.id).exists():
            roles.append("employer")
        return roles


class EmployerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["company_name", "address"]

    def validate_company_name(self, value):
        return value.strip()


class EmployerSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source="user.name", read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employer
        fields = ["id", "user_id", "employer_name", "company_name", "address"]
        read_only_fields = fields


class WorkerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["skills", "experience"]

    def validate_skills(self, value):
        return value.strip()


class WorkerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.name", read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Worker
        fields = ["id", "user_id", "name", "skills", "experience"]
        read_only_fields = fields


class UsernameOrEmailTokenSerializer(TokenObtainPairSerializer):
    """Accept email or username in the standard 'username' JWT field."""

    def validate(self, attrs):
        identity = attrs.get(self.username_field, "")
        account = User.objects.filter(email__iexact=identity).first()
        if account is None:
            account = User.objects.filter(username__iexact=identity).first()
        if account is not None:
            attrs[self.username_field] = account.get_username()
        return super().validate(attrs)
