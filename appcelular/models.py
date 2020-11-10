from django.db import models

class Celular(models.Model):
    marca = models.TextField(max_length=15)
    modelo = models.TextField(max_length=30)
    precio = models.IntegerField()

    def __str__(self) :
        return self.marca + " " + self.modelo


class Cliente(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=50)

    def __str__(self) :
        return self.firstname + " " + self.lastname + " " + self.rut