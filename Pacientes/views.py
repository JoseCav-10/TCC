from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView
from Funcionário.models import CustomUsuario,Pedidos_Exames
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from Funcionário.forms import CustomUsuarioCreateForm
import os
from Funcionário.forms import Pedidos_ExamesForm
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
        
        
    


def form_agendamento(request):
    form = Pedidos_ExamesForm()
    user = CustomUsuario.objects.get(username=request.user)
    if request.method == "POST":
        form = Pedidos_ExamesForm(request.POST, request.FILES)
        print("POST")
        print(request.POST)
        if form.is_valid():
            print("VALIDO")
            tipo_exame = form.cleaned_data['tipo_exame']
            laudo = form.cleaned_data['laudo']
            urgencia = form.cleaned_data['urgencia']
            requerente = form.cleaned_data["requerente"]
            print(requerente.name)
            first_data = request.POST["first_data"]
            second_data = request.POST["second_data"]
            dias_possiveis = f"{first_data},{second_data}"
            situacao = form.cleaned_data["situacao"]

            Pedidos_Exames.objects.create(requerente=requerente,tipo_exame=tipo_exame,laudo=laudo,urgencia=urgencia,dias_possiveis=dias_possiveis,situacao=situacao)

    context = {
        "form": form,
        "user": user
    }

    return render(request, "paciente_pages/fomu.html", context)



class AndamentoView(LoginRequiredMixin, ListView):
    model = Pedidos_Exames
    template_name = "paciente_pages/andamento.html"  # Template a ser utilizado
    context_object_name = 'objetos'  # Nome do contexto para a lista de objetos
    paginate_by = 4
    ordering = "-id"
    login_url = "/contas/login"

    def get_queryset(self):
        # Filtra os pedidos com base no usuário logado
        return super().get_queryset().filter(requerente=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cria uma lista de IDs de pedidos aprovados
        context['aprovados'] = [
            pedido.id for pedido in context['objetos'] if pedido.situacao.situacao == "Aprovado"
        ]
        return context


class DeleteFormView(DeleteView):
    model = Pedidos_Exames
    template_name = "paciente_pages/del_form.html"
    success_url = reverse_lazy("anda")


class DetailsPedidos_ExamesView(DetailView):
    template_name = "paciente_pages/details_form.html"
    model = Pedidos_Exames
    context_object_name = "pedidos"
    


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
    