from behave import *
# from features.support.yamlSupport import *
from utils.openYaml import *
import operator


@given("the config is loaded")
def step_impl(context):
    yamlConfigFile = yamlLoader("config.yaml")
    assert(operator.ne(None, yamlConfigFile.fileObj))
    # configLoad(context)


@step('the config is empty')
def step_impl(context):
    yamlConfigFile = yamlLoader()
    assert(operator.eq(None, yamlConfigFile.fileName))

    # assert(operator.is_not(None, getYaml()))
    # assert(operator.ne(None, getYaml()))
    # print(context.config)
