"""
CP1404 - Prac Extension - Electricity Bill Estimator
Author - Sean Spring
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    """Function contains main source of code for an Electricity Bill Estimator"""
    print("Electricity bill estimator 2.0")
    menu_choice = get_menu_choice()
    while menu_choice not in 'no':
        tariff = int(input("Which tariff? 11 or 31: "))
        daily_use = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        print("Estimated bill: ${:.2f}".format(get_tariff(tariff) * daily_use * billing_days))
        menu_choice = get_menu_choice()

def get_tariff(tariff):
    ""
    if tariff == 11:
        return TARIFF_11
    else:
        return TARIFF_31

def get_menu_choice():
    exitLoop = False
    while not exitLoop:
        try:
            choice = input("Would you like to estimate your electricity bill(Y/N): ").lower()
            if choice in 'yesno':
                exitLoop = True
            else:
                print("Error: please enter Y or N")
        except ValueError:
            print("Error: please enter Y or N")
    return choice

main()
