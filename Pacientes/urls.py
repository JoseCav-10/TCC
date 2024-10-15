from django.urls import path, include
from .views import FormAgendamentoView,AndamentoView,HomeView,DeleteFormView,DetailsPedidosExamesView,MeusDadosView
from Funcionário.views import ForgotPasswordView
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("andamento/", AndamentoView.as_view(), name="anda"),
    path("agendamento", FormAgendamentoView.as_view(), name="form"),
    path("forgot_password/", ForgotPasswordView.as_view(), name="senha_f"),
    path("<int:pk>/del_form/", DeleteFormView.as_view(), name="del_form"),
    path("<int:pk>/detail_form/", DetailsPedidosExamesView.as_view(), name="detail"),
    path("<int:pk>/meu/", MeusDadosView.as_view(), name="meu"),
]