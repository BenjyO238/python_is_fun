# Define a class for a Pet
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5

    def feed(self):
        self.hunger -= 1
        return f"You fed {self.name}. Hunger level: {self.hunger}"

    def play(self):
        self.happiness += 1
        return f"You played with {self.name}. Happiness level: {self.happiness}"

    def status(self):
        return f"{self.name}'s hunger level: {self.hunger}, happiness level: {self.happiness}"

# Get user input to name the pet
pet_name = input("Enter the name of your pet: ")
pet = Pet(pet_name)

# Interact with the pet
while True:
    action = input("Do you want to 'feed', 'play' or 'check status' of your pet? (or 'quit' to exit): ").lower()
    if action == 'quit':
        break
    elif action == 'feed':
        print(pet.feed())
    elif action == 'play':
        print(pet.play())
    elif action == 'check status':
        print(pet.status())
    else:
        print("Invalid action")
