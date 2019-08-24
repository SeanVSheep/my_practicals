VOWELS = 'aeiou'
def main():
    #user_name = input("Please enter your name: ").lower()
    user_name = 'Sean Spring'
    total_vowels = 0
    for char in user_name:
        if char in VOWELS:
            total_vowels += 1
    print("Out of {} letters, {} has {} vowels".format(len(user_name), user_name, total_vowels))

    new_name = "".join([c for c in user_name if c.lower() not in VOWELS])
    print(new_name)


def create():
    my_create_file = open('subjects.txt', 'w')

    my_create_file.write('CP1404\n')
    my_create_file.write('CP2403\n')
    my_create_file.write('MA1000\n')
    my_create_file.write('CP1402\n')

    my_create_file.close()

#create()


def main2():
    my_file = open('subjects.txt', 'r')

    subjects = [line.strip() for line in my_file]

    my_file.close()

    #subjects = my_file.readlines()

    print(subjects)

    first_year_subjects = [c for c in subjects if c[2] == '1']
    print(first_year_subjects)


main2()