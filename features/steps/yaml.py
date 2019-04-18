from behave import *
from utils import openYaml
import operator

@given("the config is loaded")
def step_impl(context):
    assert(operator.is_not(None, openYaml.getYaml()))
    assert(operator.ne(None, openYaml.getYaml()))
    print(context.config)
