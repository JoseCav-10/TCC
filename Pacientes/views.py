from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "paciente_pages/index.html"


class HomeView(TemplateView):
    template_name = "paciente_pages/home.html"


class Form_PedidosView(TemplateView):
    template_name = "paciente_pages/fomu.html"


class AndamentoView(TemplateView):
    template_name = "paciente_pages/andamento.html"


class Dados_PacienteView(TemplateView):
    template_name = "paciente_pages/meus_dados.html"


class RegisterView(TemplateView):
    template_name = "registration/register.html"


class Forgot_PasswordView(TemplateView):
    template_name = "forgot_password.html"

    