from behave import *
from trello.stories.py import *

@given("the story title is '{title}' ")
def step_impl(context, title):
    

@given("we have behave installed")
def step_impl(context):
    pass

@when("we implement a test")
def step_impl(context):
    assert True is not False

@then("behave will test it for us!")
def step_impl(context):
    assert context.failed is False
