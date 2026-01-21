from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=200)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Inscricao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} inscrito em {self.evento.titulo}"