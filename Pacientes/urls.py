from django.urls import path
from .views import FormAgendamentoView,AndamentoView,HomeView,DeleteFormView,DetailsPedidosExamesView,MeusDadosView,marcar_visualizacao,marcar_todas_como_lidas
from Funcionário.views import ForgotPasswordView
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("andamento/", AndamentoView.as_view(), name="anda"),
    path("marcar-visualizacao/", marcar_visualizacao, name="marcar_visualizacao"),
    path('notificacoes/marcar-todas-como-lidas/<int:destinatario_id>/', marcar_todas_como_lidas, name='marcar_todas_como_lidas'),
    path("agendamento", FormAgendamentoView.as_view(), name="form"),
    path("forgot_password/", ForgotPasswordView.as_view(), name="senha_f"),
    path("<int:pk>/del_form/", DeleteFormView.as_view(), name="del_form"),
    path("<int:pk>/detail_form/", DetailsPedidosExamesView.as_view(), name="detail"),
    path("<int:pk>/meu/", MeusDadosView.as_view(), name="meu"),
]