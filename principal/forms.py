from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *
import datetime

class RegistroNuevoCliente(UserCreationForm):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    apellidos = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    telefono = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    anos = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = WebUser

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_cliente = True
        web_user.save()
        nuevoCliente = Cliente.objects.create(
            User=web_user, nombre=self.data.get("nombre"),apellidos=self.data.get("apellidos"), telefono=self.data.get('telefono'), email= self.data.get('email'),
            anos=self.data.get('anos'))
        nuevoCliente.save()
        return web_user
    
class RegistroNuevoTrabajador(UserCreationForm):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    apellidos = forms.CharField(max_length=40, widget=forms.TextInput, required=True)
    telefono = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    departamento = forms.CharField(max_length=256, required=True)
    anos = forms.IntegerField(required=True)
    adresa = forms.CharField(max_length=256, required=True)
    centro = forms.ModelChoiceField(queryset=Centro.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):
        model = WebUser

    @transaction.atomic
    def save(self):
        web_user = super().save(commit=False)
        web_user.is_trabajador = True
        web_user.save()
        centro = Centro.objects.get(pk=self.data.get('centro'))
        nuevoTrabajador = Trabajador.objects.create(
            User=web_user, nombre=self.data.get("nombre"),apellidos=self.data.get("apellidos"),telefono=self.data.get("telefono"),email=self.data.get("email"),anos=self.data.get("anos"), departamento=self.data.get('departamento'), adresa= self.data.get('adresa'),
            centro=centro)
        nuevoTrabajador.save()
        return web_user