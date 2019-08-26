
def which_is_bigger(numb1, numb2):
    if numb1 > numb2:
        print("{} is bigger than {}".format(numb1, numb2))
    elif numb1 < numb2:
        print("{} is bigger than {}".format(numb2, numb1))
    else:
        print("both same value")

def main():


    numb1 = float(input('Choose first number: '))
    numb2 = float(input('Choose first number: '))

    which_is_bigger(numb1, numb2)


main()