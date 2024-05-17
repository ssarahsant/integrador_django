# importar as bibliotecas
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# Criação de uma classe para Manipulação do Banco
# pega os metadados (dados que trafega na api) 
# e informa como os dados serão tratados nessa aplicação
class UserSerializer(serializers.ModelSerializer):
    # tratativa de senha
    password = serializers.CharField(write_only = True)


    # Criação de Função para Criptografar
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
            

    # cria uma classe para serializer o canal de comunicação da tabela modelo user
    # desenvolve uma forma de trafegar os dados
    class Meta:
        # ifnroma a tebal do banco de dados
        model = User
        # informa os campos da tabela que serão enviados no consumo dessa api
        fields = ['id', 'username', 'email', 'password']
    # trata o campo de forma espeficica, impedindo de consumir a senha
    # desse modo a senha não será informada, sendo cadastrada direto no banco 
    # evitando a violação desse campo sensivel 
    extra_kwargs = {'password': {'write_only': True}}

