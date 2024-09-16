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
from django.urls import path
from Funcionário.views import index,cadastrar,teste,teste_copy,andament


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('aluno/cadastro',cadastrar,name="cadastro_aluno"),
    path('teste/',teste,name="teste"),
    path('testec/',teste_copy,name="copy"),
    path('anda/',andament,name="and"),
]
