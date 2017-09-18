from random import choice


LAST_NAMES = [
    "Silva",
    "Santos",
    "Sousa",
    "Oliveira",
    "Dos Santos",
    "Dos Anos",
    "Almeida",
    "Rodrigues",
    "Gomes",
    "Costa",
    "Barbosa",
    "Ribeiro",
    "Teixeira",
    "Correia",
    "Fernandes",
    "Montes"
]


def get_last_name():
    return choice(LAST_NAMES)


def update_first_name(first_name):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    if first_name[0].upper() in vowels:
        new_name = "R" + first_name.lower()
    elif first_name[0].upper() == 'R':
        new_name = first_name
    elif first_name[1] == 'r':
        new_name = first_name[1].upper() + first_name[2:]
    else:
        new_name = "R" + first_name[1:]
    return new_name
