"""
CP1404 Practical
Write a program to count the occurrences of words in a string.
The program should ask the user for a string,
then print the counts of how many of each word are in the file.
"""

def main():
    entered_string = input("Please type a setence: ")
    count_dict = {}
    for word in entered_string.split():
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    organised_key_values = list(key for key in count_dict)
    organised_key_values.sort()

    for name in organised_key_values:
        print("{:{}} : {}".format(name, len(max(count_dict, key=len)), count_dict[name]))



main()