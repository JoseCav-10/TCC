from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import CustomUsuarioCreateForm,Pedidos_ExamesForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUsuarioCreateForm
from .models import CustomUsuario,Pedidos_Exames,Notificacoes
# Create your views here.


class RegisterUserView(CreateView):
    form_class = CustomUsuarioCreateForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("home")  # URL para redirecionar após o sucesso

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.email = form.cleaned_data["username"]
        user.save()
        
        # Autentica e faz o login do usuário
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


class ForgotPasswordView(LoginRequiredMixin, View):
    template_name = "forgot_password.html"
    login_url = "login"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        usuario = CustomUsuario.objects.get(username=request.user)
        cpf_input = request.POST.get("cpf_name")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if cpf_input == usuario.cpf and new_password == confirm_password:
            usuario.set_password(new_password)
            usuario.save()
            return redirect("login")
        else:
            # Adicione uma mensagem de erro ou lógica adicional conforme necessário
            print("ERRO")
            return render(request, self.template_name)


'''
def forgot_password(request):
    if request.user.is_authenticated:
        print(request.user)
        usuario = CustomUsuario.objects.get(username=request.user)
        print(usuario)
        if request.method == 'POST':
            cpf_input = request.POST.get("cpf_name")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            print(cpf_input)
            print(usuario.cpf)
            if (cpf_input == usuario.cpf and new_password==confirm_password):
                usuario.set_password(new_password)
                usuario.save()
                return redirect("login")
            else:
                print("ERRO")


        return render(request, "forgot_password.html")
    
    else:
        return redirect("login")
'''    
