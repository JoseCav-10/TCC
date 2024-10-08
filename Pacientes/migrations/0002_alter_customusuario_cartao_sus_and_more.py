# Generated by Django 5.1 on 2024-08-12 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='cartao_sus',
            field=models.CharField(default='0000 0000 0000 0000', max_length=100, verbose_name='Cartão do SUS'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='cep',
            field=models.CharField(default='00000-000', max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='data_nascimento',
            field=models.DateField(default='2000-01-01', verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='endereco',
            field=models.CharField(default='Rua', max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='fone',
            field=models.CharField(default='(00) 0000-0000', max_length=30, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='sexo',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], default='Outro', max_length=20, verbose_name='Sexo'),
        ),
    ]
