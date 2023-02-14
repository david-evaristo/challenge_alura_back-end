from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    cor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=30, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=50, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default=1, blank=False)

    def __str__(self):
        return self.titulo
