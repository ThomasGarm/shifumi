from functions import *

score = {"player": 0,
        "computer": 0
        }

user = user_name()
while score["player"] != 3 and score["computer"] != 3:
    choosen = user_choice()
    computer = computer_choice()
    result = compare(choosen, computer, score)
    print("computer play :{}".format(computer))
    print("{} score {} / computer score {}".format(user, score["player"], score["computer"]))



