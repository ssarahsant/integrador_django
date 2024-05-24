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
    
# Modelagem da Tabela para Sensores de Temperatura
class TemperaturaData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    # timestamp = models.DateTimeField(auto_now_add = True)
    timestamp = models.DateTimeField()


    def __str__(self):
        return f"Temperatura {self.valor} C - {self.timestamp}"

# Modelagem da Tabela para Sensores de Umiade
class UmidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()


    def __str__(self):
        return f"Umidade {self.valor} % - {self.timestamp}"

# Modelagem da Tabela para Sensores Contador
class ContadorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()


    def __str__(self):
        return f"Contagem {self.sensor} - {self.timestamp}"


# Modelagem da Tabela para Sensores de Luminosidade
class LuminosidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()


    def __str__(self):
        return f"Luminosidade {self.valor} - {self.timestamp}"