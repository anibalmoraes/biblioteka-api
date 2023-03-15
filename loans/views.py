from django.shortcuts import render
from rest_framework.views import View, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView
)
from .models import Loan
from .serializers import LoanSerializer
from .permissions import (
    IsBlocked,
    IsActive,
    IsAccountOwner,
    IsAdmin,
    IsAdminOrReadOnly,
    IsDependecies,
)
from copies.models import Copy
from django.shortcuts import get_object_or_404, get_list_or_404
from users.models import User
from rest_framework.exceptions import APIException
from datetime import date


class LoansView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, IsActive, IsBlocked]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Loan.objects.filter(is_active=True, user_id=self.kwargs["copy_id"])
        return Loan.objects.filter(is_active=True, user_id=self.request.user)
    serializer_class = LoanSerializer

    def perform_create(self, serializer: LoanSerializer, **kwargs):
        copy = get_object_or_404(Copy, pk=self.kwargs["copy_id"])

        user = User.objects.get(username=serializer.validated_data.pop("username"))
        if not user.while_blocked:
            user.while_blocked = date(1930, 1, 1)
        if user.is_blocked or date.today() <= user.while_blocked:
            blok_error = APIException("Usário bloqueado!")
            blok_error.status_code = 403
            raise blok_error
        serializer.save(copy=copy, user=user)

    lookup_url_kwarg = "copy_id"


class LoansHistoricView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Loan.objects.filter(is_active=False, user_id=self.kwargs["user_id"])
        return Loan.objects.filter(is_active=False, user_id=self.request.user.id)

    serializer_class = LoanSerializer

    lookup_url_kwarg = "user_id"


class LoansUserView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Loan.objects.filter(user_id=self.kwargs["user_id"])
        return Loan.objects.filter(user_id=self.request.user.id)

    serializer_class = LoanSerializer

    lookup_url_kwarg = "user_id"


class LoansDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive, IsAdminOrReadOnly]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()

    def perform_update(self, serializer):
        serializer.save()

    lookup_url_kwarg = "loan_id"
