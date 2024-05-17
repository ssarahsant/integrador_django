from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Criação de uma Função
def abre_index(request):
    # criar uma página home
    mensagem = "Muito bem vindo ao Smart City"
    # apresentação da página
    return HttpResponse(mensagem)