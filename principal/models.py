from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class WebUser(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_trabajador = models.BooleanField(default=False)

class Centro(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.nombre)
    
    def get_absolute_url(self):
        return reverse('Centro_creado', kwargs={'pk':self.pk})

class Horario(models.Model):
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    dia_semana = models.DecimalField(max_digits=1, decimal_places=0, blank=False,null=False)
    dia = models.CharField(max_length=20)
    abierto = models.BooleanField(default=False)
    apertura = models.TimeField(auto_now=False, auto_now_add=False)
    cierre = models.TimeField(auto_now=False, auto_now_add=False)

class Trabajador(models.Model):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=40,blank=False,null=False)
    apellidos = models.CharField(max_length=40,blank=False,null=False)
    telefono = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    departamento = models.CharField(max_length=256)
    adresa = models.CharField(max_length=256)
    anos = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre + " " + self.apellidos)

class Cliente(models.Model):
    User = models.OneToOneField(WebUser, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=40,blank=False,null=False)
    apellidos = models.CharField(max_length=40,blank=False,null=False)
    telefono = models.DecimalField(max_digits=9, decimal_places=0, blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    anos = models.DecimalField(max_digits=3, decimal_places=0, blank=False,null=False)
    
    def __str__(self):
        return str(self.nombre + " " + self.apellidos)

class Animal(models.Model):
    nombre = models.CharField(max_length=256)
    peso = models.IntegerField()
    color = models.CharField(max_length=256)
    adoptado = models.BooleanField()

    def __str__(self):
        return str(self.nombre)

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.animal.nombre + " -- " + self.cliente.nombre)

class Gato(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Animal_creado', kwargs={'pk':self.pk})

class Perro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Animal_creado', kwargs={'pk':self.pk})

class Otro(Animal):
    raza = models.CharField(max_length=256)
    pelaje = models.CharField(max_length=256)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Animal_creado', kwargs={'pk':self.pk})
