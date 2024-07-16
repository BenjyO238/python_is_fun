# Define the locations and their descriptions
locations = {
    'field': {
        'description': 'You are standing in a vast open field. You see flowers and trees.',
        'items': ['flower', 'tree'],
        'north': 'forest',
        'east': 'cave',
        'south': None,
        'west': None
    },
    'forest': {
        'description': 'You are in a dense forest. You hear birds chirping.',
        'items': ['stick', 'bird'],
        'north': None,
        'east': 'lake',
        'south': 'field',
        'west': None
    },
    'cave': {
        'description': 'You have entered a dark cave. It is cold and damp.',
        'items': ['rock', 'torch'],
        'north': None,
        'east': None,
        'south': None,
        'west': 'field'
    },
    'lake': {
        'description': 'You are at the edge of a beautiful lake. The water is crystal clear.',
        'items': ['fish', 'shell'],
        'north': 'treasure_room',
        'east': None,
        'south': None,
        'west': 'forest'
    },
    'treasure_room': {
        'description': 'You are in a room in a house. It feels cozy and warm.',
        'items': ['treasure'],
        'north': None,
        'east': None,
        'south': 'lake',
        'west': None
    }
}

# Define the starting location
current_location = 'field'

# Define the item needed to win
winning_item = 'treasure'

# Main game loop
while True:
    # Print the current location description
    print(locations[current_location]['description'])

    # Get the player's input
    command = input("What would you like to do? (north, east, south, west, look, pick up [item]): ").strip().lower()

    # Handle movement commands
    if command in ['north', 'east', 'south', 'west']:
        if locations[current_location][command] is not None:
            current_location = locations[current_location][command]
        else:
            print("You can't go that way.")

    # Handle the look command
    elif command == 'look':
        print("You see:", ', '.join(locations[current_location]['items']))

    # Handle the pick up command
    elif command.startswith('pick up'):
        item = command[8:]
        if item in locations[current_location]['items']:
            if item == winning_item:
                print(f"Congratulations! You have found the {winning_item} and won the game!")
                break
            else:
                print(f"You have picked up the {item}.")
                locations[current_location]['items'].remove(item)
        else:
            print(f"There is no {item} here.")

    # Handle invalid commands
    else:
        print("Invalid command. Please try again.")
