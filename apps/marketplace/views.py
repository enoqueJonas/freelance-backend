"""Marketplace endpoints with server-side ownership and RN02 enforcement."""
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Employer, Worker

from .models import Offer, Proposal
from .serializers import OfferSerializer, ProposalCreateSerializer, ProposalSerializer


class OfferListCreate(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        offers = Offer.objects.filter(status=Offer.Status.ACTIVE).select_related(
            "employer", "employer__user"
        )
        category = request.query_params.get("category", "").strip()
        if category:
            offers = offers.filter(category__iexact=category)
        return Response(OfferSerializer(offers[:100], many=True).data)

    def post(self, request):
        employer = Employer.objects.filter(user=request.user).first()
        if employer is None:
            return Response(
                {"detail": "Crie um perfil de empregador antes de publicar."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        offer = serializer.save(employer=employer)
        return Response(
            OfferSerializer(offer).data, status=status.HTTP_201_CREATED
        )


class MyOffers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        offers = Offer.objects.filter(
            employer__user=request.user
        ).select_related("employer", "employer__user")[:100]
        return Response(OfferSerializer(offers, many=True).data)


class OfferDetail(APIView):
    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAuthenticated()]

    def get_object(self, request, pk):
        offer = get_object_or_404(
            Offer.objects.select_related("employer", "employer__user"), pk=pk
        )
        if offer.status == Offer.Status.CLOSED and (
            not request.user.is_authenticated or
            offer.employer.user_id != request.user.id
        ):
            return None
        return offer

    def get(self, request, pk):
        offer = self.get_object(request, pk)
        if offer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(OfferSerializer(offer).data)

    def patch(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        if offer.employer.user_id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if offer.status != Offer.Status.ACTIVE or offer.proposals.exists():
            return Response(
                {"detail": "Oportunidades fechadas ou com candidaturas não podem ser alteradas."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = OfferSerializer(offer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(OfferSerializer(offer).data)


class OfferClose(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        with transaction.atomic():
            offer = get_object_or_404(
                Offer.objects.select_for_update().select_related("employer"),
                pk=pk,
            )
            if offer.employer.user_id != request.user.id:
                return Response(status=status.HTTP_403_FORBIDDEN)
            if offer.status == Offer.Status.CLOSED:
                return Response(
                    {"detail": "A oportunidade já está fechada."},
                    status=status.HTTP_409_CONFLICT,
                )
            offer.status = Offer.Status.CLOSED
            offer.save(update_fields=["status", "updated_at"])
        return Response(OfferSerializer(offer).data)


class OfferProposals(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        offer = get_object_or_404(Offer.objects.select_related("employer"), pk=pk)
        if offer.employer.user_id != request.user.id and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        qs = Proposal.objects.filter(offer=offer).select_related(
            "worker", "worker__user"
        )[:100]
        return Response(ProposalSerializer(qs, many=True).data)

    def post(self, request, pk):
        worker = Worker.objects.filter(user=request.user).first()
        if worker is None:
            return Response(
                {"detail": "Crie um perfil de trabalhador antes de propor."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = ProposalCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                offer = get_object_or_404(
                    Offer.objects.select_for_update().select_related("employer"),
                    pk=pk,
                )
                if offer.status != Offer.Status.ACTIVE:
                    return Response(
                        {"detail": "Esta oportunidade não aceita mais propostas."},
                        status=status.HTTP_409_CONFLICT,
                    )
                if offer.employer.user_id == request.user.id:
                    return Response(
                        {"detail": "RN02: não pode propor à própria oportunidade."},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                if Proposal.objects.filter(offer=offer, worker=worker).exists():
                    return Response(
                        {"detail": "Já submeteu uma proposta."},
                        status=status.HTTP_409_CONFLICT,
                    )
                proposal = serializer.save(offer=offer, worker=worker)
        except IntegrityError:
            return Response(
                {"detail": "Já submeteu uma proposta."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            ProposalSerializer(proposal).data,
            status=status.HTTP_201_CREATED,
        )


class MyProposals(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Proposal.objects.filter(
            worker__user=request.user
        ).select_related("worker", "worker__user", "offer")[:100]
        return Response(ProposalSerializer(qs, many=True).data)
