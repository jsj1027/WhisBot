from behave import *
from utils.openYaml import *
import operator

# TODO Some data class I gotta make maybe make it run before all hook?


def configLoad(context):
    context.data = None
    context.data.config = yamlLoader("config.yaml")
    assert(operator.ne(None, context.data.config))
