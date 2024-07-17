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

# Function to create an animal based on user input
def create_animal():
    animal_type = input("Do you want to create a 'dog' or a 'cat'? ").lower()
    name = input("Enter the name of the animal: ")
    age = int(input("Enter the age of the animal: "))

    if animal_type == 'dog':
        breed = input("Enter the breed of the dog: ")
        return Dog(name, age, breed)
    elif animal_type == 'cat':
        color = input("Enter the color of the cat: ")
        return Cat(name, age, color)
    else:
        print("Invalid animal type")
        return None

# Function to interact with an animal
def interact_with_animal(animal):
    print(f"{animal.name} the {animal.__class__.__name__} says: {animal.speak()}")

# Main function to run the program
def main():
    print("Let's create your first animal!")
    animal1 = create_animal()
    if animal1:
        interact_with_animal(animal1)

    print("\nLet's create your second animal!")
    animal2 = create_animal()
    if animal2:
        interact_with_animal(animal2)

# Run the main function
if __name__ == "__main__":
    main()
