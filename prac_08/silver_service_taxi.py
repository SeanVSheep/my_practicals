from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Car.taxi that includes fare costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + self.flagfall

