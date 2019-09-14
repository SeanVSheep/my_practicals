"""CP1404 Practical - Guitar class"""

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return "The {} is 2019 - {} = {}".format(self.name, self.year, str(2019 - self.year))


