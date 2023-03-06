from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BookView(ListCreateAPIView):
    ...


class BookDetailView(RetrieveUpdateDestroyAPIView):
    ...
