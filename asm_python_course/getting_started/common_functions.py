# Here are common functions that we'll use in the rest of the course.

# printing
print("Hello, World!")
print("The answer is:", 42)


# Basic input from a user
name = input("Enter your name: ")
print("Hello,", name)

# Converting (casting) data types
x = int("10")
print(x + 5)  # Output: 15

y = float("3.14")
print(y * 2)  # Output: 6.28

z = str(42)
print("The answer is " + z)  # Output: The answer is 42

# Input with type conversion
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1, "years old.")

# Using input in a calculation
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)


# length of data structures or strings
text = "Python"
print(len(text))  # Output: 6

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3


# Getting the data type
x = 5
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>


# Aggregate math functions
numbers = [1, 5, 3, 2, 4]
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1
print(sum(numbers))  # Output: 15


# rounding
x = 3.7
print(round(x))  # Output: 4

y = 2.1234
print(round(y, 2))  # Output: 2.12

# absolute value
print(abs(-5))  # Output: 5
print(abs(3.14))  # Output: 3.14


# sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']


# Converting data structures
tuple_example = (1, 2, 3)
list_from_tuple = list(tuple_example)
print(list_from_tuple)  # Output: [1, 2, 3]

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3}

numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4}

