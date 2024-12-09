from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView,DetailView,View
from django.shortcuts import redirect,render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from Funcionário.models import CustomUsuario,Pedidos_Exames,Notificacoes
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from Funcionário.forms import CustomUsuarioChangeForm,Pedidos_ExamesForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.


@csrf_exempt
def marcar_visualizacao(request):
    if request.method == 'POST':
        try:
            notificacao_id = request.POST.get('notificacao_id')
            notificacao = Notificacoes.objects.get(id=notificacao_id)
            notificacao.visualizacao = True
            notificacao.save()
            return JsonResponse({'status': 'success', 'message': 'Notificação marcada como visualizada!'})
        except Notificacoes.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notificação não encontrada!'})
    return JsonResponse({'status': 'error', 'message': 'Requisição inválida!'})


def marcar_todas_como_lidas(request, destinatario_id):
    if request.method == 'POST':

        # Filtra todas as notificações que pertencem ao destinatário (usuário)
        Notificacoes.objects.filter(destinatario=request.user, visualizacao=False).update(visualizacao=True)
        return JsonResponse({'status': 'success', 'message': 'Notificações marcadas como lidas!'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


class HomeView(LoginRequiredMixin, View):
    template_name = "paciente_pages/home.html"
    login_url = "/contas/login/"

    def get(self, request, *args, **kwargs):
        # Obter o usuário atual e as notificações associadas
        user = request.user

        if user.groups.filter(name="funcionarios").exists():
            return redirect("menu")
        else:
            # Filtrar apenas as notificações que pertencem ao usuário atual
            notificacoes = Notificacoes.objects.filter(destinatario=user, visualizacao=False)
            
            # Criar o contexto com o usuário e as notificações
            context = {
                "user": user,
                "notificacoes": notificacoes  # Corrigi o nome para plural
            }
            
            return render(request, self.template_name, context)    


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
        notificacoes = model.objects.filter(destinatario=self.request.user, visualizacao=False)
        context["notificacoes"] = notificacoes

        return context


class FormAgendamentoView(LoginRequiredMixin,CreateView):
    model = Pedidos_Exames
    template_name = "paciente_pages/fomu.html"
    context_object_name = "user"
    form_class = Pedidos_ExamesForm
    login_url = "/contas/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        context["user"] = user

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user, visualizacao=False)
        context["notificacoes"] = notificacoes

        return context
    
    def get_success_url(self):

        return reverse_lazy("anda")
    
    
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

        
        Pedidos_Exames.objects.create(requerente=requerente,tipo_exame=tipo_exame,laudo=laudo,urgencia=urgencia,dias_possiveis=dias_possiveis,situacao=situacao)
        print("Pedido feito")
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        # Adiciona uma mensagem de erro que será exibida no template
        messages.error(self.request, "Houve um erro ao processar o formulário. Verifique os campos e tente novamente.")
        return super().form_invalid(form)


class AndamentoView(LoginRequiredMixin, ListView):
    model = Pedidos_Exames
    template_name = "paciente_pages/andamento.html"  # Template a ser utilizado
    context_object_name = 'objetos'  # Nome do contexto para a lista de objetos
    paginate_by = 6
    ordering = "id"
    login_url = "/contas/login"

    def get_queryset(self):
        # Filtra os pedidos com base no usuário logado
        filtrado = super().get_queryset().filter(requerente=self.request.user)
        
        return filtrado 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cria uma lista de IDs de pedidos aprovados
        context['aprovados'] = [
            pedido.id for pedido in context['objetos'] if pedido.situacao.situacao == "Aprovado"
        ]

        model = Notificacoes
        notificacoes = model.objects.filter(destinatario=self.request.user, visualizacao=False)
        context["notificacoes"] = notificacoes

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
        notificacoes = model.objects.filter(destinatario=self.request.user, visualizacao=False)
        context["notificacoes"] = notificacoes

        return context

