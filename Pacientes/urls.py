from django.urls import path, include
from .views import form_agendamento,AndamentoView,Dados_PacienteView,HomeView,DeleteFormView,DetailsPedidos_ExamesView
from Funcionário.views import forgot_password
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("meus_dados/", Dados_PacienteView.as_view(), name="dado"),
    path("andamento/", AndamentoView.as_view(), name="anda"),
    path("agendamento", form_agendamento, name="form"),
    path("forgot_password/", forgot_password, name="senha_f"),
    path("<int:pk>/del_form/", DeleteFormView.as_view(), name="del_form"),
    path("<int:pk>/detail_form/", DetailsPedidos_ExamesView.as_view(), name="detail"),
]