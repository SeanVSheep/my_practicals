"""CP1404 Practical - Guitars prac"""

from prac_06.guitar import Guitar

def main():
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name.strip() != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)
        name = input("Name: ")


    for idx, guitar in enumerate(guitars, 1):
        #print("Guitar {}: {}".format(idx, guitar))
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(idx, guitar.name, guitar.year, guitar.cost, "(vintage)" if guitar.is_vintage() else ""))
        #print("{guitar}".format(guitar=guitar))




main()





