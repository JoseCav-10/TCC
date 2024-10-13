from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from stdimage import StdImageField
import uuid
# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


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

    email = models.EmailField(unique=True)
    cpf = models.CharField("CPF", max_length=14, blank=True, null=True, unique=True)
    name = models.CharField(max_length=255)
    cartao_sus = models.CharField("Cartão do SUS", max_length=100, blank=True, null=True, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True, default=None)
    sexo = models.CharField("Sexo", choices=SEXO_CHOICES, max_length=20, blank=True, null=True, default=None)
    fone = models.CharField("Telefone", max_length=30, blank=True, null=True, default=None) 
    endereco = models.CharField("Endereço", max_length=255, blank=True, null=True, default=None)
    cep = models.CharField("CEP", max_length=9, blank=True, null=True, default=None)
    foto_perfil = StdImageField(upload_to=get_file_path, variations={'thumb': {"width": 30, "height": 30, "crop": True}}, default="img/default.png", blank=True, null=True)
    is_staff = models.BooleanField("Membro da Equipe", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.name

    objects = UsuarioManager()

class Base(models.Model):
    criado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Tipo_Exame(Base):
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
    

class Pedidos_Exames(Base):

    requerente = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    tipo_exame = models.ForeignKey(Tipo_Exame, on_delete=models.CASCADE)
    laudo = models.FileField(upload_to="uploads_laudo/")
    dias_possiveis = models.CharField(max_length=50)
    dia_marcado = models.DateTimeField(blank=True, null=True)
    urgencia = models.BooleanField(default=False)
    situacao = models.ForeignKey(Status_Exame, on_delete=models.CASCADE)

    


class Notificacoes(Base):
    destinatario = models.ForeignKey(CustomUsuario, on_delete=models.CASCADE)
    visualizacao = models.BooleanField(default=False)
    situacao = models.ForeignKey(Status_Exame, on_delete=models.CASCADE)
    conteudo = models.TextField(default="Pedido confirmado")