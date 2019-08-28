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

    for name in ages_dict:
        print("{:10} - {:6}".format(name, ages_dict[name]))

    for name, age in ages_dict.items():
        print("{:10} - {:6}".format(name, age))

#dict_activity()

def test_func():
    #hello = zip("abc", [1, 2, 3])
    #hello looks like this [('a', 1), ('b', 2) ('c', 3)]
    goodbye = dict(zip("abc", [1, 2, 3]))
    print(goodbye)

#test_func()


def dict_comprehension():
    dict_ages = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}

    new_dict = {name: age for name, age in dict_ages.items() if age < 18}

    print(new_dict)

    test_dict = {k:v for k,v in dict_ages.items()}

    print(test_dict)

    test_dict2 = {v:k for k,v in dict_ages.items()}

    print(test_dict2)

#dict_comprehension()

#testing branches

print("feedback branch")






