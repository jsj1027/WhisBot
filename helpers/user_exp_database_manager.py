from datetime import datetime
import json
from pathlib import Path

user_exp_database_filename = Path("database_files/user_exp_database.json")

user_exp_database = None

addedExp = 100

def get_user_exp_database():
    global user_exp_database
    return user_exp_database

def set_user_exp_database():
    global user_exp_database
    try:
        f = open(user_exp_database_filename, 'r+')
    except FileNotFoundError:
        f = open(user_exp_database_filename, 'w+')
    user_exp_database= json.load(f)
    return

def save_user_exp_database():
    local_user_exp_database = get_user_exp_database()
    with open(user_exp_database_filename, 'w') as outfile:
        json.dump(local_user_exp_database, outfile)
    return

def check_user_in_exp_database(user_id):
    local_user_exp_database = get_user_exp_database()
    if user_id in local_user_exp_database:
        return True
    else:
        return False

def add_new_user_to_exp_database(userID, userName):
    local_user_exp_database = get_user_exp_database()
    local_user_exp_database[userID] = {"name": userName,
                                       "id": userID,
                                       "exp": 0,
                                       "last_given_exp": ""
                                       }
    save_user_exp_database()
    return

def add_exp(userID):
    local_user_exp_database = get_user_exp_database()
    currrentExp = local_user_exp_database[userID]["exp"]
    local_user_exp_database[userID]["exp"] = currrentExp + addedExp
    local_user_exp_database[userID]["last_given_exp"] = datetime.today().strftime("%b-%d-%Y, %H:%M:%S")
    save_user_exp_database()
    return

def get_last_time_user_given_exp(userID):
    local_user_exp_database = get_user_exp_database()
    return local_user_exp_database[userID]["last_given_exp"]

def can_user_get_exp(userID):
    last_given_exp = get_last_time_user_given_exp(userID)
    last_given_exp = last_given_exp.strptime(last_given_exp, '%b-%d-%Y, %H:%M:%S')
    #if the current time is less than 2 minutes from the last exp gain you dont get exp.

def ready():
    set_user_exp_database()
    return

"""
formatted = datetime.datetime.today().strftime("%b-%d-%Y, %H:%M:%S")
date = datetime.datetime.strptime(formatted, '%b-%d-%Y, %H:%M:%S')
print(date)
"""