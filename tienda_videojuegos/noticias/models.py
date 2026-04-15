from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
