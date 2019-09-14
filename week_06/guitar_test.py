"""CP1404 Practical - Guitar Test prac"""


def main():
    """ test code for guitar class"""

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson)

    print(gibson.get_age())
    print(gibson.is_vintage())

main()