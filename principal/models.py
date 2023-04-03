from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class WebUser(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_trabajador = models.BooleanField(default=False)

class Centro(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)

class Trabajador(models.Model):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=40,blank=False,null=False)
    apellidos = models.CharField(max_length=40,blank=False,null=False)
    departamento = models.CharField(max_length=256)
    adresa = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Cliente(models.Model):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=40,blank=False,null=False)
    apellidos = models.CharField(max_length=40,blank=False,null=False)
    telefono = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    anos = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)

class Animal(models.Model):
    nombre = models.CharField(max_length=256)
    peso = models.IntegerField()
    color = models.CharField(max_length=256)
    adoptado = models.BooleanField()

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

class Gato(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Perro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

class Otro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
