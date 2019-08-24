
"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""
'''
out put should look like:
How many months? 5

Enter income for month 1: 120
Enter income for month 2: 245.4
Enter income for month 3: 900
Enter income for month 4: 1205.56
Enter income for month 5: 12.35

Income Report
-------------
Month  1 - Income: $    120.00         Total: $    120.00
Month  2 - Income: $    245.40         Total: $    365.40
Month  3 - Income: $    900.00         Total: $   1265.40
Month  4 - Income: $   1205.56         Total: $   2470.96
Month  5 - Income: $     12.35         Total: $   2483.31
'''

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    exitLoop = False
    while not exitLoop:
        try:
            numer_of_months = int(input("How many months? "))
            exitLoop = True
        except ValueError:
            print("ERROR! Please enter numerical value")

    exitLoop = False
    for numer_of_months in range(1, numer_of_months + 1):
        income = float(input("Enter income for months {} : ".format(numer_of_months)))
        incomes.append(income)

    print_report(incomes, numer_of_months)


def print_report(incomes, numer_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for numer_of_months in range(1, numer_of_months + 1):
        income = incomes[numer_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(numer_of_months, income, total))


main()






