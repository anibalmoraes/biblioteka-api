from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
