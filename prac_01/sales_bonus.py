def main():
    sales = float(input("Enter sales: $"))

    while sales < 0:
        sales = float(input("ERROR! please enter sales bonus"))

    if sales < 1000:
        bonus = sales * 0.1
    elif sales > 1000:
        bonus = sales * 0.15

    print("Sales + bonus: " + str("%.2f" % (bonus + sales)))

main()

def loop():
sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales < 1000:
        bonus = sales * 0.1
    elif sales > 1000:
        bonus = sales * 0.15

    print("Sales + bonus: " + str("%.2f" % (bonus + sales)))

loop()