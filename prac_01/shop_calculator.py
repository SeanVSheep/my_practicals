def main():
    total = 0
    validInput = False
    while not validInput:
        try:
            itemNumber = int(input("Number of items: "))
            while itemNumber < 0:
                itemNumber = int(input("Invalid number of items, renter amount: "))
            validInput = True
        except:
            print("Error! must enter a numerical value")

    for i in range(itemNumber):
        price = float(input("Price of item: "))
        total = total + price

    if total > 100:
        total = total * 0.9

    print("total price for " + str(itemNumber) + " items is $" + str("%.2f" % total))

main()