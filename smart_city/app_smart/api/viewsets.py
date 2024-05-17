# importações
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers

# Criação de uma classe 
class CreateUserAPIViweSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # permite acessar a api quem está logado
    # permissions_classes = [permissions.IsAdminUser]

    # Criação de uma função
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


