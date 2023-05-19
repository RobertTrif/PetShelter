from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
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
    