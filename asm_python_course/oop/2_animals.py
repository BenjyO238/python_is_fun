# Define a base class called Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some generic animal sound"

# Define a subclass called Dog that inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof!"

# Define a subclass called Cat that inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

# Create instances (objects) of the Dog and Cat classes
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Black")

# Interact with the objects
print(f"{dog.name} the Dog says: {dog.speak()}")
print(f"{cat.name} the Cat says: {cat.speak()}")
