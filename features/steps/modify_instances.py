from behave import *

@step('Go site and click the modify centro button')
def step_impl(context):
    from principal.models import Centro
    centro_id = Centro.objects.get(nombre = "centro_2")
    context.browser.visit(context.get_url('/centro/'+str(centro_id.pk)))
    context.browser.links.find_by_text('Editar centro').click()
        
@when('I Modify a center')
def step_impl(context):
    #fill the form
    for row in context.table:
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_value('Submit').first.click()

@step('Go site and click the modify cat button')
def step_impl(context):
    from principal.models import Animal
    animal_id = Animal.objects.get(nombre = "Michi")
    
    context.browser.visit(context.get_url('/animal/'+str(animal_id.pk)))
    context.browser.links.find_by_text('Editar animal').click()

@when('I Modify a cat')
def step_impl(context):
    from principal.models import Centro
    centro = Centro.objects.create(nombre="centro_gato", direccion="direccion")
    centro.save()
    #fill the form
    form = context.browser.find_by_tag('form').first
    for row in context.table:
        for heading in row.headings:
            #if (heading != "centro"):
                context.browser.fill(heading, row[heading])
            #else:
             #   context.browser.find_by_name('centro').select(str(centro.pk))
    form.find_by_value('Submit').first.click()

@step('Go site and click the modify dog button')
def step_impl(context):
    from principal.models import Animal
    animal_id = Animal.objects.get(nombre = "Rufus")
    
    context.browser.visit(context.get_url('/animal/'+str(animal_id.pk)))
    context.browser.links.find_by_text('Editar animal').click()

@when('I Modify a dog')
def step_impl(context):
    from principal.models import Centro
    centro = Centro.objects.create(nombre="centro_perro", direccion="direccion")
    centro.save()
    #fill the form
    form = context.browser.find_by_tag('form').first
    for row in context.table:
        for heading in row.headings:
            #if (heading != "centro"):
                context.browser.fill(heading, row[heading])
            #else:
            #    context.browser.find_by_name('centro').select(str(centro.pk))
        form.find_by_value('Submit').first.click()

@step('Go site and click the modify other button')
def step_impl(context):
    from principal.models import Animal
    animal_id = Animal.objects.get(nombre = "Sebastian")
    
    context.browser.visit(context.get_url('/animal/'+str(animal_id.pk)))
    context.browser.links.find_by_text('Editar animal').click()

@when('I Modify a other')
def step_impl(context):
    from principal.models import Centro
    centro = Centro.objects.create(nombre="centro_otro", direccion="direccion")
    centro.save()
    #fill the form
    form = context.browser.find_by_tag('form').first
    for row in context.table:  
        for heading in row.headings:
            #if (heading != "centro"):
                context.browser.fill(heading, row[heading])
            #else:
            #    context.browser.find_by_name('centro').select(str(centro.pk))
        form.find_by_value('Submit').first.click()

@step('Go site and click the modify user button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    context.browser.links.find_by_text('Usuario').click()

@when('I Modify a user')
def step_impl(context):
    #fill the form
    for row in context.table:
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_value('Submit').first.click()

@step('I\'m viewing the page details for this after modify "{animal}"')
def step_impl(context, animal):
    #assert that the animal was created correctly
    table = context.table
    assert context.browser.is_text_present('Nombre: ' + table[0][0])
    assert context.browser.is_text_present('Peso (Kg): ' + table[0][1])
    assert context.browser.is_text_present('Color: ' + table[0][2])
    assert context.browser.is_text_present('Raza: ' + table[0][3])
    assert context.browser.is_text_present('Pelaje: ' + table[0][4])
    assert context.browser.is_text_present('Centro: ' + table[0][5])

@step('I\'m viewing the page details for this after modify a user')
def step_impl(context):
    table = context.table
    context.browser.visit(context.get_url('/'))
    assert context.browser.is_text_present(table[0][0] +" "+ table[0][1])

