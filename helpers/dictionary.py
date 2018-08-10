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
users = json.load(f)

def get_black_list():
    global black_list
    return black_list


def get_white_list():
    global white_list
    return white_list


def get_users():
    global users
    return users


def check_user_database(user):
    if user in users:
        return users[user]
    else:
        return False


def change_user_database_info(user_id_number, user_info):
    users[user_id_number] = user_info
    return


def add_user_to_user_database(user_id_number, bad_words_used, points_to_add):
    if check_user_database(user_id_number) == False:
        users[user_id_number] = [[bad_words_used], points_to_add, 0]
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
