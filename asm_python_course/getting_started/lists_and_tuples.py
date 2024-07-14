
### Lists
# Getting single elements from list
# Example 1: Basic list indexing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
print(fruits[-1])  # Output: date (last element)

# Example 2: Accessing elements in a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])  # Output: 5

# Example 3: Using variables as indices
index = 2
print(fruits[index])  # Output: cherry

# How to get sections of lists, called slicing
# Example 1: Basic slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])  # Output: [2, 3, 4, 5]
print(numbers[:4])   # Output: [0, 1, 2, 3]
print(numbers[6:])   # Output: [6, 7, 8, 9]

# Example 2: Slicing with step
print(numbers[1:8:2])  # Output: [1, 3, 5, 7]
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Example 3: Negative indices in slicing
print(numbers[-5:-2])  # Output: [5, 6, 7]

# How to add elements to a list
# Example 1: Append method
colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors)  # Output: ['red', 'green', 'blue', 'yellow']

# Example 2: Insert method
colors.insert(1, "orange")
print(colors)  # Output: ['red', 'orange', 'green', 'blue', 'yellow']

# Example 3: Extend method
more_colors = ["purple", "pink"]
colors.extend(more_colors)
print(colors)  # Output: ['red', 'orange', 'green', 'blue', 'yellow', 'purple', 'pink']

# Example 4: Concatenation
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
all_numbers = numbers + more_numbers
print(all_numbers)  # Output: [1, 2, 3, 4, 5, 6]

# How to remove elements from a list
# Example 1: Remove method
animals = ["cat", "dog", "elephant", "lion", "tiger"]
animals.remove("elephant")
print(animals)  # Output: ['cat', 'dog', 'lion', 'tiger']

# Example 2: Pop method
popped_animal = animals.pop()
print(popped_animal)  # Output: tiger
print(animals)  # Output: ['cat', 'dog', 'lion']

# Example 3: Pop with index
second_animal = animals.pop(1)
print(second_animal)  # Output: dog
print(animals)  # Output: ['cat', 'lion']

# Example 4: Del statement
del animals[0]
print(animals)  # Output: ['lion']

# Example 5: Clear method
animals.clear()
print(animals)  # Output: []


# How to iterate over a list
# Example 1: Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Using range and len
for i in range(len(fruits)):
    print(f"Fruit {i + 1}: {fruits[i]}")

# Example 3: List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Squares of even numbers: {even_squares}")

# Example 4: While loop
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# How to enumerate a list
# Example 1: Basic enumeration
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Example 2: Enumeration with custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit {index}: {fruit}")

# Example 1: Creating a numbered list of tasks
tasks = ["Buy groceries", "Clean the house", "Do laundry", "Cook dinner"]
for number, task in enumerate(tasks, start=1):
    print(f"Task {number}: {task}")

# Output:
# Task 1: Buy groceries
# Task 2: Clean the house
# Task 3: Do laundry
# Task 4: Cook dinner

# Example 2: Finding indices of specific elements
numbers = [10, 5, 8, 3, 5, 2, 7, 5]
indices_of_five = [index for index, num in enumerate(numbers) if num == 5]
print(f"Indices of 5: {indices_of_five}")
# Output: Indices of 5: [1, 4, 7]

# Example 3: Creating a dictionary with value frequencies
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
word_freq = {}
for index, word in enumerate(words):
    if word in word_freq:
        word_freq[word].append(index)
    else:
        word_freq[word] = [index]
print(word_freq)
# Output: {'apple': [0, 2], 'banana': [1, 4], 'cherry': [3], 'date': [5]}

# Example 4: Alternating operations based on index
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num * 2 if index % 2 == 0 else num + 1 for index, num in enumerate(numbers)]
print(result)
# Output: [2, 3, 6, 5, 10, 7, 14, 9, 18, 11]

#Sorting a list
# Basic sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print(f"Sorted numbers: {sorted_numbers}")

# Sorting in reverse order
reverse_sorted = sorted(numbers, reverse=True)
print(f"Reverse sorted: {reverse_sorted}")

# Sorting in place
numbers.sort()
print(f"Original list sorted: {numbers}")

# Sorting strings
fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print(f"Sorted fruits: {sorted_fruits}")

# Sorting with a key function
words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=len)
print(f"Sorted by length: {sorted_by_length}")


# Getting sum, min, max
numbers = [4, 2, 8, 1, 9, 5]

# Sum
total = sum(numbers)
print(f"Sum: {total}")

# Min
minimum = min(numbers)
print(f"Minimum: {minimum}")

# Max
maximum = max(numbers)
print(f"Maximum: {maximum}")

# Min and max with key function
words = ["apple", "banana", "cherry", "date"]
shortest = min(words, key=len)
longest = max(words, key=len)
print(f"Shortest word: {shortest}, Longest word: {longest}")

# Counting list elements
numbers = [1, 2, 3, 2, 4, 2, 5]
count_of_2 = numbers.count(2)
print(f"Count of 2: {count_of_2}")

# Reversing a list
numbers = [1, 2, 3, 4, 5]

# Reverse in place
numbers.reverse()
print(f"Reversed in place: {numbers}")

# Create a reversed copy
original = [1, 2, 3, 4, 5]
reversed_copy = list(reversed(original))
print(f"Original: {original}")
print(f"Reversed copy: {reversed_copy}")

# Reverse using slicing
sliced_reverse = original[::-1]
print(f"Reversed using slicing: {sliced_reverse}")

# Joining elements of a list into a string
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(f"Joined sentence: {sentence}")

# Splitting a string into a list
sentence = "Hello, world!"
words = sentence.split()
print(f"Split sentence: {words}")





### Tuples
# Creating tuples
# Creating tuples
point = (3, 4)
person = ("Alice", 25, "New York")

# Accessing elements
x = point[0]  # x = 3
y = point[1]  # y = 4
name, age, city = person  # Unpacking

print(f"Point: {point}")
print(f"x: {x}, y: {y}")
print(f"Person: {name} is {age} years old and lives in {city}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)

# Count method
count_2 = numbers.count(2)
print(f"Number of 2s: {count_2}")  # Output: 3

# Index method
index_4 = numbers.index(4)
print(f"Index of 4: {index_4}")  # Output: 4

# Length of tuple
length = len(numbers)
print(f"Length of tuple: {length}")  # Output: 6

# Concatenation
more_numbers = numbers + (5, 6)
print(f"Concatenated tuple: {more_numbers}")

# Tuples for multiple assignment
# Swapping variables
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Returning multiple values from a function
def calculate_stats(numbers):
    return sum(numbers), len(numbers), sum(numbers) / len(numbers)

total, count, average = calculate_stats([1, 2, 3, 4, 5])
print(f"Total: {total}, Count: {count}, Average: {average}")

