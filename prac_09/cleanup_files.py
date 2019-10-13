"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    #new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = filename
    new_name[0] = new_name[0].isalpha()

    return new_name


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