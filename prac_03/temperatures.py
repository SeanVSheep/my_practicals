MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    #controls the temperature converation program
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = method_name(celsius)
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Result: {:.2f} F".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def method_name(celsius):
    #users input for fahrenheit is passed in and returns celsius conversation
    return celsius * 9.0 / 5 + 32

main()