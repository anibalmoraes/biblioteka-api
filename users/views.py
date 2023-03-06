from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserView(ListCreateAPIView):
    ...


class UserDetailView(RetrieveUpdateDestroyAPIView):
    ...
