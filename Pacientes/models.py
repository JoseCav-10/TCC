from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser precisa ter is_superuser=True")
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser precisa ter is_staff=True")
        
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    SEXO_CHOICES = [
        ('Feminino', "Feminino"),
        ("Masculino", "Masculino"),
        ("Outro", "Outro"),
    ]

    email = models.EmailField("E-mail", unique=True)
    cpf = models.CharField("CPF", max_length=14, blank=True, null=True, unique=True)
    cartao_sus = models.CharField("Cartão do SUS", max_length=100, blank=True, null=True, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True, default=None)
    sexo = models.CharField("Sexo", choices=SEXO_CHOICES, max_length=20, blank=True, null=True, default=None)
    fone = models.CharField("Telefone", max_length=30, blank=True, null=True, default=None) 
    endereco = models.CharField("Endereço", max_length=255, blank=True, null=True, default=None)
    cep = models.CharField("CEP", max_length=9, blank=True, null=True, default=None)
    is_staff = models.BooleanField("Membro da Equipe", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    objects = UsuarioManager()


class Tipo_Exame(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


class Status_Exame(models.Model):
    EXAMES_CHOICES = [
        ("Pendente", "Pendente"),
        ("Aprovado", "Aprovado"),
        ("Recusado", "Recusado"),
    ]
    
    situacao = models.CharField(max_length=20, choices=EXAMES_CHOICES, default="Pendente")

    def __str__(self):
        return self.situacao
    

class Pedidos_Exames(models.Model):
    requerente = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    tipo_exame = models.ForeignKey(Tipo_Exame, on_delete=models.CASCADE)
    laudo = models.FileField(upload_to="media")
    dias_possiveis = models.CharField(max_length=20)
    dia_marcado = models.DateField()
    urgencia = models.BooleanField(default=False)
    situacao = models.ForeignKey(Status_Exame, on_delete=models.CASCADE)

    def __str__(self):
        return self.requerente


class Notificacoes(models.Model):
    destinatario = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    visualizacao = models.BooleanField(default=False)
    situacao = models.ForeignKey(Status_Exame, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField()
    conteudo = models.TextField()