from rest_framework import generics

from accounts import serializers
from accounts import services


class RegisterApiView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    queryset = services.get_users()