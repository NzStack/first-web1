from django.db import models

class Celular(models.Model):
    marca = models.TextField(max_length=15)
    modelo = models.TextField(max_length=30)
    precio = models.PositiveIntegerField(max_length=8)

    def __str__(self) :
        return self.marca + " " + self.modelo + " " + self.precio
