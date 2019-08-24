
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

def woefully_inadequate_security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    if input("Please verify username: ") in usernames:
        print("Access granted")
    else:
        print("Access denied")

#woefully_inadequate_security_checker()