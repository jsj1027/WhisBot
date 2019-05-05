from utils.dictionary import *


def check_contents(message):
    message_set = {}
    message.content = message.content.split()
    for word in message.content:
        word = word.lower()
        message_set[word] = word
    message_set = check_black_list_intersection(message_set)
    if message_set == {}:
        return []
    message_white = check_white_list_intersection(message_set)
    if message_white != {}:
        for word in message_white:
            message_set.remove(word)
    return list(message_set)


def point_assignment(message_set):
    point_total = 0
    for word in message_set:
        point_total += check_black_list_database(word)
    return point_total


# //TODO HOLY CRAP WHY DOES THIS RETURN A NUMBER MAKE THIS NEVER RETURN A NUMBER THIS IS GARBAGE CODE
def calculate_user_points(user_id_number, points_to_add, bad_words_used):
    if check_if_user_in_database(user_id_number):
        add_points_to_user(user_id_number, points_to_add)
        add_words_to_user(user_id_number, bad_words_used)
    else:
        add_user_to_user_database(
            user_id_number, bad_words_used, points_to_add)


def user_ban_reset(user_id_number):
    try:
        ban_counter_reset(user_id_number)
    except Exception as e:
        print(e)
    return
