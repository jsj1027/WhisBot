from behave import *
from utils.openYaml import *
import operator


@given("the config is loaded")
def step_impl(context):
    x = yamlLoader("config.yaml")
    assert(operator.ne(None, x.fileObj))


@given("the config is empty")
def step_impl(context):
    x = yamlLoader()
    assert(operator.eq(None, x.fileName))

    # assert(operator.is_not(None, getYaml()))
    # assert(operator.ne(None, getYaml()))
    # print(context.config)
