import wikipedia


def main():
    user_input = input("S - Search\nP - Page Summary\nQ - Quit\n>>> ")
    wiki_info = []
    while user_input.lower() != 'q':
        if user_input.lower() == 's':
            user_input = input("What would you like to search: ")
            wiki_info = wikipedia.search(user_input)
            for index, item in enumerate(wiki_info):
                print("{} - {}".format(index, item))
        elif user_input.lower() == 'p':
            if len(wiki_info) == 0:
                print("Search something first")
            else:
                valid_input = False
                while not valid_input:
                    try:
                        user_input = int(input("Enter the page number you'd like to search from search results: "))
                        valid_input = True
                    except ValueError:
                        print("Enter numerical value")
                try:
                    print(wikipedia.summary(wiki_info[user_input]))
                except:
                    print("Please choose correct search number!")
        else:
            print("Incorrect menu choice!")
        user_input = input("\nS - Search\nP - Page Summary\nQ - Quit\n>>> ")
main()