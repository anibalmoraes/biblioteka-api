from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Book
from .serializers import BookSerializer


class BookView(ListCreateAPIView, PageNumberPagination):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(RetrieveUpdateDestroyAPIView):
    ...
