from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioChangeForm, CustomUsuarioCreateForm
from .models import CustomUsuario, Notificacoes, Pedidos_Exames, Tipo_Exame, Status_Exame
# Register your models here.

admin.site.register(Tipo_Exame)


admin.site.register(Status_Exame)


class Pedidos_ExamesAdmin(admin.ModelAdmin):
    list_display = ("requerente", "dia_marcado", 'urgencia', "situacao")

admin.site.register(Pedidos_Exames, Pedidos_ExamesAdmin)


class NotificacoesAdmin(admin.ModelAdmin):
    list_display = ('destinatario', 'visualizacao', 'situacao')

admin.site.register(Notificacoes, NotificacoesAdmin)


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin): 
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ("username","email", "name","cpf", 'is_staff', "is_active")
    fieldsets = (
        (None, {'fields': ('email',"username", "password")}),
        ("Informações Pessoais", {'fields': ("name", 'cpf', 'cartao_sus', 'data_nascimento', 'sexo', "fone", "endereco", "cep","foto_perfil")}), 
        ("Permissões", {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Datas Importantes", {'fields': ("last_login", "date_joined")}),
    )
    labels = {"username": 'E-mail'}

