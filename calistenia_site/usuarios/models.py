from django.db import models
from django.contrib.auth.models import User

# Registro de peso corporal ao longo do tempo
class PesoCorporal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    peso = models.FloatField()  # em kg

    def __str__(self):
        return f"{self.usuario.username} - {self.peso}kg em {self.data}"


# Treinos realizados
class Treino(models.Model):
    TIPOS = [
        ("PUSH", "Push"),
        ("PULL", "Pull"),
        ("LEGS", "Pernas"),
        ("FS", "Freestyle"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPOS)
    exercicio = models.CharField(max_length=100)
    series = models.IntegerField()
    reps_por_serie = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.exercicio} ({self.tipo})"


# Marcos importantes atingidos
class Marco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.nome}"


# Plano alimentar (metas de macros)
class PlanoAlimentar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # 1 plano por usuário
    calorias_meta = models.IntegerField()
    proteinas_meta = models.FloatField()  # gramas
    carboidratos_meta = models.FloatField()
    gorduras_meta = models.FloatField()

    def __str__(self):
        return f"Plano alimentar de {self.usuario.username}"


# Alimentos (opcional, se você quiser cadastrar os alimentos do usuário)
class Alimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # null = alimento global
    nome = models.CharField(max_length=100)
    calorias = models.FloatField()  # por 100g
    proteinas = models.FloatField()
    carboidratos = models.FloatField()
    gorduras = models.FloatField()

    def __str__(self):
        return self.nome


# Cronograma de treinos (agenda semanal)
class Cronograma(models.Model):
    DIAS = [
        ("SEG", "Segunda"),
        ("TER", "Terça"),
        ("QUA", "Quarta"),
        ("QUI", "Quinta"),
        ("SEX", "Sexta"),
        ("SAB", "Sábado"),
        ("DOM", "Domingo"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=3, choices=DIAS)
    tipo_treino = models.CharField(max_length=10, choices=Treino.TIPOS)

    def __str__(self):
        return f"{self.usuario.username} - {self.get_dia_semana_display()} - {self.get_tipo_treino_display()}"
