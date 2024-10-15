from django.urls import path

from .views import RegisterUserView,ForgotPasswordView

urlpatterns = [
    path('', RegisterUserView.as_view(), name='register'),
    path('forgot_password', ForgotPasswordView.as_view(), name='forgot'),
    #path('teste', "função", name='teste'),
]