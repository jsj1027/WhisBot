from behave import *
from trello.stories import *

# import importlib.util
# spec = importlib.util.spec_from_file_location("stories.py", "C:/Users/johnsoj1/Desktop/My Projects/WhisBot/trello/stories.py")
# stories =  importlib.util.module_from_spec(spec)
# spec.loader.exec_module(stories)


@given("we have behave installed")
def step_impl(context):
    pass

@given("the cardDataBase is set")
def step_impl(context):
    getCardDataBase()
    assert (cardDataBase is None)

@given("the story title is {title}")
def step_impl(context,title):
    pass

@when("we implement a test")
def step_impl(context):
    assert True is not False

@then("behave will test it for us!")
def step_impl(context):
    assert True is not False
