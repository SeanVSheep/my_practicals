def main():
    #allows user to enter a score and find out its value
    score = float(input("Enter score: "))
    print(get_score_value(score))

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