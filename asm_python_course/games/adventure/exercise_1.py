# Dictionary basics
# This program teaches about dictionaries and accessing their values

# Create a dictionary of animals and their sounds
animal_sounds = {
    'dog': 'woof',
    'cat': 'meow',
    'cow': 'moo',
    'duck': 'quack'
}

# Print all animals and their sounds
print("All animals and their sounds:")
for animal, sound in animal_sounds.items():
    print(f"The {animal} says {sound}!")

# Ask the user for an animal and print its sound
while True:
    user_animal = input("\nEnter an animal name (or 'quit' to exit): ").lower()

    if user_animal == 'quit':
        break

    if user_animal in animal_sounds:
        print(f"The {user_animal} says {animal_sounds[user_animal]}!")
    else:
        print(f"Sorry, I don't know what sound a {user_animal} makes.")