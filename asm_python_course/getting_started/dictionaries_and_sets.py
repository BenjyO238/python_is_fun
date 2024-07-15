### Dictionaries

# A dictionary is a collection of key-value pairs.

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 13,
    "grade": 7,
    "favorite_subject": "Science"
}

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Modifying values
student["age"] = 14
print(f"Age: {student['age']}")

# Adding a new key-value pair
student["hobby"] = "Reading"
print(f'Hobby: {student["hobby"]}')

# Removing a key-value pair
del student["age"]
print(student)

# Remove and return an item using pop
grade = student.pop("grade")
print(f"Removed grade: {grade}")
print(student)

# Check if a key exists in the dictionary
if "name" in student:
    print("Name is in the dictionary")

if "address" not in student:
    print("Address is not in the dictionary")

# Getting keys and values
keys = student.keys()
values = student.values()

print(f"Keys: {list(keys)}")
print(f"Values: {list(values)}")

# Looping (interating) through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Getting an item
# Using get() with a default value
phone = student.get("phone", "Not available")
print(f"Phone: {phone}")

# Nested dictionaries
school = {
    "name": "Springfield Middle School",
    "students": {
        "Alice": {"grade": 7, "favorite_subject": "Science"},
        "Bob": {"grade": 8, "favorite_subject": "Math"}
    }
}

print(f"Bob's favorite subject: {school['students']['Bob']['favorite_subject']}")


# merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merging dictionaries (Python 3.5+)
merged = {**dict1, **dict2}
print(f"Merged dictionary: {merged}")

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared = {num: num**2 for num in numbers}
print(f"Squared numbers: {squared}")


### Sets
# A set is an unordered collection of unique items.

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Creating a set from a list
numbers = set([1, 2, 3, 2, 1])
print(f"Numbers set: {numbers}")  # Duplicate values are automatically removed

# Adding elements to a set
colors = {"red", "green", "blue"}
colors.add("yellow")
print(f"Colors after adding yellow: {colors}")

# Adding multiple elements
colors.update(["orange", "purple"])
print(f"Colors after update: {colors}")

# Removing elements from a set
animals = {"dog", "cat", "elephant", "tiger"}
animals.remove("elephant")
print(f"Animals after removing elephant: {animals}")

# Using discard (doesn't raise an error if the element is not found)
animals.discard("lion")
print(f"Animals after discarding lion: {animals}")

# Checking membership in a set
fruits = {"apple", "banana", "cherry"}
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'grape' in fruits?", "grape" in fruits)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print(f"Union: {union_set}")

# Intersection
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# Difference
difference_set = set1.difference(set2)
print(f"Difference (set1 - set2): {difference_set}")

# Finding unique elements in a list
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"Unique numbers: {unique_numbers}")

# Removing duplicates from a string
text = "mississippi"
unique_chars = set(text)
print(f"Unique characters in '{text}': {unique_chars}")

# Checking for subsets in a set
fruits = {"apple", "banana", "cherry"}
citrus = {"lemon", "orange"}
more_fruits = {"apple", "banana", "cherry", "date", "elderberry"}

print("Is citrus a subset of fruits?", citrus.issubset(fruits))
print("Is more_fruits a superset of fruits?", more_fruits.issuperset(fruits))




