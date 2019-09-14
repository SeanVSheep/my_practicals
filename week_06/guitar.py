"""CP1404 Practical - Guitar class"""

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "My guitar: {}, first made in {}".format(self.name, self.year)



