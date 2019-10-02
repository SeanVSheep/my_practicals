"""
CP1404 - Prac Extension - Menu driven number sequence generator
Author - Sean Spring
"""

MENU = """1) Show the even numbers from {0} to {1}
2) Show the odd numbers from {0} to {1}
3) Show the squares from {0} to {1}
4) Exit the program
>>>"""


def main():
    """Function contains the main code for a Menu driven number sequence generator"""
    first_number = get_number("first")
    second_number = get_number("second")
    ascending_descending = get_direction(first_number, second_number)
    menu_choice = get_menu_choice(first_number, second_number)
    while menu_choice != 4:
        if menu_choice == 1:
            print("Even numbers from {} to {}:".format(first_number, second_number))
            for x in range(first_number, second_number, ascending_descending):
                if x % 2 == 0:
                    print(x)
        elif menu_choice == 2:
            print("Odd numbers from {} to {}:".format(first_number, second_number))
            for x in range(first_number, second_number, ascending_descending):
                if x % 2 == 1:
                    print(x)
        elif menu_choice == 3:
            print("Squared numbers from {} to {}:".format(first_number, second_number))
            for x in range(first_number, second_number, ascending_descending):
                print("{} squared: {}".format(x, x*x))
        else:
            print("PICK A CORRECT MENU OPTION!!!")

        menu_choice = get_menu_choice(first_number, second_number)

def get_direction(first, second):
    if first < second:
        return 1
    else:
        return -1

def get_menu_choice(first, second):
    return int(input(MENU.format(first, second)))

def get_number(order):
    exitLoop = False
    while not exitLoop:
        try:
            number = int(input("Enter " + order + " number: "))
            exitLoop = True
        except ValueError:
            print("ERROR enter numerical value!")
    return number
main()