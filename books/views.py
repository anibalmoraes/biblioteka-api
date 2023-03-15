from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer, FollowingSerializer, FollowersSerializer
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


class FollowingView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]

    serializer_class = FollowingSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.request.user.id)
        book = get_object_or_404(Book, pk=self.kwargs["pk"])

        serializer.save(user_id=user, book_id=book)


class FollowersView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]

    serializer_class = FollowersSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        followers = []
        book = get_object_or_404(Book, pk=self.kwargs["pk"])

        for follower in book.following.all().values("username"):
            print(follower)
            followers.append(follower)

        print(followers, type(followers[0]))

        return followers
