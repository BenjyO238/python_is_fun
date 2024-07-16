# Item collection game

# This program teaches about lists, removing items, and win conditions

items = ['apple', 'book', 'key', 'treasure']
collected_items = []

print("Welcome to the Item Collector!")
print("Your goal is to collect all items, including the treasure.")
print("Commands: 'look' to see items, 'take [item]' to collect an item, 'quit' to exit")

while True:
    command = input("\nWhat would you like to do? ").lower()

    if command == 'quit':
        break
    elif command == 'look':
        if items:
            print("You see:", ", ".join(items))
        else:
            print("There are no items left to collect!")
    elif command.startswith('take '):
        item = command[5:]  # Get the item name after 'take '
        if item in items:
            items.remove(item)
            collected_items.append(item)
            print(f"You have taken the {item}.")
            if item == 'treasure':
                print("Congratulations! You found the treasure and won the game!")
                break
        else:
            print(f"There is no {item} here.")
    else:
        print("Invalid command. Please try again.")

print("\nGame Over!")
print("Items you collected:", ", ".join(collected_items))