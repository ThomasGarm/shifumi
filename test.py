def exit_game():
    echap=input("Continue ? yes/no").lower
    while control_exit_game(echap) is False:
        print("Invalid command")
        echap=input("Continue ? yes/no").lower
    return echap

def control_exit_game(echap):
    try:
        assert echap in again
    except AssertionError as a:
        return False