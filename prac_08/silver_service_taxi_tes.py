from prac_08.silver_service_taxi import SilverServiceTaxi


hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)

silver_taxi = SilverServiceTaxi("Silver Taxi", 30, 2)
silver_taxi.drive(18)
print("You drive 18km\n{}\nFare for {} is ${:.2f}\n".format(silver_taxi, silver_taxi.name, silver_taxi.get_fare()))
