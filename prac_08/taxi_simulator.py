from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"
MENU_CHOICES = "qcd"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.00
    print("lets Drive!")
    menu_input = get_menu_choice()

    while menu_input != 'q':

        if menu_input == 'c':
            print_taxis(taxis)
            current_taxi = get_taxi_choice

        menu_input = get_menu_choice()





def get_menu_choice():
    user_choice = input("{}\n>>>".format(MENU)).lower()
    while user_choice not in MENU_CHOICES:
        user_choice = input("Invalid Option\n{}\n>>>".format(MENU)).lower()
    return user_choice

def print_taxis(taxis):
    for i, taxis in enumerate(taxis):
        print("{} - {}".format(i, taxis))

main()