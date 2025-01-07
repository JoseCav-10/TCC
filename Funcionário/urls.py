from django.urls import path

from .views import RegisterUserView,ForgotPasswordView,MenuFuncionarioView,CalendarioView,FormFuncionarioView,PedidoAFuncionarioView,DetailsPedidosExamesFuncView

urlpatterns = [
    path('', RegisterUserView.as_view(), name='register'),
    path('forgot_password', ForgotPasswordView.as_view(), name='forgot'),
    path('menu', MenuFuncionarioView.as_view(), name='menu'),
    path('pedidos', PedidoAFuncionarioView.as_view(), name='pedidos'),
    path('calendario', CalendarioView.as_view(), name='calendario'),
    path('<int:pk>/form', FormFuncionarioView.as_view(), name='form_func'),
    path('<int:pk>/detail_pedido', DetailsPedidosExamesFuncView.as_view(), name='detail_func'),
    #path('teste', "função", name='teste'),
]