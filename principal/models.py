from django.db import models

# Create your models here.
class Centro(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=256)
    departamento = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=256)

class Animal(models.Model):
    nombre = models.CharField(max_length=256)
    peso = models.IntegerField()
    color = models.CharField(max_length=256)

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

class Gato(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)

class Perro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)

class Otro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
