MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    #controls the temperature conversion program
    choice = menu()

    while choice != "Q":

        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print("Result: {:.2f} F".format(celsius))

        else:
            print("Invalid option")

        choice = menu()
    print("Thank you.")


def menu():
    #prints menu options and returns users choice
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def convert_fahrenheit_to_celsius(fahrenheit):
    #users input of fahrenheit is passed in and returns celsius conversion
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit(celsius):
    #users input of celcius is passed in and returns fahrenheit conversion
    return celsius * 9.0 / 5 + 32

main()