from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrReadOnly2


class BookView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly2]

    serializer_class = BookSerializer
    queryset = Book.objects.all()
