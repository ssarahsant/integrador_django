# importações
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers
from ..models import Sensor
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.routers import Response

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
    
# Permissão para realizar consultas (ocultas) no banco através json 
# existem duas formas para isso, através do json ou get
# a outra forma é usando urls
class SensorFilterView (APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tipo = request.data.get('tipo', None)
        localizacao = request.data.get('localizacao', None)
        responsavel = request.data.get('responsavel', None)
        status_operacional = request.data.get('status_operacional', None)

        # Q permite fazer uma query
        filters = Q()
        if tipo:
            filters &=Q (tipo__icontains=tipo)
        if localizacao:
            filters &=Q (localizacao__icontains=localizacao)
        if responsavel:
            filters &=Q (responsavel__icontains=responsavel)
        if status_operacional:
            filters &=Q (status_operacional__icontains=status_operacional)
        
        queryset = Sensor.objects.filter(filters)
        serializer = serializers.SensorSerializer(queryset, many=True)
        return Response(serializer.data)
