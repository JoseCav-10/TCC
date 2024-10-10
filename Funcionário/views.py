from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import UserChangeForm,UserCreationForm,CustomUsuarioCreateForm,Pedidos_ExamesForm
from django.contrib.auth import authenticate, login
from .models import CustomUsuario,Pedidos_Exames


# Create your views here.

def testes(request):
    form = Pedidos_ExamesForm()
    user = CustomUsuario.objects.get(username=request.user)
    if request.method == "POST":
        form = Pedidos_ExamesForm(request.POST, request.FILES)
        print("POST")
        print(request.POST)
        if form.is_valid():
            print("VALIDO")
            tipo_exame = form.cleaned_data['tipo_exame']
            laudo = form.cleaned_data['laudo']
            urgencia = form.cleaned_data['urgencia']
            requerente = form.cleaned_data["requerente"]
            first_data = request.POST["first_data"]
            second_data = request.POST["second_data"]
            dias_possiveis = f"{first_data},{second_data}"
            situacao = form.cleaned_data["situacao"]

            Pedidos_Exames.objects.create(requerente=requerente,tipo_exame=tipo_exame,laudo=laudo,urgencia=urgencia,dias_possiveis=dias_possiveis,situacao=situacao)

    context = {
        "form": form,
        "user": user
    }

    return render(request, "registration/register copy.html", context)


def register_user(request):
    form = CustomUsuarioCreateForm()

    if request.method == "POST":
        form = CustomUsuarioCreateForm(request.POST, request.FILES)
        print("oiiii")
        if form.is_valid():
            print("oiiii")
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    context = {
        "form": form
    }
    return render(request, "registration/register.html", context)

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