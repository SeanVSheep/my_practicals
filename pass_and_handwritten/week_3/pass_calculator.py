MENU_UI = """The NON-Crappiest Calculator can...
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Exit
"""

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def get_valid_number(message):
    valid_input = 0
    while valid_input == 0:
        try:
            number = int(input(message))
            valid_input = 1
        except ValueError:
            print("That's not a number! Try again.")

    return number

def print_menu_options():
    print(MENU_UI)

def get_valid_selection(low_number, high_number):
    valid_selection = 0
    while valid_selection == 0:
        try:
            selected_option = int(input("What would you like to do? "))
            while selected_option > high_number or selected_option < low_number:
                selected_option = int(input("Invalid choice! What would you like to do? "))
            valid_selection = 1
        except ValueError:
            print("That's not a number! Try again.")

    return selected_option


def main():
    print("Welcome to the Clean Calculator!")
    loop_controller = 0
    while loop_controller == 0:
        print_menu_options()
        selected_option = get_valid_selection(1, 5)

        if selected_option == 5:
            print("Goodbye!")
            loop_controller = 1
            break
        else:
            number_1 = get_valid_number("Enter the first number: ")
            number_2 = get_valid_number("Enter the second number: ")

        if (selected_option == 1):
            result = add(number_1, number_2)
        elif (selected_option == 2):
            result = subtract(number_1, number_2)
        elif (selected_option == 3):
            result = multiply(number_1, number_2)
        else:
            result = divide(number_1, number_2)

        print("The result is " + str(result))

main()