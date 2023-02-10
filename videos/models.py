from django.db import models

# Create your models here.

class Video(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
