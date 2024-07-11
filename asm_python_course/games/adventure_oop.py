class Item:
    def __init__(self, name):
        self.name = name

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.directions = {}

    def add_item(self, item):
        self.items.append(item)

    def set_directions(self, directions):
        self.directions = directions

    def look(self):
        if self.items:
            return f"You see: {', '.join(item.name for item in self.items)}"
        else:
            return "There is nothing here."

class Game:
    def __init__(self):
        self.locations = self.create_locations()
        self.current_location = self.locations['field']
        self.winning_item = 'treasure'
        self.inventory = []

    def create_locations(self):
        # Define locations
        field = Location('field', 'You are standing in a vast open field. You see flowers and trees.')
        forest = Location('forest', 'You are in a dense forest. You hear birds chirping.')
        cave = Location('cave', 'You have entered a dark cave. It is cold and damp.')
        lake = Location('lake', 'You are at the edge of a beautiful lake. The water is crystal clear.')
        treasure_room = Location('treasure_room', 'You are in a room in a house. It feels cozy and warm.')

        # Add items to locations
        field.add_item(Item('flower'))
        field.add_item(Item('tree'))
        forest.add_item(Item('stick'))
        forest.add_item(Item('bird'))
        cave.add_item(Item('rock'))
        cave.add_item(Item('torch'))
        lake.add_item(Item('fish'))
        lake.add_item(Item('shell'))
        treasure_room.add_item(Item('treasure'))

        # Set directions for each location
        field.set_directions({'north': forest, 'east': cave})
        forest.set_directions({'south': field, 'east': lake})
        cave.set_directions({'west': field})
        lake.set_directions({'west': forest, 'north': treasure_room})
        treasure_room.set_directions({'south': lake})

        # Return a dictionary of all locations
        return {
            'field': field,
            'forest': forest,
            'cave': cave,
            'lake': lake,
            'treasure_room': treasure_room
        }

    def play(self):
        while True:
            # Print the current location description
            print(self.current_location.description)

            # Get the player's input
            command = input("What would you like to do? (north, east, south, west, look, pick up [item]): ").strip().lower()

            # Handle movement commands
            if command in ['north', 'east', 'south', 'west']:
                if command in self.current_location.directions:
                    self.current_location = self.current_location.directions[command]
                else:
                    print("You can't go that way.")

            # Handle the look command
            elif command == 'look':
                print(self.current_location.look())

            # Handle the pick up command
            elif command.startswith('pick up'):
                item_name = command[8:]
                for item in self.current_location.items:
                    if item.name == item_name:
                        if item.name == self.winning_item:
                            print(f"Congratulations! You have found the {self.winning_item} and won the game!")
                            return
                        else:
                            print(f"You have picked up the {item.name}.")
                            self.inventory.append(item)
                            self.current_location.items.remove(item)
                        break
                else:
                    print(f"There is no {item_name} here.")

            # Handle invalid commands
            else:
                print("Invalid command. Please try again.")

# Create a game instance and start the game
game = Game()
game.play()
