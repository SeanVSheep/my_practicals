"""CP1404 Practical - Guitar Test prac"""

from week_06.guitar import Guitar

def main():
    """ test code for guitar class"""

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 123.12)

    print(gibson.get_age())
    print(another_guitar.get_age())
    print(gibson.is_vintage())
    print(another_guitar.is_vintage())

main()