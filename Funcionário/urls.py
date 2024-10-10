from django.urls import path

from .views import register_user, forgot_password, testes

urlpatterns = [
    path('', register_user, name='register'),
    path('forgot_password', forgot_password, name='forgot'),
    path('teste', testes, name='teste'),
]