VOWELS = 'aeiou'
def main():
    user_name = input("Please enter your name: ").lower()
    total_vowels = 0
    for char in user_name:
        if char in VOWELS:
            total_vowels += 1
    print("Out of {} letters, {} has {} vowels".format(len(user_name), user_name, total_vowels))


main()