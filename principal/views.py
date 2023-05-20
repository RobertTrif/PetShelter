from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import user_passes_test
import requests
import json
import json
from urllib.request import urlopen

import json
import requests

import requests

def animal_details(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if Perro.objects.filter(pk=animal_id).exists():
        tipo = Perro.objects.get(pk=animal_id)
    elif Gato.objects.filter(pk=animal_id).exists():
        tipo = Gato.objects.get(pk=animal_id)
    elif Otro.objects.filter(pk=animal_id).exists():
        tipo = Otro.objects.get(pk=animal_id)

    if Gato.objects.filter(pk=animal_id).exists():
        breed_name = tipo.raza  # Assuming "raza" represents the breed name for a cat
        breed_type = 'cat'
    elif Perro.objects.filter(pk=animal_id).exists():
        breed_name = tipo.raza  # Assuming "raza" represents the breed name for a dog
        breed_type = 'dog'
    else:
        breed_name = None
        breed_type = None

    breed_info = {}
    image_url = None  # Initialize the image URL variable

    if breed_name:
        breed_search_url = f'https://api.thedogapi.com/v1/breeds/search?q={breed_name}&limit=1&api_key=live_zzGlFfnyqVgP7Lz69AOcfObQvaUcbJdTEB6j5uZ8kfPK5eGyJyvEjHUxHBBZwjyv'
        response = requests.get(breed_search_url)
        if response.status_code == 200:
            breed_info_list = response.json()
            if breed_info_list:
                breed_info = breed_info_list[0]
                image_url = get_image_url(breed_info['reference_image_id'])  # Obtain the image URL

    context = {
        'animal': animal,
        'breed_info_json': breed_info,
        'tipo': tipo,
        'image_url': image_url,  # Add the image URL to the context
    }

    return render(request, "animal_details.html", context)


def get_image_url(image_id):
    image_url = ''
    image_info_url = f'https://api.thedogapi.com/v1/images/{image_id}'
    response = requests.get(image_info_url)
    if response.status_code == 200:
        image_info = response.json()
        if image_info and 'url' in image_info:
            image_url = image_info['url']
    print("Image URL:", image_url)       
    return image_url




#html request
def api(request):
    return render(request, "APi-pages/pagination-cat.html")

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def administracion(request):
    if request.user.is_trabajador:
        return render(request, "administracion.html")
    else:
        return redirect('/login')
    
class Crear_perro(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'login'
    model = Perro
    template_name = 'new_animal.html'
    form_class = NewPerro
    def test_func(self):
        return self.request.user.is_trabajador
    def handle_no_permission(self):
        return redirect('/login')

class Crear_gato(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'login'
    model = Gato
    template_name = 'new_animal.html'
    form_class = NewGato
    def test_func(self):
        return self.request.user.is_trabajador
    def handle_no_permission(self):
        return redirect('/login')

class Crear_otro(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'login'
    model = Otro
    template_name = 'new_animal.html'
    form_class = NewOtro
    def test_func(self):
        return self.request.user.is_trabajador
    def handle_no_permission(self):
        return redirect('/login')

class Crear_centro(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'login'
    model = Centro
    template_name = 'new_animal.html'
    form_class = NewCentro
    def test_func(self):
        return self.request.user.is_trabajador
    def handle_no_permission(self):
        return redirect('/login')
   
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

@login_required(login_url='login')
def updateAnimal(request, pk):
    if request.user.is_trabajador:
        animal = None
        form = None
        try:
            animal = Perro.objects.get(id=pk)
            form = NewPerro(instance=animal)
        except Perro.DoesNotExist:
            try:
                animal = Gato.objects.get(id=pk)
                form = NewGato(instance=animal)
            except Gato.DoesNotExist:
                try:
                    animal = Otro.objects.get(id=pk)
                    form = NewOtro(instance=animal)
                except Otro.DoesNotExist:
                    animal = None
        if animal is None:
            return redirect('/')
        if request.method == 'POST':
            if isinstance(animal, Perro):
                form = NewPerro(request.POST, instance=animal)
            elif isinstance(animal, Gato):
                form = NewGato(request.POST, instance=animal)
            elif isinstance(animal, Otro):
                form = NewOtro(request.POST, instance=animal)
            form.instance.id = pk
            if form.is_valid():
                form.save()
                return redirect('/animal/'+str(pk))
        context = {'form': form}
        return render(request, 'edit_animal.html', context)
    else:
        return redirect('/')

@login_required(login_url='login')
def updateCentro(request, pk):
    if request.user.is_trabajador:
        centro = Centro.objects.get(id=pk)
        form = NewCentro(instance=centro)
        if request.method == 'POST':
            form = NewCentro(request.POST, instance=centro)
            form.instance.id = pk
            if form.is_valid():
                form.save()
                return redirect('/centro/'+str(pk))
        context = {'form': form}
        return render(request, 'edit_centro.html', context)
    else:
        return redirect('/')

@login_required(login_url='login')
def updateUser(request):
    user = None
    form = None
    try:
        user = Cliente.objects.get(User_id=request.user.id)
        form = updateCliente(instance=user)
    except Cliente.DoesNotExist:
        try:
            user = Trabajador.objects.get(User_id=request.user.id)
            form = updateTrabajador(instance=user)
        except Trabajador.DoesNotExist:
            user = None
    if user is None:
        return redirect('/')
    if request.method == 'POST':
        if isinstance(user, Cliente):
            form = updateCliente(request.POST, instance=user)
        elif isinstance(user, Trabajador):
            form = updateTrabajador(request.POST, instance=user)
        form.instance.id = request.user.id
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'edit_user.html', context)

@login_required(login_url='login')
def updatePassword(request):
    
    user_id = request.user.id
    print(user_id)
    user = WebUser.objects.get(id=request.user.id)
    form = updatePasswordForm(instance=user)
    if request.method == 'POST':
        form = NewCentro(request.POST, instance=centro)
        form.instance.id = pk
        if form.is_valid():
            form.save()
            return redirect('/centro/'+str(pk))
    context = {'form': form}
    return render(request, 'edit_centro.html', context)
    
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
    elif animal_type == "Centro":
        AnimalModel = Centro
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
    elif animal_type == "Centro":
        AnimalModel = Centro    
    else:
        AnimalModel = Animal

    animal = get_object_or_404(AnimalModel, pk=animal_id)
    animal.delete()

    messages.success(request, f"{animal.nombre} ha sido eliminado exitosamente.")
    return redirect("eliminar", animal_type=animal_type)


def pagina_no_encontrada(request):
    return render(request, 'pagina_no_encontrada.html')