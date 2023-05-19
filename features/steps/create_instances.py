from behave import *

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
        if context.browser.url == context.get_url(uri):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                if (heading != "centro"):
                    context.browser.fill(heading, row[heading])
                else:
                    context.browser.find_by_name('centro').select(str(centro.pk))

            form.find_by_value('Crear').first.click()

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

@then('There are {count:n} cats')
def step_impl(context, count):
    from principal.models import Gato
    assert count == Gato.objects.count()

@then('There are {count:n} dogs')
def step_impl(context, count):
    from principal.models import Perro
    assert count == Perro.objects.count()

@then('There are {count:n} others')
def step_impl(context, count):
    from principal.models import Otro
    assert count == Otro.objects.count()