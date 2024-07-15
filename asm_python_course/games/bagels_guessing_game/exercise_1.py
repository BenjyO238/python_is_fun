# Random number generation

import random

print("Let's generate a random number between 1 and 10!")
random_number = random.randint(1, 10)
print(f"The random number is: {random_number}")

print("\nNow, let's shuffle a list of numbers:")
numbers = list(range(1, 6))
print(f"Original list: {numbers}")
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

