from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    plataforma = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
