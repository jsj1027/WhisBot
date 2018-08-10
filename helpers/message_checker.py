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


def add_points(user_id_number, points_to_add, bad_words_used):
    total = 0
    if check_if_user_in_database(user_id_number):
        user_info = check_if_user_in_database(user_id_number)
        user_info[1] += points_to_add
        user_info[0] += bad_words_used
        total = float(user_info[1])
        change_user_database_info(user_id_number, user_info)
    else:
        add_user_to_user_database(user_id_number, bad_words_used, points_to_add)
    return total


def user_ban_reset(user_id_number):

    user_info = check_if_user_in_database(user_id_number)
    user_info[1] = 0
    user_info[2] += 1
    change_user_database_info(user_id_number, user_info)
    return

# create some text file and load it with the users name saing heyyyy this nigga banned.
