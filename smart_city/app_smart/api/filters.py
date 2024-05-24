import django_filters
from app_smart.models import Sensor

class SensorFilter(django_filters.FilterSet):
    responsavel = django_filters.CharFilter(field_name='responsavel', lookup_expr='incontains')
    status_operacional = django_filters.CharFilter(field_name='status_operacional', lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='exact')
    localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='incontains')
    class Meta:
        model = Sensor
        fields = ['responsavel', 'status_operacional', 'tipo', 'localizacao']