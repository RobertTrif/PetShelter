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
from django.contrib.auth.views import LoginView, LogoutView

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
    path('login/', wv.signup, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
