black_list = {}
white_list = {}

#You need a set of all the words
def check_contents(message):
    message_set = {}
    for word in message.content:
        message_set.add(word)
    message_set = message_set.intersection(black_list)
    message_white = message_set.intersection(white_list)
    for word in message_white:
        message_set.remove(word)
    return message_set

#You need a dictionary of all the words
def point_assignement(message_set):
    point_total = 0
    for word in message_set:
      point_total += word_dictionary[word]
    return point_total

#create another dictionary of users, keys are users id number,
#values are [[bad words used list], total points, banned_x_times]
def add_points(user_id_number, points_to_add, bad_words_used)#set
    total_points = 0
    if user_dict[user_id_number]:
        user_info = user_dict[user_id_number]
        user_info[1] += points_to_add
        user_info[0] = user_info[0].union(bad_words_used)
        user_dict[user_id_number] = user_info
        total_points = user_info[1]
    else:
        user_dict[user_id_number] = [[bad_words_used], points_to_add]
        total_points = points_to_add
    return points_to_add

def user_ban_reset(user_id_number):
    user_info = user_dict[user_id_number]
    user_info[1] = 0
    user_info[2] += 1
    return

#create some text file and load it with the users name saing heyyyy this nigga banned.
