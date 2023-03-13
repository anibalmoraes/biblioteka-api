from .models import Copy
from books.models import Book
from books.permissions import IsAdminOrReadOnly
from .serializers import CopySerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class CopyCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    lookup_url_kwarg = "book_id"

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_id"))
        return serializer.save(book=book)


class CopyView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer
