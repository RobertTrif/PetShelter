"""petshelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import principal.views as wv

import principal.forms as form
from django.contrib.auth import views as auth_views
from principal.views import CustomLoginView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
import principal.models as model
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.urls import path
from principal.views import  eliminar_confirmar , eliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', wv.index, name='Index'),
    path ('animal/<int:animal_id>', wv.animal, name='Animal'),
    path ('animales/<str:animal_type>', wv.animales, name='Animales'),
    path ('lista_animales/', wv.lista_animales, name='Lista_animales'),
    path ('centros/', wv.centros, name='Centros'),
    path ('centro/<int:centro_id>', wv.centro, name='Centro'),
    path ('registro_cliente/', wv.RegistroClienteView.as_view(), name='Registro_cliente'),
    path ('registro_trabajador/', wv.RegistroTrabajadorView.as_view(), name='Registro_trabajador'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('administracion/', wv.administracion, name='Administracion'),
    # Crear de animales 
    path('administracion/crear_perro/', 
         CreateView.as_view(model=model.Perro, template_name = 'new_animal.html', form_class = form.NewPerro),
         name='New_perro'),
    path('administracion/crear_gato/', 
         CreateView.as_view(model=model.Gato, template_name = 'new_animal.html', form_class = form.NewGato),
         name='New_gato'),
    path('administracion/crear_otro/', 
         CreateView.as_view(model=model.Otro, template_name = 'new_animal.html', form_class = form.NewOtro),
         name='New_otro'),
    path('administracion/crear_centro/', 
         CreateView.as_view(model=model.Centro, template_name = 'new_animal.html', form_class = form.NewCentro),
         name='New_centro'),
    path('administracion/<int:pk>', DetailView.as_view(model= model.Animal, template_name='animal_creado.html'), name='Animal_creado'),
    
    # Elliminacion de animales 
    path('administracion/eliminar_animal/<str:animal_type>/', eliminar, name='eliminar'),
    path('administracion/<int:pk>', DetailView.as_view(model= model.Animal, template_name='animal_creado.html'), name='Animal_creado'),
    path('administracion/eliminar_animal/<str:animal_type>/<int:animal_id>/', wv.eliminar_confirmar, name='eliminar_confirmar'),
    path('pagina_no_encontrada/', wv.pagina_no_encontrada, name='pagina_no_encontrada'),
   
]
