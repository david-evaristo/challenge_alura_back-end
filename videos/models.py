from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=30, blank=False)
    cor = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.titulo
