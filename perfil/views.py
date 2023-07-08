from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta
from django.contrib import messages
from django.contrib.messages import constants

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

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar/')
    
    # serve para criar uma referência para a model
    conta = Conta(
        apelido = apelido,
        banco = banco, 
        tipo = tipo, 
        valor = valor, 
        icone = icone,
    )
    
    # efetiva nova conta criada no banco de dados
    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

