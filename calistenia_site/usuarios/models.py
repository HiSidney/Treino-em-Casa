from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # data_nascimento = models.DateField(null=True, blank=True)
    # peso = models.FloatField(null=True, blank=True)
    # altura = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    
class ProgressoPeso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    peso = models.FloatField()  # em kg

    def __str__(self):
        return f"{self.usuario.username} - {self.peso}kg em {self.data}"


class ProgressoTreino(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    exercicio = models.CharField(max_length=100)
    series = models.IntegerField()
    repeticoes = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.exercicio}"


class Marco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)  # Ex: "Primeira barra"
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.nome}"
