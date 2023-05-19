from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.db import transaction
from .models import *
from django.forms import ModelForm

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

class NewPerro(ModelForm):
    class Meta:
        model = Perro
        fields = "__all__"
        exclude = ()

class NewGato(ModelForm):
    class Meta:
        model = Gato
        fields = "__all__"
        exclude = ()

class NewOtro(ModelForm):
    class Meta:
        model = Otro
        fields = "__all__"
        exclude = ()

class NewCentro(ModelForm):
    class Meta:
        model = Centro
        fields = "__all__"
        exclude = ()

class updateTrabajador(ModelForm):
    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude = ["User"]
class updateCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ["User"]

class updatePasswordForm(UserChangeForm):
    class Meta:
        model = WebUser
        fields = ['password']
        exclude = ('last_login', 'is_superuser', 'id','username', 'first_name', 'last_name',)
