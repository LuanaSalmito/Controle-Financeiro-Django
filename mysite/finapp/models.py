from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    senha = models.CharField(max_length=40)
    data_nascimento = models.DateField()


    genero_escolha = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
    ]
    genero = models.CharField(max_length=15, choices=genero_escolha)


    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.email}"



class Balanco(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    saldoInicio = models.DecimalField(max_digits=10, decimal_places=2)

    periodo_escolha = [
        ('15 dias', '15 dias'),
        ('30 dias', '30 dias'),
    ]

    periodo = models.CharField(max_length=15, choices = periodo_escolha)
    


class Receita(models.Model):

    balanco = models.ForeignKey(Balanco, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    


class Despesa(models.Model):

    balanco = models.ForeignKey(Balanco, on_delete=models.CASCADE)

    descricao = models.CharField(max_length=255)

    valor = models.DecimalField(max_digits=30, decimal_places=2)

    data = models.DateField()

    foto = models.ImageField(upload_to='fotos/despesas')

   
    despesa_escolha = [
        ('Alimentação', 'Alimentação'),
        ('Transporte', 'Transporte'),
        ('Moradia', 'Moradia'),
        ('Filhos', 'Filhos'),
        ('Comunicação', 'Comunicação'),
        ('Saúde', 'Saúde'),
        ('Outros', 'Outros'),
        ('Despesa recorrente', 'Despesa recorrente'),
    ] 
    tipo = models.CharField(max_length=255, choices=despesa_escolha)

class HistoricoBalanco(models.Model):


    balanco = models.ForeignKey(Balanco, on_delete=models.CASCADE)

    date = models.DateField()

    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    receitas = models.ManyToManyField(Receita)

    despesas = models.ManyToManyField(Despesa)
