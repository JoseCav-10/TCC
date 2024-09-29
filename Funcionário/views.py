from django.shortcuts import render

def pedidos(request):
      return render(request, 'escola/pedidosadmin.html')

def menu(request):
      return render(request, 'escola/menuadmin.html')

def formuadmin(request): 
      return render(request, 'escola/formularioadmin.html')

def calendario(request):
      return render(request, 'escola/calendario.html')
