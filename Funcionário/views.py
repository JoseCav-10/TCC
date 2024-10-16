from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import CustomUsuarioCreateForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUsuarioCreateForm
from .models import CustomUsuario,Pedidos_Exames,Notificacoes,Status_Exame
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
            print("ok")
            login(self.request, user)
            print(self.request.user)
            redirect("home")

        return super().form_valid(form)


class ForgotPasswordView(LoginRequiredMixin, View):
    template_name = "registration/forgot_password.html"
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


class CalendarioView(LoginRequiredMixin,ListView):
    template_name = "funcionario_pages/calendario.html"
    model = Pedidos_Exames
    context_object_name = "pedidos_aprovados"
    login_url = "contas/login"
    paginate_by = 5
    ordering = "id"

    def get_queryset(self):
        urgencia = self.request.GET.get('urgencia')
        situacao = Status_Exame.objects.get(id=2)
        queryset = Pedidos_Exames.objects.filter(situacao=situacao)

        if urgencia == '1':
            queryset = queryset.filter(urgencia=True)
        elif urgencia == '0':
            queryset = queryset.filter(urgencia=False)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aqui você constrói o dicionário de datas como antes.
        situacao = Status_Exame.objects.get(id=2)
        pedidos = Pedidos_Exames.objects.filter(situacao=situacao)
        
        # Resto do seu código para adicionar as datas ao contexto
        context['datas'] = self.build_data_dictionary(pedidos)
        return context
    
    def build_data_dictionary(self, pedidos):
        dicionaryDatas = {}
        listDatas = []
        listMeses = []
        listNumMeses = []
        meses_impressos = set()
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        
        for i in pedidos:
            mes = i.dia_marcado.month
            if mes not in meses_impressos:
                mesNome = meses[mes - 1]
                listNumMeses.append(mes)
                listMeses.append(mesNome)
                meses_impressos.add(mes)
        
        valor = 0
        for j in listNumMeses:
            for l in pedidos:
                if l.dia_marcado.month == j:
                    listDatas.append(l.dia_marcado.day)
            dicionaryDatas[listMeses[valor]] = listDatas
            listDatas = []
            valor += 1
        
        return dicionaryDatas
        
    
    def post(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        

        situacao = Status_Exame.objects.get(id=4)
        id = request.POST.get("pk")
        print(id)
        pedido = Pedidos_Exames.objects.get(id=id)
        print(pedido)

        pedido.situacao = situacao
        pedido.save()

        return redirect("calendario")


class DetailsPedidosExamesFuncView(LoginRequiredMixin,DetailView):
    template_name = "funcionario_pages/details_form.html"
    model = Pedidos_Exames
    context_object_name = "pedidos"
    login_url = "/contas/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class FormFuncionarioView(LoginRequiredMixin, DetailView):
    template_name = "funcionario_pages/formularioadmin.html"
    model = Pedidos_Exames
    context_object_name = "pedido"
    login_url = "contas/login"

    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = super().get_context_data(**kwargs)

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = super().get_context_data(**kwargs)
        pedido = context['pedido']


        embasar = request.POST.get("embasamento")
        situ = request.POST.get("situacao")
        situacao = Status_Exame.objects.get(id=situ)
        print(situacao)
        
        if embasar == "confirmar":
            dia_marcado = request.POST.get("dia_marcado")
            pedido.dia_marcado = dia_marcado
            pedido.situacao = situacao
            pedido.save()

            Notificacoes.objects.create(destinatario=pedido.requerente,pedido=pedido,situacao=situacao)

            return redirect("pedidos")
        
        elif embasar == "recusar":
            pedido.situacao = situacao
            pedido.save()

            motivo = request.POST.get("motivo")
            Notificacoes.objects.create(destinatario=pedido.requerente,pedido=pedido,situacao=situacao,conteudo=motivo)

            return redirect("pedidos")
        
        else:

            return redirect("pedido")


class MenuFuncionarioView(LoginRequiredMixin, View):
    template_name = "funcionario_pages/menuadmin.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PedidoAFuncionarioView(LoginRequiredMixin, ListView):
    template_name = "funcionario_pages/pedidosadmin.html"
    model = Pedidos_Exames
    context_object_name = "pedidos"
    

    def get_queryset(self):
        pedidos = Pedidos_Exames.objects.filter(situacao=1)
        print(pedidos)

        return pedidos

#Falta: feito(paginação), filtro, concluir    
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
