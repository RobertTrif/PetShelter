from behave import *

use_step_matcher("parse")

@given('Exists a worker "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
        

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/myrestaurants/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()