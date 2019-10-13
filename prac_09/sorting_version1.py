import shutil
import os


def main():
    os.chdir('FilesToSort')

    file_names = [name for name in os.listdir('.')]
    print(file_names)

    for name in file_names:
        try:
            os.mkdir(name[name.find('.')+1:])
        except FileExistsError:
            pass

        shutil.move(name, name[name.find('.')+1:])



main()