from behave import *
# import sys
# import os
# currentDir = ""
# while currentDir != 'WhisBot':
#     pathSplit = os.getcwd().split("\\")
#     pathLen = len(pathSplit)
#     currentDir = pathSplit[pathLen-1]
#     os.chdir("..")
# os.chdir("WhisBot")
# sys.path.append(os.getcwd())
import os
currentDir = os.getcwd()
import fiximport
fiximport.fix('WhisBot')
from trello.stories import *
fiximport.back(currentDir)
main()

@given('the story title is {title}')
def step_impl(context, title):
    assert isinstance(title, str)

