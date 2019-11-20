from random import randint

choice=["pierre", "feuille", "ciseaux"]


def user_name():
    user=input("choose your name")
    while control_user_name(user) is False:
        print("minimum 2 caractères et maxi 6")
        user=input("choose your name")
    return user


def control_user_name(user):
    try:
        assert len(user) >1 and len(user) < 6
    except AssertionError as a:
        return False

def user_choice():
    print("choose between pierre, feuille and ciseaux")
    user_entry=input("your choice").lower()
    while control_user_choice(user_entry) is False:
        print("choose between pierre, feuille and ciseaux")
        user_entry=input("your choice").lower()
    return user_entry


def control_user_choice(user_entry):
    try:
        assert user_entry in choice
    except AssertionError as a:
        return False


def computer_choice():
    return choice[randint(0, len(choice)-1)]

def compare(choosen, computer, score):
    if choosen != computer:
        if choosen== "pierre" and computer== "ciseaux"\
        or choosen== "feuille" and computer== "pierre"\
        or choosen== "ciseaux" and computer== "feuille":
            score["player"] += 1
        else:
            score["computer"] += 1
    return score

