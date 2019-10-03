"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

CORRECT_VALUES = 'cv'
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

choice = int(input("1) choose your input\n2) Generate random word\n>>>"))
word_format = ''
if choice == 1:
    word_format = input("Please enter #'s for constants and %'s for vowels: ").lower()
elif choice == 2:
    word_length = random.randint(1, 10)
    for x in range(word_length):
        if random.randint(1, 2) == 1:
            word_format += CONSONANTS[random.randint(0, 20)]
        else:
            word_format += VOWELS[random.randint(0, 4)]
word = ""
for kind in word_format:
    if kind == '#':
        word += random.choice(CONSONANTS)
    elif kind == '%':
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)