from behave import *
from utils.openYaml2 import *
import operator


@given("the config is loaded")
def step_impl(context):
    x = yamlLoader()
    x.fileObj = "config.yaml"
    assert(operator.ne(None, x.fileObj))


@given("the config is empty")
def step_impl(context):
    x = yamlLoader()
    assert(operator.eq(None, x.fileObj))

    # assert(operator.is_not(None, getYaml()))
    # assert(operator.ne(None, getYaml()))
    # print(context.config)
