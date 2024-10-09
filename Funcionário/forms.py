from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm,forms.ModelForm):

    class Meta: 
        model = CustomUsuario
        fields = ("username", "name",'cpf','cartao_sus','data_nascimento','sexo','fone','endereco','cep', 'foto_perfil')
        labels = {"username": 'E-mail/User'}      

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user
        

class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ("username", "name",'cpf','cartao_sus','data_nascimento','sexo','fone','endereco','cep', 'foto_perfil')
        labels = {"username": 'Username/E-mail'}

