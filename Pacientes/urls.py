from django.urls import path, include
from .views import IndexView,Forgot_PasswordView,Form_PedidosView,RegisterView,AndamentoView,Dados_PacienteView,HomeView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("meus_dados/", Dados_PacienteView.as_view(), name="dado"),
    path("andamento/", AndamentoView.as_view(), name="anda"),
    path("agendamento", Form_PedidosView.as_view(), name="form"),
    path("home/", HomeView.as_view(), name="home"),
    path("forgot_password/", Forgot_PasswordView.as_view(), name="senha_f"),
]