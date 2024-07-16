# Simple game loop

import random

secret_number = random.randint(1, 10)
attempts = 3

print("I'm thinking of a number between 1 and 10.")
print(f"You have {attempts} attempts to guess it.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"Sorry, you're out of attempts. The number was {secret_number}.")
