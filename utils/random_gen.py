import random

failures = ["engine_fire", "Nav radio", "Gps radio", "Flaps", "Lights", "Autopilot","kneeboard", "None"]


def random_seed():
    return random.randint(1, 100)


def random_word(amount):
    if amount in range(1, 5):
        return failures[0]
    elif amount in range(6, 15):
        return failures[1]
    elif amount in range(16, 25):
        return failures[2]
    elif amount in range(26, 35):
        return failures[3]
    elif amount in range(36, 45):
        return failures[4]
    elif amount in range(46, 55):
        return failures[5]
    elif amount in range(56, 65):
        return failures[6]
    elif amount in range(66, 100):
        return failures[7]


x = random_seed()
word = random_word(x)
print(word)

