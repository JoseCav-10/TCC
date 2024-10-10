from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from Funcionário.models import CustomUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from Funcionário.forms import CustomUsuarioCreateForm
import os
# Create your views here.


class IndexView(TemplateView):
    template_name = "paciente_pages/index.html"


class HomeView(LoginRequiredMixin, ListView):
    model = CustomUsuario
    template_name = "paciente_pages/home.html"
    context_object_name = "user"
    login_url = "/contas/login"

    def get_queryset(self):
        user = CustomUsuario.objects.get(username=self.request.user)
        return user
        
        
    


class Form_PedidosView(TemplateView):
    template_name = "paciente_pages/fomu.html"


class AndamentoView(TemplateView):
    template_name = "paciente_pages/andamento.html"


class Dados_PacienteView(TemplateView):
    template_name = "paciente_pages/meus_dados.html"


'''class CreateRegisterView(CreateView):
    model = CustomUsuario
    template_name = "registration/register.html"
    fields = ["name",'cpf','cartao_sus', "username","password1","password2",'data_nascimento',"sexo", "fone", "endereco", "cep", "foto_perfil"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(attrs={"class": "form-control", "id": 'id_username', 'aria-describedby': "id_username_helptext", "name": "username", "max-length":'150'})
        form.fields["password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        form.fields["name"].widget = forms.TextInput(attrs={"class": "form-control", "id": 'exampleInputText1'})
        form.fields["cpf"].widget = forms.TextInput(attrs={"class": "form-control", "id": "id_cpf"})
        form.fields["cartao_sus"].widget = forms.TextInput(attrs={"class": "form-control", "id": "susInput"})
        form.fields["data_nascimento"].widget = forms.DateInput(attrs={"class": "form-control", "type": "date", 'id': 'dateInput'})
        form.fields["sexo"].widget = forms.Select(attrs={"class": "form-control"})
        form.fields["fone"].widget = forms.TextInput(attrs={"class": "form-control", "id": 'phoneInput'})
        form.fields["endereco"].widget = forms.TextInput(attrs={"class": "form-control", "id": 'endInput'})
        form.fields["cep"].widget = forms.TextInput(attrs={"class": "form-control", "id": 'cepInput'})
        form.fields["foto_perfil"].widget = forms.FileInput(attrs={"class": "form-control", 'id': 'foto'})

        return form'''
    


'''class Forgot_PasswordView(TemplateView):
    
    template_name = "forgot_password.html"
    
'''
    