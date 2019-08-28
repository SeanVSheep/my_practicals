WORDS = ['hi', 'hello', 'you', 'poop', 'haha', 'hi', 'you', 'you']
ages_dict = {"Bill": 21, "janes": 34, "jack": 56}


def main():
    count_dict = {}
    for word in WORDS:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    print(count_dict)

#main()


def main2():
    count_dict = {}
    for word in WORDS:
        try:
            count_dict[word] += 1
        except KeyError:
            count_dict[word] = 1

    print(count_dict)

    count_dict["bob"] = count_dict.get("bob", 0) + 1

    print(count_dict)

#main2()

def dict_activity():
    name = input("Name: ")
    age = int(input("Age: "))
    ages_dict[name] = age
    for char in ages_dict:
        print("{:10} - {:6}".format(char, ages_dict[char]))



dict_activity()