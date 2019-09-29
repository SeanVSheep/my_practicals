from prac_08.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print("You drive 40km\n{}\nfare is ${:.2f}\n".format(my_taxi, my_taxi.get_fare()))
my_taxi.start_fare()
my_taxi.drive(100)
print("You try to drive 100km\n{}\nfare is ${:.2f}\n".format(my_taxi, my_taxi.get_fare()))