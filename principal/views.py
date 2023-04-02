from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from principal.models import Centro, Trabajador, Cliente, Animal, Adopcion, Gato, Perro, Otro

# Create your views here.
# create a simple view index
def index(request):
    animals = Animal.objects.all()
    return render(request, "index.html", {'animals': animals})

# print information of specific animal
def animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return render(request, "animal.html", {'animal': animal})
