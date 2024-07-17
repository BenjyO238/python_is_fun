# Define the locations and their descriptions
locations = {
    'field': {
        'description': 'You are standing in a vast open field. You see flowers and trees.',
        'items': ['flower', 'tree'],
        'north': 'forest',
        'east': 'cave',
        'south': None,
        'west': 'beach'
    },
    'forest': {
        'description': 'You are in a dense forest. You hear birds chirping.',
        'items': ['stick', 'bird'],
        'north': None,
        'east': 'lake',
        'south': 'field',
        'west': 'house'
    },
    'cave': {
        'description': 'You have entered a dark cave. It is cold and damp.',
        'items': ['rock', 'torch'],
        'north': None,
        'east': 'mountain',
        'south': None,
        'west': 'field'
    },
    'lake': {
        'description': 'You are at the edge of a beautiful lake. The water is crystal clear.',
        'items': ['fish', 'shell'],
        'north': 'rainforest',
        'east': None,
        'south': None,
        'west': 'forest'
    },
    'rainforest': {
        'description': 'You are in a lush rainforest. It is teeming with life.',
        'items': ['fruit', 'vine'],
        'north': None,
        'east': 'time_machine_room',
        'south': 'lake',
        'west': None
    },
    'time_machine_room': {
        'description': 'You are in a hidden room. It contains a strange device.',
        'items': ['can of tuna', 'loaf of bread', 'time machine'],
        'north': None,
        'east': None,
        'south': None,
        'west': 'rainforest'
    },
    'beach': {
        'description': 'You are on a sunny beach. The waves are gently crashing on the shore.',
        'items': ['sand', 'shell'],
        'north': None,
        'east': 'field',
        'south': None,
        'west': None
    },
    'house': {
        'description': 'You are in a cozy house. It feels warm and safe here.',
        'items': ['key', 'book'],
        'north': None,
        'east': 'forest',
        'south': None,
        'west': None
    },
    'mountain': {
        'description': 'You are on a tall mountain. The view is breathtaking.',
        'items': ['stone', 'eagle feather'],
        'north': None,
        'east': None,
        'south': None,
        'west': 'cave'
    }
}

# Define the starting location
current_location = 'field'

# Define the maximum items a player can carry
max_items = 3
inventory = []

# Helper function to find path
def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in locations:
        return None
    for direction in ['north', 'east', 'south', 'west']:
        if locations[start][direction]:
            next_location = locations[start][direction]
            if next_location not in path:
                new_path = find_path(next_location, end, path)
                if new_path:
                    return [start] + [direction] + new_path
    return None

# Main game loop
while True:
    # Print the current location description
    print(locations[current_location]['description'])

    # Get the player's input
    command = input("What would you like to do? (north, east, south, west, look, pick up [item], drop [item], inventory): ").strip().lower()

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
    elif command.startswith('pick up '):
        item = command[8:]
        if item in locations[current_location]['items']:
            if len(inventory) < max_items:
                inventory.append(item)
                locations[current_location]['items'].remove(item)
                print(f"You have picked up the {item}.")
                if item == 'time machine':
                    print("Congratulations! You have found the time machine and won the game!")
                    break
            else:
                print("You can't carry any more items. Try dropping something.")
        else:
            print(f"There is no {item} here.")

    # Handle the drop command
    elif command.startswith('drop '):
        item = command[5:]
        if item in inventory:
            inventory.remove(item)
            locations[current_location]['items'].append(item)
            print(f"You have dropped the {item}.")
        else:
            print(f"You don't have a {item}.")

    # Handle the inventory command
    elif command == 'inventory':
        print("You are carrying:", ', '.join(inventory))

    # Handle the map to home command
    elif command == 'map to home':
        path = find_path(current_location, 'field')
        if path:
            directions = [step for step in path if step in ['north', 'east', 'south', 'west']]
            print("Directions to home:", ' --> '.join(directions))
        else:
            print("No path to home found.")

    # Handle the map to end command
    elif command == 'map to end':
        path = find_path(current_location, 'time_machine_room')
        if path:
            directions = [step for step in path if step in ['north', 'east', 'south', 'west']]
            print("Directions to the end:", ' --> '.join(directions))
        else:
            print("No path to the end found.")

    # Handle invalid commands
    else:
        print("Invalid command. Please try again.")
