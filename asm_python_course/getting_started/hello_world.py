# This is a comment. It won't show up in the output. And here's you first line of code. 
print("Hello, World!")

# These are variables. They store values. Let's practice in the repl
x = 5
y = 10
z = x + y
print(z)

# Let's practice some math. Python uses symbols for math
# + is addition
# - is subtraction
# * is multiplication
# / is division
# % is modulus
# ** is exponent
# // is floor division

# Use the variables below to explore some math operations. Let's try
# all of the symbols above. And don't forget we can use parentheses
# Basic variables
a = 10
b = 3

# Addition
print("Addition:")
result = a + b
print(result)  # Output: 13

# Subtraction
print("\nSubtraction:")
result = a - b
print(result)  # Output: 7

# Multiplication
print("\nMultiplication:")
result = a * b
print(result)  # Output: 30

# Division
print("\nDivision:")
result = a / b
print(result)  # Output: 3.3333333333333335

# Integer Division (floor division)
print("\nInteger Division:")
result = a // b
print(result)  # Output: 3

# Modulus (remainder)
print("\nModulus:")
result = a % b
print(result)  # Output: 1

# Exponentiation
print("\nExponentiation:")
result = a ** b
print(result)  # Output: 1000

# Examples with parentheses

print("\nExamples with parentheses:")

# Example 1: (a + b) * 2
result = (a + b) * 2
print(result)  # Output: 26

# Example 2: a * (b + 5)
result = a * (b + 5)
print(result)  # Output: 80

# Example 3: (a + b) / (a - b)
result = (a + b) / (a - b)
print(result)  # Output: 1.8571428571428572

# Example 4: Complex expression
x = 5
y = 2
z = 3
result = (x + y) * z - (x / y)
print(result)  # Output: 18.5



# There a few ways of formatting strings for when we print them:
# Setup some variables for our examples
name = "Alice"
age = 30
height = 1.75
favorite_colors = ['blue', 'green']

# 1. Basic variable substitution
# Using str.format()
print("My name is {} and I'm {} years old.".format(name, age))

# Using f-string
print(f"My name is {name} and I'm {age} years old.")

# 2. Specifying variable order
# Using str.format()
print("I'm {1} years old and my name is {0}.".format(name, age))

# Using f-string (order is implicit)
print(f"I'm {age} years old and my name is {name}.")

# 3. Named placeholders
# Using str.format()
print("My name is {name} and I'm {age} years old.".format(name=name, age=age))

# Using f-string (names are implicit)
print(f"My name is {name} and I'm {age} years old.")

# 4. Formatting numbers
# Using str.format()
print("I am {:.2f} meters tall.".format(height))

# Using f-string
print(f"I am {height:.2f} meters tall.")

# 5. Calling methods within the formatting
# Using str.format()
print("My favorite color is {}.".format(favorite_colors[0].upper()))

# Using f-string
print(f"My favorite color is {favorite_colors[0].upper()}.")

# 6. Using expressions
# Using str.format()
print("Next year, I'll be {}.".format(age + 1))

# Using f-string
print(f"Next year, I'll be {age + 1}.")


# 8. Using dictionaries
person = {'name': 'Bob', 'age': 25}

# Using str.format()
print("His name is {name} and he's {age}.".format(**person))

# Using f-string
print(f"His name is {person['name']} and he's {person['age']}.")

# 9. Debugging - showing variable names and values (Python 3.8+)
# This is unique to f-strings
x = 10
y = 20
print(f"{x=}, {y=}")  # Output: x=10, y=20
# f-string
name = "Alice"
age = 25
print(f"{name} is {age} years old.")

