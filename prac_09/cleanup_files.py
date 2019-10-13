"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    #new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    correct_output = False
    new_name = filename
    while not correct_output:
        for position in range(len(new_name)):
            if new_name[0] != new_name[0].isalpha():
                new_name = new_name.capitalize()
            elif new_name[position] == new_name[position].islower() and new_name[position - 1] == new_name[position - 1].isalpha():
                new_name = create_new_string(new_name, position, '_')
                break
            elif position == (len(new_name)-1):
                correct_output = True
                print('HIT')
            print(position)


    return new_name

def create_new_string(string, position, new_character):
    new_string = string[:position] + new_character + string[position:]
    return new_string

print("hello to --- > {}".format(create_new_string('hello', 3, '_')))

def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\t\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        print("\n----------------\n")

        for filename in filenames:
            print("filename: {}".format(filename))
            full_name = os.path.join(directory_name, filename)
            print("full_name: {}".format(full_name))
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("new name: {}".format(new_name))
            #os.rename(full_name, new_name)

print("{}".format(get_fixed_filename('silentNight.txt')))

#demo_walk()