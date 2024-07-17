# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass  # To be defined by subclasses

    def feed(self):
        pass  # To be defined by subclasses

# Subclass for Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

    def feed(self):
        return f"{self.name} the Dog eats and then rolls over and barks happily!"

# Subclass for Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the post!"

    def feed(self):
        return f"{self.name} the Cat eats and then purrs contentedly!"

# Subclass for Bird
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def speak(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying!"

    def feed(self):
        return f"{self.name} the Bird eats and then flaps its wings excitedly!"

# Subclass for Elephant
class Elephant(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def speak(self):
        return "Trumpet!"

    def perform_trick(self):
        return f"{self.name} is balancing on a ball!"

    def feed(self):
        return f"{self.name} the Elephant eats and then sprays water with its trunk!"

# ZooGame class
class ZooGame:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def choose_animal(self):
        print("Choose an animal to interact with:")
        for i, animal in enumerate(self.animals):
            print(f"{i + 1}. {animal.name} the {animal.__class__.__name__}")
        choice = int(input("Enter the number of the animal: ")) - 1
        return self.animals[choice]

    def interact_with_animal(self, animal):
        print(f"You chose to interact with {animal.name} the {animal.__class__.__name__}.")
        print(f"{animal.name} says: {animal.speak()}")
        if isinstance(animal, Dog):
            action = input("Do you want to 'fetch' or 'feed' the dog? ").lower()
            if action == "fetch":
                print(animal.fetch())
            elif action == "feed":
                print(animal.feed())
        elif isinstance(animal, Cat):
            action = input("Do you want to 'scratch' or 'feed' the cat? ").lower()
            if action == "scratch":
                print(animal.scratch())
            elif action == "feed":
                print(animal.feed())
        elif isinstance(animal, Bird):
            action = input("Do you want to 'fly' or 'feed' the bird? ").lower()
            if action == "fly":
                print(animal.fly())
            elif action == "feed":
                print(animal.feed())
        elif isinstance(animal, Elephant):
            action = input("Do you want to 'perform trick' or 'feed' the elephant? ").lower()
            if action == "perform trick":
                print(animal.perform_trick())
            elif action == "feed":
                print(animal.feed())

    def play(self):
        while True:
            animal = self.choose_animal()
            self.interact_with_animal(animal)
            cont = input("Do you want to interact with another animal? (yes/no) ").lower()
            if cont != "yes":
                break

# Creating instances of animals
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Black")
bird = Bird("Tweety", 1, "Canary")
elephant = Elephant("Dumbo", 10, "Large")

# Creating the game and adding animals
game = ZooGame()
game.add_animal(dog)
game.add_animal(cat)
game.add_animal(bird)
game.add_animal(elephant)

# Playing the game
game.play()
