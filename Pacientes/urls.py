from django.urls import path, include
from .views import IndexView,form_agendamento,AndamentoView,Dados_PacienteView,HomeView
from Funcionário.views import forgot_password
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("meus_dados/", Dados_PacienteView.as_view(), name="dado"),
    path("andamento/", AndamentoView.as_view(), name="anda"),
    path("agendamento", form_agendamento, name="form"),
    path("home/", HomeView.as_view(), name="home"),
    path("forgot_password/", forgot_password, name="senha_f"),
]