from django.contrib import admin
from .models import Centro,Trabajador,Cliente,Animal,Adopcion,Gato,Perro,Otro
# Register your models here.
admin.site.register(Centro)
admin.site.register(Trabajador)
admin.site.register(Cliente)
admin.site.register(Animal)
admin.site.register(Adopcion)
admin.site.register(Gato)
admin.site.register(Perro)
admin.site.register(Otro)