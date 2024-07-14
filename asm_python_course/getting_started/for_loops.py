"""
For loops in Python are super important. For loops are used to iterate over a sequence
(list, tuple, dictionary, set, string) or other iterable objects. There different ways to write them.
"""

# Used when you want to iterate through each item in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Repeat an action 3 times
for _ in range(3):
    print("Hello")
# Output:
# Hello
# Hello
# Hello


# Used when you need to iterate a specific number of times
for i in range(5):
    print(f"I'm on number {i}")

# Let's see some more range examples
# Generates numbers from 2 to 6 (7 is excluded)
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6


# Counts down from 5 to 1
for i in range(5, 0, -1):
    print(i)
# Output: 5, 4, 3, 2, 1

fruits = ["apple", "banana", "cherry", "date"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
# Index 3: date

# Generate years from 2020 to 2025
for year in range(2020, 2026):
    print(year)
# Output: 2020, 2021, 2022, 2023, 2024, 2025

# Generate odd numbers from 9 to 1 in descending order
for i in range(9, 0, -2):
    print(i)
# Output: 9, 7, 5, 3, 1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print every third number
for i in range(0, len(numbers), 3):
    print(numbers[i])
# Output: 0, 3, 6, 9








