from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"
MENU_CHOICES = "qcd"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.00
    print("lets Drive!")
    menu_input = get_menu_choice()

    while menu_input != 'q':

        if menu_input == 'c':
            print_taxis(taxis)
            current_taxi = taxis[get_taxi_choice(len(taxis))]
            print(current_taxi)
        elif menu_input == 'd':
            if current_taxi is None:
                print("Select your vehicle!")
            else:
                current_taxi.start_fare()
                distance = get_distance()
                current_taxi.drive(distance)
                current_bill = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_bill))
                total_bill += current_bill

        print("Bill to date: ${:.2f}".format(total_bill))
        menu_input = get_menu_choice()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    print_taxis(taxis)


def get_menu_choice():
    user_choice = input("{}\n>>>".format(MENU)).lower()
    while user_choice not in MENU_CHOICES:
        user_choice = input("Invalid Option\n{}\n>>>".format(MENU)).lower()
    return user_choice

def print_taxis(taxis):
    for i, taxis in enumerate(taxis):
        print("{} - {}".format(i, taxis))

def get_taxi_choice(total_taxis):
    exit_loop = False
    while not exit_loop:
        try:
            users_choice = int(input("Choose Taxi: "))
            if users_choice >= 0 and users_choice <= (total_taxis - 1):
                exit_loop = True
            else:
                print("Taxi not listed")
        except ValueError:
            print("Error, Enter a number")
    return users_choice

def get_distance():
    exit_loop = False
    while not exit_loop:
        try:
            users_choice = int(input("Drive how far? "))
            if users_choice >= 1:
                exit_loop = True
            else:
                print("Please drive somewhere!")
        except ValueError:
            print("Error, Enter a number")
    return users_choice





main()