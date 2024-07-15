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


# Print index and value
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


# Print every third number from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(numbers), 3):
    print(numbers[i])
# Output: 0, 3, 6, 9


# Used when you need both the index and value of items in a list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry


# Used to iterate through each character in a string
word = "Python"
for char in word:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n


# Used when you need to iterate over multiple dimensions. These are nested for loops.
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
# Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)


# The else block executes when the loop completes normally (not broken)
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed successfully


# Used to skip the rest of the current iteration and continue to the next
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4


# Used to exit the loop prematurely when a condition is met
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2


# A concise way to create a new list based on an existing list
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]


# Used to iterate through key-value pairs in a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: New York










