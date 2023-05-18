from behave import *

@step('Go site and click the modify button')
def step_impl(context):
    context.browser.visit(context.get_url('/centro/1'))
    context.browser.links.find_by_text('Editar centro').click()
        
@when('I Modify a center')
def step_impl(context):
    #fill the form
    for row in context.table:
        context.browser.visit(context.get_url('/centro_edit/1'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_value('Submit').first.click()
