"""
CP1404 - Prac Extension - ASCII table
Author - Sean Spring
"""

MENU = """1) Character > ASCII
2) Ascii > Character
3) Print ASCII table
4) Quit
>>>
"""


def main():
    """Function contains the main bulk of the code for ASCII table program"""
    print("Welcome to the ASCII table helper")
    menu_choice = get_menu_choice()
    while menu_choice != 4:
        if menu_choice == 1:
            character = get_character()
            print("The ASCII code for {} is {}".format(character, ord(character)))
        elif menu_choice == 2:
            number = get_number()
            print("The character for {} is {}".format(number, chr(number)))
        elif menu_choice == 3:
            for x in range(33, 127):
                print("{:3} | {}".format(x, chr(x)))
        menu_choice = get_menu_choice()

def get_character():
    exit_loop = False
    char = ''
    while not exit_loop:
        char = input("Enter a character: ")
        if char.isalpha() and len(char) == 1:
            exit_loop = True
        else:
            print("Error incorrect character entered")
    return char

def get_number():
    exit_loop = False
    numb = 0
    while not exit_loop:
        try:
            numb = int(input("Enter a number between 33 and 127: "))
            if numb < 33 or numb > 127:
                print("Error, select number between 33 and 127")
            else:
                exit_loop = True
        except ValueError:
            print("ERROR, enter numerical value!")
    return numb

def get_menu_choice():
    exit_loop = False
    choice = 0
    while not exit_loop:
        try:
            choice = int(input(MENU))
            if choice < 1 or choice > 3:
                print("Error, select correct menu option")
            else:
                exit_loop = True
        except ValueError:
            print("ERROR, enter numerical value!")
    return choice

main()