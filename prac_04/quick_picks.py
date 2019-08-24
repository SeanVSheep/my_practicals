"""
How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
"""

import random
NUMBERS_ON_A_LINE = 6

MIN_RANGE = 1
MAX_RANGE = 45

def main():
    exitLoop = False
    while not exitLoop:
        try:
            picks = int(input("How many quick picks? "))
            while picks <= 0:
                picks = int(input("Picks must be greater then 0: "))
            exitLoop = True
        except ValueError:
            print("ERROR! Please enter numerical value")

    for i in range(picks):
        generated_numbers = []
        exitLoop = False
        while not exitLoop:
            new_number = random.randint(MIN_RANGE, MAX_RANGE)
            if new_number not in generated_numbers:
                generated_numbers.append(new_number)

            if len(generated_numbers) == 6:
                exitLoop = True
        generated_numbers.sort()
        print("{:3}{:3}{:3}{:3}{:3}{:3}".format(generated_numbers[0], generated_numbers[1], generated_numbers[2], generated_numbers[3], generated_numbers[4], generated_numbers[5]))





main()