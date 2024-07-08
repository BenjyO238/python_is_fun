# More symbols
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
# strings:
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


# bytes and strings: this is how computers store data.
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
