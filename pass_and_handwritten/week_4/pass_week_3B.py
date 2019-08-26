menu_items = ['Chicken', 'Nuggets', 'Pizza', 'Cheeseburger', 'Steak Sandwich', 'Crumbed Fish']

def print_item(food):
    print(food)

print("kids dinner menu:")
for i in range(len(menu_items)):
    print_item(menu_items[i])

print("All meals come with chips and a drink.")

