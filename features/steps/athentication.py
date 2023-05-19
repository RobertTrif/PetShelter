from behave import *

use_step_matcher("parse")

@given('Exists a worker "{username}" with password "{password}"')
def step_impl(context, username, password):
    from principal.models import Trabajador, WebUser, Centro
    centro = Centro.objects.create(nombre="centro", direccion="direccion")
    centro.save()
    user = WebUser.objects.create_user(is_trabajador = True, password=password, username=username)
    user.save()
    trabajador = Trabajador.objects.create(User=user, nombre="Pepe",apellidos="Marin",telefono=698524587,email="email@email.email",anos=93, departamento="departamento", 
                                           adresa="adresa", centro=centro)
    trabajador.save()

@given('I login as worker "{username}" with password "{password}"')
def step_impl(context, username, password):
    from principal.models import WebUser, Trabajador
    user = WebUser.objects.get(username=username)
    trab = Trabajador.objects.get(User = user)
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    assert context.browser.is_text_present('Conectado como ' + trab.nombre + ' ' +trab.apellidos)

@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('/logout/'))
    assert context.browser.is_text_present('login')