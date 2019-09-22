"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""

    '''
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    '''

    # MOD 1)
    limo = Car("limo", 100)
    print("Your {} has {}km worth of fuel".format(limo.name, limo.fuel))
    # MOD 2)
    limo.add_fuel(20)
    print("You fill up with 20km of fuel, Your {} has {}km worth of fuel".format(limo.name, limo.fuel))
    # MOD 3)
    print("limo fuel =", limo.fuel)
    # MOD 4)
    limo.drive(115)
    print("Your {} drives {}km".format(limo.name, limo.odometer))
    # MOD 5)
    print("limo odometer =", limo.odometer)
    # MOD 6)
    print(limo)


main()