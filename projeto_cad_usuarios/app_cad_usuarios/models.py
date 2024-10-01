from django.db import models


#transformar codigo python em SQL
class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.IntegerField()  # Em horas

    def __str__(self):
        return self.nome
