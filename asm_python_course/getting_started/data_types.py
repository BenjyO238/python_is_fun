# Here are some common math symbols
# = is assignment
# == is equality (this is tricky and we'll talk about it later)
# != is inequality
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to

# In python data can be of different types. Let's review these.
# int: whole numbers, positive or negative, no decimals or fractions
# float: numbers that have decimals. For example 3.14
# str: strings. For example "hello". Strings need to be single or double-quoted.
# bool: True or False
# list: an ordered collection of items. For example [1, 2, 3].
# tuple: an ordered collection of items. For example (1, 2, 3). But you can't change the items in a tuple.
# dict: an unordered collection of key-value pairs. For example {"name": "John", "age": 30}.
# set: an unordered collection of unique items. For example {1, 2, 3}.

# Let's practice some data types.
# We'll start with strings:
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


# String creation and concatenation
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Alice!

# String formatting
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)  # Output: Alice is 30 years old.


# String case methods
text = "Python Programming is AWESOME!"

# Convert to lowercase
lowercase_text = text.lower()
print(lowercase_text)  # Output: python programming is awesome!

# Convert to uppercase
uppercase_text = text.upper()
print(uppercase_text)  # Output: PYTHON PROGRAMMING IS AWESOME!

# Capitalize (first character uppercase, rest lowercase)
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Python programming is awesome!

# Title case (first character of each word uppercase)
title_case_text = text.title()
print(title_case_text)  # Output: Python Programming Is Awesome!

# Swapcase (swap upper and lowercase)
swapped_case_text = text.swapcase()
print(swapped_case_text)  # Output: pYTHON pROGRAMMING IS awesome!

# Case-insensitive comparison
text1 = "Python"
text2 = "python"
print(text1.lower() == text2.lower())  # Output: True

# Case-insensitive search
sentence = "Python is easy to learn"
search_term = "PYTHON"
if search_term.lower() in sentence.lower():
    print(f"Found '{search_term}' in the sentence")
# Output: Found 'PYTHON' in the sentence

# String slicing
print(text[0:6])  # Output: python
print(text[-11:])  # Output: programming

# String splitting and joining
words = text.split()
print(words)  # Output: ['python', 'programming']
new_text = " ".join(words)
print(new_text)  # Output: python programming

# Check if string contains substring
print("python" in text)  # Output: True

# String length
print(len(text))  # Output: 19


# Numbers
# Basic arithmetic
a, b = 5, 2
print(a + b)  # Addition: 7
print(a - b)  # Subtraction: 3
print(a * b)  # Multiplication: 10
print(a / b)  # Division: 2.5
print(a // b)  # Integer division: 2
print(a % b)  # Modulus: 1
print(a ** b)  # Exponentiation: 25

# Float operations
x = 3.14
y = 2.5
print(round(x, 1))  # Rounding: 3.1
print(abs(-y))  # Absolute value: 2.5

# Type conversion
int_num = int(x)
float_num = float(a)
print(int_num, float_num)  # Output: 3 5.0

# Using math module
import math
print(math.pi)  # Pi: 3.141592653589793
print(math.sqrt(16))  # Square root: 4.0

# Boolean values
is_sunny = True
is_raining = False

# Boolean operations
print(is_sunny and is_raining)  # AND: False
print(is_sunny or is_raining)  # OR: True
print(not is_sunny)  # NOT: False

# Comparison operators
x, y = 5, 10
print(x < y)  # Less than: True
print(x >= y)  # Greater than or equal to: False
print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True

# Boolean in control flow
if is_sunny:
    print("Wear sunglasses!")
else:
    print("No need for sunglasses.")

# Truthy and Falsy values
empty_list = []
if empty_list:
    print("List has items")
else:
    print("List is empty")  # This will be printed



# We won't cover bytes but this is how computers store data:
def string_to_bytes(text):
    byte_array = text.encode('utf-8')
    print(f"'{text}' as bytes: {byte_array}")
    print("Individual byte values:")
    for byte in byte_array:
        print(f"{byte:08b}", end=" ")

word = 'a'
# Example usage
string_to_bytes(word)
# string_to_bytes("Hello, World!")
