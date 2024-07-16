# Text based navigation

# This program teaches about navigation using dictionaries

# Define the rooms and their connections
rooms = {
    'hall': {'north': 'bedroom', 'east': 'kitchen', 'south': None, 'west': None},
    'bedroom': {'north': None, 'east': None, 'south': 'hall', 'west': None},
    'kitchen': {'north': None, 'east': None, 'south': None, 'west': 'hall'}
}

# Start in the hall
current_room = 'hall'

print("Welcome to the House Navigator!")
print("You can move by typing: north, south, east, or west")
print("Type 'quit' to exit the program")

while True:
    print(f"\nYou are in the {current_room}.")
    direction = input("Which direction do you want to go? ").lower()

    if direction == 'quit':
        break

    if direction in rooms[current_room]:
        if rooms[current_room][direction] is not None:
            current_room = rooms[current_room][direction]
            print(f"You move to the {current_room}.")
        else:
            print("You can't go that way!")
    else:
        print("Invalid direction. Please use north, south, east, or west.")