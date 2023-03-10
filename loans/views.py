from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Loan
from .serializers import LoanSerializer
from .permissions import IsBlocked, IsActive, IsAccountOwner, IsAdmin


class LoansView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsBlocked]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoansHistoricView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive, IsAccountOwner]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_url_kwarg = "user_id"


class LoansDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsActive, IsAdmin]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()

    def perform_update(self, serializer):
        serializer.save()

    lookup_url_kwarg = "user_id"
