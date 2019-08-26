
def welcome_message(name):
    print("Welcome to the game, {}".format(name))


def main():
    player_name = input("Name: ")
    welcome_message(player_name)

main()

