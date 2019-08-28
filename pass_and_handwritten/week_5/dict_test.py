WORDS = ['hi', 'hello', 'you', 'poop', 'haha', 'hi', 'you', 'you']

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

main2()