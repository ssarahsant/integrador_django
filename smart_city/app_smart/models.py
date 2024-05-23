# Importação
from django.db import models

# Create your models here.

# Criação de Tabela Sensor
class Sensor(models.Model):
    # limitação das possibilitdade de tipo de sensores que o usuário pode cadastrar
    # criação de lista para definir opções de seleção do usuário, para padronizar 
    # a inserção de dados no banco
    TIPOS_SENSOR_CHOICES=[
        # Campo, Texto registrado
        ('Temperatura', 'Temperatura'),
        ('Umidade', 'Umidade'),
        ('Contador', 'Contador'),
        ('Luminosidade', 'Luminosidade')
    ]

    # Criação dos campos/colunas da Tabela Sensor

    # campo que recebe a opção que o usuário seleciona
    tipo = models.CharField(max_length=50, choices=TIPOS_SENSOR_CHOICES)
    #  mac_address = identificador de plavcas eletronicas
    # alfa numero que tem as informação de cada placa que se comunica
    mac_address = models.CharField(max_length=20, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    localizacao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length=20, blank=True, null=True)
    status_operacional = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)


    def __str__(self):
        return f"{self.tipo} - {self.localizacao}"
    
    