from helpers.dictionary import *


def check_contents(message):
    message_set = {}
    message.content = message.content.split()
    for word in message.content:
        message_set[word] = word
    message_set = check_black_list_intersection(message_set)
    if not message_set:
        return set()
    message_white = check_white_list_intersection(message_set)
    if not message_white:
        for word in message_white:
            message_set.remove(word)
    return message_set


def point_assignment(message_set):
    point_total = 0
    for word in message_set:
        point_total += check_black_list_database(word)
    return point_total


#//TODO HOLY CRAP WHY DOES THIS RETURN A NUMBER MAKE THIS NEVER RETURN A NUMBER THIS IS GARBAGE CODE
def add_points(user_id_number, points_to_add, bad_words_used):
    user_point_total = 0
    try:
        add_points_to_user(user_id_number, points_to_add)
        add_words_to_user(user_id_number, bad_words_used)
        user = grab_user_from_database(user_id_number)
        user_point_total = user[1]
    except ValueError:
        add_user_to_user_database(user_id_number, bad_words_used, points_to_add)
    return user_point_total


def user_ban_reset(user_id_number):
    try:
        ban_counter_reset(user_id_number)
    except Exception as e:
        print(e)
    return


