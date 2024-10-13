from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import UserChangeForm,UserCreationForm,CustomUsuarioCreateForm,Pedidos_ExamesForm
from django.contrib.auth import authenticate, login
from .models import CustomUsuario,Pedidos_Exames


# Create your views here.




def testes(request):
    pedidos = Pedidos_Exames.objects.filter(requerente=request.user)
    lista_aprovados = []

    for i in pedidos:
        if i.situacao.situacao == "Aprovado":
            lista_aprovados.append(i.id)

    print(lista_aprovados)
    context = {
        'objetos': pedidos,
        'aprovados': lista_aprovados
    }

    return render(request, "paciente_pages/andamento.html", context)


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