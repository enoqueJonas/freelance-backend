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


def public_https_url(value):
    """Only expose HTTPS links; do not fetch user-supplied addresses."""
    from ipaddress import ip_address
    from urllib.parse import urlsplit

    value = value.strip()
    if not value:
        return value
    parsed = urlsplit(value)
    if parsed.scheme.lower() != "https" or not parsed.hostname or (
        parsed.username is not None or parsed.password is not None
    ):
        raise serializers.ValidationError("Use um endereço HTTPS público sem credenciais.")
    host = parsed.hostname.lower()
    if host in {"localhost", "localhost.localdomain"} or host.endswith(".local"):
        raise serializers.ValidationError("Não é permitido utilizar endereços locais.")
    try:
        if not ip_address(host).is_global:
            raise serializers.ValidationError("Endereços IP internos não são permitidos.")
    except ValueError:
        pass  # regular DNS hostname
    return value


def cleaned_text(value):
    return value.strip()


class SkillsInputField(serializers.CharField):
    """Accept a string or a small string list without migrating legacy DB values."""
    def to_internal_value(self, data):
        if isinstance(data, list):
            if len(data) > 20 or any(not isinstance(x, str) for x in data):
                raise serializers.ValidationError("Até 20 competências em texto.")
            data = ", ".join(data)
        value = super().to_internal_value(data)
        entries = [v.strip() for v in value.split(",") if v.strip()]
        if len(entries) > 20 or any(len(x) > 60 for x in entries):
            raise serializers.ValidationError("Indique até 20 competências de 60 caracteres.")
        if len(set(x.casefold() for x in entries)) != len(entries):
            raise serializers.ValidationError("Não repita competências.")
        result = ", ".join(entries)
        if len(result) > 200:
            raise serializers.ValidationError("A descrição excede 200 caracteres.")
        return result


class EmployerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            "company_name", "address", "contact_name", "description",
            "industry", "location", "website_url",
        ]

    def validate_company_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Indique a organização.")
        return value.strip()

    def validate_description(self, value):
        if len(value) > 3000:
            raise serializers.ValidationError("Descrição demasiado extensa.")
        return value.strip()

    def validate_website_url(self, value):
        return public_https_url(value)


class EmployerSerializer(serializers.ModelSerializer):
    """Private representation: used only for the owner or an administrator."""
    employer_name = serializers.CharField(source="user.name", read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employer
        fields = [
            "id", "user_id", "employer_name", "company_name", "address",
            "contact_name", "description", "industry", "location", "website_url",
        ]
        read_only_fields = fields


class EmployerPublicSerializer(serializers.ModelSerializer):
    """Safe business catalogue: no home address, contact or user's name."""
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employer
        fields = [
            "id", "user_id", "company_name", "description",
            "industry", "location", "website_url",
        ]
        read_only_fields = fields


class WorkerCreateSerializer(serializers.ModelSerializer):
    skills = SkillsInputField(max_length=200, allow_blank=False)

    class Meta:
        model = Worker
        fields = [
            "skills", "experience", "title", "bio", "location",
            "experience_years", "github_url", "portfolio_url",
        ]

    def validate_title(self, value):
        return value.strip()

    def validate_bio(self, value):
        if len(value) > 3000:
            raise serializers.ValidationError("Biografia demasiado extensa.")
        return value.strip()

    def validate_experience_years(self, value):
        if value is not None and value > 70:
            raise serializers.ValidationError("Indique um número de anos plausível.")
        return value

    def validate_github_url(self, value):
        url = public_https_url(value)
        if url:
            from urllib.parse import urlsplit
            if urlsplit(url).hostname not in ("github.com", "www.github.com"):
                raise serializers.ValidationError("Indique um perfil github.com válido.")
        return url

    def validate_portfolio_url(self, value):
        return public_https_url(value)


class WorkerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.name", read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    skills_list = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = [
            "id", "user_id", "name", "skills", "skills_list", "experience",
            "title", "bio", "location", "experience_years",
            "github_url", "portfolio_url",
        ]
        read_only_fields = fields

    def get_skills_list(self, obj):
        return [s.strip() for s in obj.skills.split(",") if s.strip()]


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
