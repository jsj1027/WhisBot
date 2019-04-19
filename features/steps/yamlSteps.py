from behave import *
from utils.openYaml import *
import operator


@given("the config is loaded")
def step_impl(context):
    x = yamlLoader("config.yaml")
    print(x.fileName)
    x.fileObj = "config.yaml"
    print(x.fileObj)

    # assert(operator.is_not(None, getYaml()))
    # assert(operator.ne(None, getYaml()))
    # print(context.config)
