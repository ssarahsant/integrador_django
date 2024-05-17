# Importações
from django.urls import path, include
from . import views
from app_smart.api.viewsets import CreateUserAPIViweSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Criação das Rotas
urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUserAPIViweSet.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

