"""
Create a function that turns " " into "%20"
"""

def string_replacement(message):
    strMessage = str(message).replace(" ", "%20")
    print(strMessage)


string_replacement(input())