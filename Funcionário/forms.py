from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUsuario, Pedidos_Exames


class CustomUsuarioCreateForm(UserCreationForm,forms.ModelForm):

    class Meta: 
        model = CustomUsuario
        fields = ("username", "name",'cpf','cartao_sus','data_nascimento','sexo','fone','endereco','cep', 'foto_perfil')
        labels = {"username": 'E-mail/User'}   
        widgets = {
            "username": forms.EmailInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "cartao_sus": forms.TextInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(attrs={"class": "form-control", "type": 'date'}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "fone": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "foto_perfil": forms.FileInput(attrs={"class": "form-control"}),

        }   

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


class Pedidos_ExamesForm(forms.ModelForm):

    class Meta:
        model = Pedidos_Exames
        fields = ("requerente","tipo_exame","laudo","urgencia","situacao")
        widgets = {
            "tipo_exame": forms.Select(attrs={"class": 'form-control select2'}),
            "laudo": forms.FileInput(attrs={"class": 'form-control'}),
            "urgencia": forms.CheckboxInput(attrs={"class": 'custom-switch-input'})
        }
        

    