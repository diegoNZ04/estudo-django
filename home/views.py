from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_home(req):
    if req.method == "GET":
        return render(req, 'ver_home.html')
    elif req.method == "POST":
        nome = req.POST.get('nome')
        idade = req.POST.get('idade')
        
        pessoa = Pessoa(nome=nome, idade=idade)
        pessoas = Pessoa.objects.filter(nome=nome, idade=idade)
        
        if pessoas.exists():
            return HttpResponse('Usuário Já Cadastrado No Database!')
       
        pessoa.save()
        return HttpResponse(f'Usuario {nome} de {idade} Anos Cadastrado!')
         
        
       
    
def inserir_item(req):
    return HttpResponse('Estou no inserir')