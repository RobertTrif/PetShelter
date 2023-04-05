from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from .models import *
from .forms import *
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

def logout_view(request):
    logout(request)
    return redirect('login')