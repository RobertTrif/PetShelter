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


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', wv.index, name='Index'),
    path ('animal/<int:animal_id>', wv.animal_details, name='Animal'),
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
    path('administracion/crear_perro/', wv.Crear_perro.as_view(), name='New_perro'),
    path('administracion/crear_gato/', wv.Crear_gato.as_view(), name='New_gato'),
    path('administracion/crear_otro/', wv.Crear_otro.as_view(), name='New_otro'),
    path('administracion/crear_centro/', wv.Crear_centro.as_view(),name='New_centro'),
    path('administracion/animal_creado/<int:pk>', DetailView.as_view(model= model.Animal, template_name='animal_creado.html'), name='Animal_creado'),
    path('animal_edit/<str:pk>/', wv.updateAnimal, name='edit_animal'),
    path('centro_edit/<str:pk>/', wv.updateCentro, name='edit_centro'),
    path('edit_user/', wv.updateUser, name='edit_user'),
    path('edit_password/', wv.updatePassword, name='edit_password'),
    path('administracion/centro_creado/<int:pk>', DetailView.as_view(model= model.Centro, template_name='centro_creado.html'), name='Centro_creado'),
    path('api/', wv.api, name='API'),

    # Elliminacion de animales 
    path('administracion/eliminar_animal/<str:animal_type>/', wv.eliminar, name='eliminar'),
    path('administracion/<int:pk>', DetailView.as_view(model= model.Animal, template_name='animal_creado.html'), name='Animal_creado'),
    path('administracion/eliminar_animal/<str:animal_type>/<int:animal_id>/', wv.eliminar_confirmar, name='eliminar_confirmar'),
    path('pagina_no_encontrada/', wv.pagina_no_encontrada, name='pagina_no_encontrada'),
    path('administracion/centro_creado/<int:pk>', DetailView.as_view(model= model.Centro, template_name='centro_creado.html'), name='Centro_creado'),
]
