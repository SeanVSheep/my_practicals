import shutil
import os


def main():
    os.chdir('FilesToSort')

    file_names = [name for name in os.listdir('.')]

    new_extensions = {}

    for name in file_names:

        if os.path.isdir(name):
            continue

        extension = name[name.find('.')+1:]
        if extension not in new_extensions:
            new_extensions[extension] = input("What category would you like to sort {} files into?".format(extension))

            try:
                os.mkdir(new_extensions[extension])
            except FileExistsError:
                pass

        shutil.move(name, new_extensions[extension])



main()