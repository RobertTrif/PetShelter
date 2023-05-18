
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from principal.models import Centro, Trabajador, Cliente, Animal, Adopcion, Gato, Perro, Otro
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *

# Create your views here.
# create a simple view index
def index(request):
    return render(request, "index.html")

# print information of specific animal
def animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)

    return render(request, "animal.html", {'animal': animal})
    return render(request, "animal.html", {'animal': animal})

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


def administracion(request):
    return render(request, "administracion.html")

class RegistroClienteView(CreateView):
    model = WebUser
    form_class = RegistroNuevoCliente
    template_name = 'registro_cliente.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'cliente'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        web_user = form.save()
        login(self.request, web_user)
        return redirect('Index')
    
class RegistroTrabajadorView(CreateView):
    model = WebUser
    form_class = RegistroNuevoTrabajador
    template_name = 'registro_trabajador.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trabajador'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        web_user = form.save()
        login(self.request, web_user)
        return redirect('Index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'users/login.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                self.add_error(None, 'Incorrect username or password. Please try again.')
        return cleaned_data

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import  Gato, Perro, Otro
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test


def is_trabajador(user):
    return user.is_authenticated and user.is_trabajador

login_required_trabajador = user_passes_test(is_trabajador)

@login_required(login_url='pagina_no_encontrada')
def eliminar(request, animal_type):
    if animal_type == "Perro":
        AnimalModel = Perro
    elif animal_type == "Gato":
        AnimalModel = Gato
    elif animal_type == "Otro":
        AnimalModel = Otro
    else:
        AnimalModel = Animal

    animales = AnimalModel.objects.all()

    context = {"animales": animales, "animal_type": animal_type}
    return render(request, "eliminar.html", context)

@login_required(login_url='/pagina_no_encontrada')
def eliminar_confirmar(request, animal_type, animal_id):
    if animal_type == "Perro":
        AnimalModel = Perro
    elif animal_type == "Gato":
        AnimalModel = Gato
    elif animal_type == "Otro":
        AnimalModel = Otro
    else:
        AnimalModel = Animal

    animal = get_object_or_404(AnimalModel, pk=animal_id)
    animal.delete()

    messages.success(request, f"{animal.nombre} ha sido eliminado exitosamente.")
    return redirect("eliminar", animal_type=animal_type)


def pagina_no_encontrada(request):
    return render(request, 'pagina_no_encontrada.html')