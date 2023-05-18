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


@when('I register a center')
def step_impl(context):
    #fill the form
    for row in context.table:
        context.browser.visit(context.get_url('/administracion/crear_centro/'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_value('Crear').first.click()
    #assert that the center was created correctly

@step('I\'m viewing the details of this center')
def step_impl(context):
    context.browser.visit(context.get_url('/centros/'))
    table = context.table
    context.browser.links.find_by_text(table[0][0]).click()
    assert context.browser.is_text_present('Nombre: ' + table[0][0])
    assert context.browser.is_text_present('Direccion: ' + table[0][1])

@when('I register a "{animal}"')
def step_impl(context, animal):
    #create a centro for this animal
    from principal.models import Centro
    centro = Centro.objects.create(nombre=context.table[0][5], direccion="direccion")
    centro.save()
    #fill the form
    for row in context.table:
        uri = "/administracion/crear_" + animal + "/"
        context.browser.visit(context.get_url(uri))
        if not context.browser.is_text_present("Para acceder a esta seccion necesitas iniciar sesion con tu cuenta de trabajdor del centro"):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                if (heading != "centro"):
                    context.browser.fill(heading, row[heading])
                else:
                    context.browser.find_by_name('centro').select(str(centro.pk))

            form.find_by_value('Crear').first.click()



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

@then('I\'m viewing a message "{message}"')
def step_impl(context, message):
    #assert that the animal was created correctly
    assert context.browser.is_text_present(message)

@step('I\'m viewing the page details for this "{animal}"')
def step_impl(context, animal):
    #assert that the animal was created correctly
    uri = "/animales/" + animal
    context.browser.visit(context.get_url(uri))
    table = context.table
    context.browser.links.find_by_text(table[0][0]).click()
    assert context.browser.is_text_present('Nombre: ' + table[0][0])
    assert context.browser.is_text_present('Peso (Kg): ' + table[0][1])
    assert context.browser.is_text_present('Color: ' + table[0][2])
    assert context.browser.is_text_present('Raza: ' + table[0][3])
    assert context.browser.is_text_present('Pelaje: ' + table[0][4])
    assert context.browser.is_text_present('Centro: ' + table[0][5])