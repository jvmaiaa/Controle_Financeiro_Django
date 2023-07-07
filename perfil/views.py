from django.shortcuts import render 
from django.http import HttpResponse
from .models import Conta
# função home recebe a request do usuário e retorna uma response 
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request, 'gerenciar.html')

# dentro de cada parâmetro eu vou colocar oq foi escrito em cada name de cada input
# dados do tipo de arquivo, eu recebo com o parâmetro FILES, como foi colocado no campo icones 
def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    return HttpResponse(f'{apelido} {banco} {tipo} {valor} {icone}')

