"""CP1404 Practical - Guitars prac"""

from week_06.guitar import Guitar

def main():
    guitars = []
    name = input("Name: ")
    while name.strip() != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)
        name = input("Name: ")

    print(guitars)

main()





