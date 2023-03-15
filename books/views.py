from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer, FollowingSerializer
from .permissions import IsAdminOrReadOnly
from users.models import User
from users.permissions import IsUserPermission
from django.shortcuts import get_object_or_404
import ipdb


class BookView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class FollowingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]

    serializer_class = FollowingSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.request.user.id)
        book = get_object_or_404(Book, pk=self.kwargs["pk"])

        serializer.save(user_id=user, book_id=book)
