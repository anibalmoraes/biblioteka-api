from django.shortcuts import render
from rest_framework.views import View, Request, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
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
from django.shortcuts import get_object_or_404
from users.models import User


class LoansView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, IsActive, IsBlocked]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_url_kwarg = "copy_id"

    def perform_create(self, serializer: LoanSerializer):
        copy = get_object_or_404(Copy, pk=self.kwargs["copy_id"])
        user = User.objects.get(username=serializer.validated_data.pop("username"))

        serializer.save(copy=copy, user=user)


class LoansHistoricView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive, IsAccountOwner]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_url_kwarg = "user_id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object("is_active" == False)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LoansDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive, IsAdminOrReadOnly, IsAccountOwner]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object("is_active" == True)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()

    def perform_update(self, serializer):
        serializer.save()

    lookup_url_kwarg = "loan_id"
