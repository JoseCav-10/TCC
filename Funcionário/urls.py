from django.urls import path
from Pacientes.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]