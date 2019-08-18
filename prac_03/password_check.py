"""
Sean
"""
MIN_LENGTH = 5
def main():
    #main body of code initialises functions to get password str and print password str length in artrics
    password = get_password()
    print_astrics(password)


def print_astrics(password):
    #receives password str and prints the same amount of characters with astrics
    print(len(password) * "*")


def get_password():
    #user enters password and checks if the str is correct length
    password = input("Enter new password: ")
    while len(password) < MIN_LENGTH:
        password = input("Enter new password, minimum {} characters: ".format(MIN_LENGTH))
    return password


main()