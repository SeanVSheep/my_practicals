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
            number_of_picks = int(input("How many quick picks? "))
            while number_of_picks <= 0:
                number_of_picks = int(input("Picks must be greater then 0: "))
            exitLoop = True
        except ValueError:
            print("ERROR! Please enter numerical value")

    print_quick_picks(number_of_picks)
    #optomised_quick_picks(number_of_picks)


def optomised_quick_picks(number_of_picks):
    #code extracted from solutions to show where I can improve my solution
    for i in range(number_of_picks):
        quick_picks = []
        for j in range(NUMBERS_ON_A_LINE):
            number = random.randint(MIN_RANGE, MAX_RANGE)
            while number in quick_picks:
                number = random.randint(MIN_RANGE, MAX_RANGE)
            quick_picks.append(number)
        quick_picks.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join("{:2}".format(number) for number in quick_picks))


def print_quick_picks(number_of_picks):
    #my code for solution to exercise
    for i in range(number_of_picks):
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