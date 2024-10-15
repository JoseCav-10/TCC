from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from Funcionário.models import CustomUsuario,Pedidos_Exames,Notificacoes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from Funcionário.forms import CustomUsuarioChangeForm
from Funcionário.forms import Pedidos_ExamesForm
# Create your views here.



class HomeView(LoginRequiredMixin, ListView):
    model = CustomUsuario
    template_name = "paciente_pages/home.html"
    context_object_name = "user"
    login_url = "/contas/login"

    def get_queryset(self):
        user = CustomUsuario.objects.get(username=self.request.user)
        return user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user)
        context["notificacao"] = notificacoes


        return context
        

class MeusDadosView(LoginRequiredMixin,UpdateView):
    template_name = "paciente_pages/meus_dados.html"  
    model = CustomUsuario     
    form_class = CustomUsuarioChangeForm
    login_url = "/contas/login"
    context_object_name = "pedidos"

    def get_success_url(self):
        return reverse('meu', kwargs={'pk': self.request.user.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model = Pedidos_Exames
        # Cria uma lista de IDs de pedidos aprovados
        context['pedidos'] = model.objects.filter(requerente=self.request.user)

        pedidos_list = model.objects.filter(requerente=self.request.user)

        # Configurar paginação
        page = self.request.GET.get('page', 1)
        paginator = Paginator(pedidos_list, 5)  # 5 pedidos por página

        try:
            pedidos = paginator.page(page)
        except PageNotAnInteger:
            pedidos = paginator.page(1)  # Se a página não for um número inteiro, retorna a primeira
        except EmptyPage:
            pedidos = paginator.page(paginator.num_pages)  # Se a página estiver fora do intervalo, retorna a última

        context['pedidos'] = pedidos

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user)
        context["notificacao"] = notificacoes

        return context


class FormAgendamentoView(LoginRequiredMixin,CreateView):
    model = Pedidos_Exames
    template_name = "paciente_pages/fomu.html"
    context_object_name = "user"
    form_class = Pedidos_ExamesForm
    success_url = reverse_lazy("form")
    login_url = "/contas/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context["user"] = user

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user)
        context["notificacao"] = notificacoes

        return context
    
    def form_valid(self, form):
        print("VALIDO")
        tipo_exame = form.cleaned_data['tipo_exame']
        laudo = form.cleaned_data['laudo']
        urgencia = form.cleaned_data['urgencia']
        requerente = form.cleaned_data["requerente"]
        first_data = self.request.POST["first_data"]
        second_data = self.request.POST["second_data"]
        dias_possiveis = f"{first_data},{second_data}"
        situacao = form.cleaned_data["situacao"]

        print(tipo_exame,requerente)

        Pedidos_Exames.objects.create(requerente=requerente,tipo_exame=tipo_exame,laudo=laudo,urgencia=urgencia,dias_possiveis=dias_possiveis,situacao=situacao)

        return super().form_valid(form)


class AndamentoView(LoginRequiredMixin, ListView):
    model = Pedidos_Exames
    template_name = "paciente_pages/andamento.html"  # Template a ser utilizado
    context_object_name = 'objetos'  # Nome do contexto para a lista de objetos
    paginate_by = 4
    ordering = "-id"
    login_url = "/contas/login"

    def get_queryset(self):
        # Filtra os pedidos com base no usuário logado
        return super().get_queryset().filter(requerente=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cria uma lista de IDs de pedidos aprovados
        context['aprovados'] = [
            pedido.id for pedido in context['objetos'] if pedido.situacao.situacao == "Aprovado"
        ]

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user)
        context["notificacao"] = notificacoes

        return context


class DeleteFormView(LoginRequiredMixin,DeleteView):
    model = Pedidos_Exames
    template_name = "paciente_pages/del_form.html"
    success_url = reverse_lazy("anda")
    login_url = "/contas/login"


class DetailsPedidosExamesView(LoginRequiredMixin,DetailView):
    template_name = "paciente_pages/details_form.html"
    model = Pedidos_Exames
    context_object_name = "pedidos"
    login_url = "/contas/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user)
        context["notificacao"] = notificacoes

        return context

