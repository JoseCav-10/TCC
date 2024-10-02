"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Funcionário.views import index,cadastrar,teste,teste_copy,andament,dados,cadastro,esqueceu_senha
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="Funcionário.index.html"),name="index"),
    path('teste',index,name="index1"),
    path('contas/', include('django.contrib.auth.urls')),
    path('aluno/cadastro',cadastrar,name="cadastro_aluno"),
    path('home/',teste,name="home"),
    path('cadastro/',cadastro,name="cadastro"),
    path('esqueceu/',esqueceu_senha,name="senha_f"),
    path('form/',teste_copy,name="form"),
    path('anda/',andament,name="anda"),
    path('dados/',dados,name="dado"),
]
