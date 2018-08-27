import json
from pathlib import Path

# values are [[bad words used list], total points, banned_x_times]

database_folder = Path("C:/Users/Kaloshade/Desktop/Folders/WhisBot/database_files")
black_list_filename = database_folder / "test_black.json"
white_list_filename = database_folder / "test_white.json"
user_database_filename = database_folder / "test_user.json"

black_list = None
white_list = None
user_database = None
# TODO We can probably make the dictionary holding everything a class, tbh we can prob make this whole thing /
# / involved in way more OOP


def set_black_list():
    global black_list
    try:
        f = open(black_list_filename, 'r+')
    except FileNotFoundError:
        f = open(black_list_filename, 'w+')
    black_list = json.load(f)
    return


def set_white_list():
    global white_list
    try:
        f = open(white_list_filename, 'r+')
    except FileNotFoundError:
        f = open(white_list_filename, 'w+')
    white_list = json.load(f)
    return


def set_users():
    global user_database
    try:
        f = open(user_database_filename, 'r+')
    except FileNotFoundError:
        f = open(user_database_filename, 'w+')
    user_database = json.load(f)
    return


def save_black_list():
    local_black_list = get_black_list()
    with open(black_list_filename, 'w') as outfile:
        json.dump(local_black_list, outfile)
    return


def save_white_list():
    local_white_list = get_white_list()
    with open(white_list_filename, 'w') as outfile:
        json.dump(local_white_list, outfile)
    return

def save_user_database():
    local_user_database = get_users()
    with open(user_database_filename, 'w') as outfile:
        json.dump(local_user_database, outfile)
    return

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
#//TODO DELTET THIS FUNCITON ADD ALL USES
def change_user_database_info(user_id_number, new_user_info):
    user_database = get_users()
    if check_if_user_in_database(user_id_number):
        user_database[user_id_number] = new_user_info
        save_user_database()
    else:
        raise ValueError("This user isn't in the database, you can't change their info")

def add_points_to_user(user_id_number, points_to_add):
    local_user_database = get_users()
    try:
        user_info = grab_user_from_database(user_id_number)
        user_info[1] += points_to_add
        local_user_database[user_id_number] = user_info
        save_user_database()
    except Exception as e:
        print(e)
        # TODO make this exception more detailed
    return

def add_words_to_user(user_id_number, words_to_add):
    local_user_database = get_users()
    try:
        user_info = grab_user_from_database(user_id_number)
        user_info[0] += words_to_add
        local_user_database[user_id_number] = user_info
        save_user_database()
    except Exception as e:
        print(e)
        # TODO make this exception more detailed
    return

def increase_ban_counter(user_id_number):
    local_user_database = get_users()
    try:
        user_info = grab_user_from_database(user_id_number)
        user_info[2] += 1
        local_user_database[user_id_number] = user_info
        save_user_database()
    except Exception as e:
        print(e)
        # TODO make this exception more detailed
    return

def ban_counter_reset(user_id_number):
    local_user_database = get_users()
    try:
        user_info = grab_user_from_database(user_id_number)
        user_info[2] = 0
        local_user_database[user_id_number] = user_info
        save_user_database()
    except Exception as e:
        print(e)
        # TODO make this exception more detailed
    return

def add_user_to_user_database(user_id_number, bad_words_used, points_to_add):
    if not check_if_user_in_database(user_id_number):
        user_database[user_id_number] = [[bad_words_used], float(points_to_add), 0]
        save_user_database()
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


def main():
    set_black_list()
    set_white_list()
    set_users()

main()