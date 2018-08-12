import json
from pathlib import Path

# values are [[bad words used list], total points, banned_x_times]

database_folder = Path("database_files")
black_list_filename = database_folder / "black_list.json"
white_list_filename = database_folder / "white_list.json"
users_filename = database_folder / "users.json"

# we have to initialize the database folders if its the first time and open then everytimee.
f = open(black_list_filename, 'r+')
black_list = json.load(f)
f = open(white_list_filename, 'r+')
white_list = json.load(f)
f = open(users_filename, 'r+')
user_database = json.load(f)
# TODO We can probably make the dictionary holding everything a class, tbh we can prob make this whole thing /
# / involved in way more OOP

"""
def set_black_list():
    # TODO Move code to initialize it here
    return 


def set_white_list():
    # TODO Move code to initialize it here
    return


def set_users():
    # TODO Move code to initialize it here
    return
"""

def get_black_list():
    global black_list
    return black_list


def get_white_list():
    global white_list
    return white_list


def get_users():
    global user_database
    return user_database


def check_if_user_in_database(user_id):
    user_database = get_users()
    if user_id in user_database:
        return True
    else:
        return False


def grab_user_from_database(user_id):
    user_database = get_users()
    if check_if_user_in_database(user_id):
        return user_database[user_id]
    else:
        raise ValueError("This user isn't in the database, you can't grab it/")


def change_user_database_info(user_id_number, new_user_info):
    user_database = get_users()
    if check_if_user_in_database(user_id_number):
        user_database[user_id_number] = new_user_info
    else:
        raise ValueError("This user isn't in the database, you can't change their info")


def add_user_to_user_database(user_id_number, bad_words_used, points_to_add):
    if not check_if_user_in_database(user_id_number):
        user_database[user_id_number] = [[bad_words_used], points_to_add, 0]
    else:
        raise ValueError("This value is already in the database")


def check_black_list_database(word):
    if word in black_list:
        return black_list[word]
    else:
        return False


def check_white_list_database(word):
    if word in white_list:
        return white_list[word]
    else:
        return False


def check_black_list_intersection(message_set):
    return message_set.keys() & black_list.keys()


def check_white_list_intersection(message_set):
    #   return message_set.intersection(white_list)
    #   At this point message_set is a set
    return message_set & white_list.keys()
