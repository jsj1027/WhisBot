black_list = {
    "arian": 0.5,

    "aryan": 0.5,

    "beaner": 0.5,

    "cumslut": 0.5,

    "coon": 0.5,

    "dike": 0.5,

    "dyke": 0.5,

    "dykes": 0.5,

    "fag": 0.5,

    "fagg": 0.5,

    "fagged": 0.5,

    "faggit": 0.5,

    "faggot": 0.5,

    "fagot": 0.5,

    "fags": 0.5,

    "faig": 0.5,

    "faigt": 0.5,

    "fannybandit": 0.5,

    "fudgepacker": 0.5,

    "gay": 0.5,

    "gays": 0.5,

    "gringo": 0.5,

    "hitler": 0.5,

    "hiv": 0.5,

    "inbred": 0.5,

    "incest": 0.5,

    "injun": 0.5,

    "jap": 0.5,

    "japs": 0.5,

    "kike": 0.5,

    "kikes": 0.5,

    "kkk": 0.5,

    "klan": 0.5,

    "kyke": 0.5,

    "lesbo": 0.5,

    "lesbos": 0.5,

    "lez": 0.5,

    "lezzie": 0.5,

    "lezzies": 0.5,

    "lezzy": 0.5,

    "muff diver": 0.5,

    "muffdiver": 0.5,

    "negro": 0.5,

    "nigger": 0.5,

    "niggers": 0.5,

    "pollock": 0.5,

    "queer": 0.5,

    "rape": 0.5,

    "raped": 0.5,

    "reetard": 0.5,

    "reich": 0.5,

    "retard": 0.5,

    "retarded": 0.5,

    "rtard": 0.5,

    "r-tard": 0.5,

    "schizo": 0.5,

    "slave": 0.5,

    "slut": 0.5,

    "sluts": 0.5,

    "spic": 0.5,

    "spick": 0.5,

    "spik": 0.5,

    "spiks": 0.5,

    "spooge": 0.5,

    "wetback": 0.5,

    "wigger": 0.5,
}

white_list = {
    "sure": 0
}

def check_black_list_word(word):
    if word in black_list:
        return black_list[word]
    else:
        return False

def check_white_list_word(word):
    if word in white_list:
        return white_list[word]
    else:
        return False

def check_black_list_intersection(message_set):
    return message_set.intersection(black_list)


def check_white_list_intersection(message_set):
    return message_set.intersection(white_list)
