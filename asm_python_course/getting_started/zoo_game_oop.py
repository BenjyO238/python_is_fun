# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
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

# Subclass for Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the post!"

# Subclass for Bird
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def speak(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying!"

# ZooGame class
class ZooGame:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def play(self):
        for animal in self.animals:
            print(f"{animal.name} the {animal.__class__.__name__} says: {animal.speak()}")
            if isinstance(animal, Dog):
                print(animal.fetch())
            elif isinstance(animal, Cat):
                print(animal.scratch())
            elif isinstance(animal, Bird):
                print(animal.fly())

# Creating instances of animals
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Black")
bird = Bird("Tweety", 1, "Canary")

# Creating the game and adding animals
game = ZooGame()
game.add_animal(dog)
game.add_animal(cat)
game.add_animal(bird)

# Playing the game
game.play()
