from behave import *
https://stackoverflow.com/questions/40022220/attempted-relative-import-beyond-toplevel-package/40022629
#sick of this crap fix it with this 

@given("we have behave installed")
def step_impl(context):
    pass

@when("we implement a test")
def step_impl(context):
    assert True is not False

@then("behave will test it for us!")
def step_impl(context):
    assert context.failed is False
