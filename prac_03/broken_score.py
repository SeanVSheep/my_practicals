def main():
    #allows user to enter a score and find out its value
    score = get_score()
    print(get_score_value(score))


def get_score():
    #user enters a number and returns value after error checking to make sure it is correct value
    exitLoop = False
    while not exitLoop:
        try:
            score = float(input("Enter score: "))
            exitLoop = True
        except ValueError:
            print("ERROR! Enter a number")
    return score



def get_score_value(score):
    #users score is passed in and returns its value back to main
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()