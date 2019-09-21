"""CP1404 Practical - Languages prac"""

from week_06.programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    languages = [ruby, python, visual_basic]
    # print(ruby.is_dynamic())
    print("The dynamically typed languages are:")
    for l in languages:
        if l.is_dynamic():
            print(l.name)








main()