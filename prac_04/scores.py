"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv", 'r')
    scores_data2 = []
    for line in scores_file:
        scores_data2.append(line.strip().split(','))
    print(scores_data2)


    scores_file.close()
    print("\n\n\nMY OUT PUTT\n------------------------\n")
    #print('length of inner lists(z) is {}\nlength of entire list(x) is {}'.format(len(scores_data2), len(scores_data2[0])))
    for x in range(len(scores_data2[0])):
        average = 0
        max = 0
        min = 100
        for z in range(len(scores_data2)):
            if z == 0:
                print("{} Scores:".format(scores_data2[z][x]))
            elif z > 0 and z < 10:
                if max < int(scores_data2[z][x]):
                    max = int(scores_data2[z][x])
                if min > int(scores_data2[z][x]):
                    min = int(scores_data2[z][x])
                print(scores_data2[z][x])
                average += int(scores_data2[z][x])
            else:
                if max < int(scores_data2[z][x]):
                    max = int(scores_data2[z][x])
                if min > int(scores_data2[z][x]):
                    min = int(scores_data2[z][x])
                print(scores_data2[z][x])
                average += int(scores_data2[z][x])
                print("Max: {}\nMin: {}\nAvg: {}\n".format(max, min, average/10))



main()