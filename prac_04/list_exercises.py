
def question_one():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))

    print(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The smallest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

#question_one()

