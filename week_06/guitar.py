"""CP1404 Practical - Guitar class"""

class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return (2019 - self.year)

    def is_vintage(self):
        return self.get_age() >= 50

def main():
    """ test code for guitar class"""

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson)

    print(gibson.get_age())
    print(gibson.is_vintage())

main()
