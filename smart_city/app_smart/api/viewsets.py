# importações
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers
from ..models import Sensor
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter
from django_filters.rest_framework import DjangoFilterBackend

# Criação de uma classe 
class CreateUserAPIViweSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # permite acessar a api quem está logado
    # permissions_classes = [permissions.IsAdminUser]

    # Criação de uma função
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Realiza a gestão da serialização (permissão de acessos e vizualização)
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permissions_class = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter
    