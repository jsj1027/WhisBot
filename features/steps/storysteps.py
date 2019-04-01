from behave import *
def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
load_src("stories", "../../trello/stories.py")
from stories import *

@given('the story title is {title}')
def step_impl(context, title):
    assert isinstance(title, str)

