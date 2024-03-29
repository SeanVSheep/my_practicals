"""CP1404 Practical - Programming Language class"""


class ProgrammingLanguage:
    """Programming Language Class"""

    def __init__(self, name, typing, reflection, year):
        """"Programming Language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing.lower() =='dynamic'





