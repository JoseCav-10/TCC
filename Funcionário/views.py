from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import UserChangeForm,UserCreationForm,CustomUsuarioCreateForm
from django.contrib.auth import authenticate
from .models import CustomUsuario


# Create your views here.

def register_user(request):
    form = CustomUsuarioCreateForm()

    if request.method == "POST":
        form = CustomUsuarioCreateForm(request.POST, request.FILES)
        print("oiiii")
        if form.is_valid():
            print("oiiii")
            form.save()

    context = {
        "form": form
    }
    return render(request, "registration/register.html", context)

def forgot_password(request):
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
        else:
            print("ERRO")


    return render(request, "forgot_password.html")