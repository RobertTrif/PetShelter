from audioop import reverse
from behave import *
from selenium.webdriver.support.ui import Select
use_step_matcher("parse")
import time


@given('Exists a worker "{username}" with password "{password}"')
def step_impl(context, username, password):
    from principal.models import Trabajador, WebUser, Centro
    centro = Centro.objects.create(nombre="centro", direccion="direccion")
    centro.save()
    user = WebUser.objects.create_user(is_trabajador = True, password=password, username=username)
    user.save()
    trabajador = Trabajador.objects.create(User=user, nombre="Pepe", apellidos="Marin", telefono=698524587, email="email@email.email",anos=93, departamento="departamento", 
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


from splinter import Browser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


@when('I click on the "Administracion" button')
def step_when_click_administracion_button(context):
    administracion_link = context.browser.find_by_xpath('//a[text()="Administracion"]').first
    administracion_link.click()


@then('I should be redirected to the "Administracion" page')
def step_then_redirected_to_administracion_page(context):
    wait = WebDriverWait(context.browser.driver, 10)
    try:
        wait.until(EC.url_contains('/administracion/'))
        assert '/administracion/' in context.browser.url
    except NoSuchElementException:
        assert False, "Not redirected to the 'Administracion' page"


@when('I select "{animal}" from "Eliminar animal"')
def step_when_select_animal_from_eliminar(context, animal):
    eliminar_form = context.browser.find_by_name("eliminar_animal").first
    select = eliminar_form.find_by_name("menu").first
    select.select(animal)
    eliminar_button = eliminar_form.find_by_css("input[type='button'][value='Eliminar']").first
    eliminar_button.click()


@then('I should delete de animal "{animal_name}"')
def step_then_delete_animal(context, animal_name):
      
    # Delete the specified animal
    animal_li = context.browser.find_by_xpath(f"//a[text()='{animal_name}']/ancestor::li")
    eliminar_button = animal_li.find_by_xpath(".//button[text()='Eliminar']").first
    eliminar_button.click()

@then('I wait for {seconds} seconds')
def step_then_wait(context, seconds):
    time.sleep(int(seconds))