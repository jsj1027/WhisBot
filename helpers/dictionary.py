import json
from pathlib import Path

# values are [[bad words used list], total points, banned_x_times]

database_folder = Path("database_files/")
black_list_filename = database_folder / "black_list.json"
white_list_filename = database_folder / "white_list.json"
users_filename = database_folder / "users.json"

if black_list_filename.exists():
    with open(black_list_filename, "r+") as f:
        black_list = json.load(f)
else:
    black_list = open(black_list_filename, "r+")
if white_list_filename.exists():
    with open(white_list_filename, "r+") as f:
        white_list = json.load(f)
else:
    white_list = open(white_list_filename, "r+")
if users_filename.exists():
    with open(users_filename, "r+") as f:
        users = json.load(f)
else:
    users = open(users_filename, "r+")


def check_user_database(user):
    if user in users:
        return users[user]
    else:
        return False


def change_user_database_info(user_id_number, user_info):
    users[user_id_number] = user_info
    return


def add_user_to_user_database(user_id_number, bad_words_used, points_to_add):
    users[user_id_number] = [[bad_words_used], points_to_add, 0]


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
    #   return message_set.intersection(black_list)
    return message_set.keys() & black_list.keys()


def check_white_list_intersection(message_set):
    #   return message_set.intersection(white_list)
    #   At this point message_set is a set
    return message_set & white_list.keys()
