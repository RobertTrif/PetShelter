from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from principal.models import Centro, Trabajador, Cliente, Animal, Adopcion, Gato, Perro, Otro

# Create your views here.
# create a simple view index
def index(request):
    return render(request, "index.html")

# print information of specific animal
def animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if (Perro.objects.filter(pk=animal_id).exists()):
        tipo = Perro.objects.get(pk=animal_id)
    elif (Gato.objects.filter(pk=animal_id).exists()):
        tipo = Gato.objects.get(pk=animal_id)
    elif (Otro.objects.filter(pk=animal_id).exists()):
        tipo = Otro.objects.get(pk=animal_id)

    return render(request, "animal.html", {'animal': animal, 'tipo': tipo})

def animales(request, animal_type):
    if (animal_type == "Perro"):
        animales = Perro.objects.all()
    elif (animal_type == "Gato"):
        animales = Gato.objects.all()
    elif (animal_type == "Otro"):
        animales = Otro.objects.all()
    elif (animal_type == "Animal"):
        animales = Animal.objects.all()

    return render(request, "animales.html", {"animales":animales})

def lista_animales(request):
    return render(request, 'lista_animales.html')

def centros(request):
    centros = Centro.objects.all()
    return render(request, "centros.html", {'centros':centros} )

def centro(request, centro_id):
    centro = Centro.objects.get(pk=centro_id)
    return render(request, "centro.html", {'centro':centro} )

