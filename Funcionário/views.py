from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect


# Create your views here.

def index(request):
        return render(request,'paciente_pages/index.html')


def cadastrar(request):
   return render(request,'paciente_pages/cadastro_aluno.html')


def teste(request):
      return render(request, "paciente_pages/home.html")
 

def teste_copy(request):
      return render(request, "paciente_pages/fomu.html")

def andament(request):
      return render(request, "paciente_pages/andamento.html")
