from django.urls import path

from .views import register_user, forgot_password

urlpatterns = [
    path('', register_user, name='register'),
    path('fpass', forgot_password, name='forgot'),
]