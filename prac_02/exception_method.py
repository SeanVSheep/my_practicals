"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    when someone tries to enter a value different to an interger
2. When will a ZeroDivisionError occur?
    when someone tries to enter the denominator as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    yes enter a loop on the denominator so it checks if value is == 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator that isn't 0: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")