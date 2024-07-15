# Using dictionaries

# Exercise 3: Mad Lib template using a dictionary
template = "The {adjective} {animal} {verb} through the {place}."

word_types = {
    "adjective": "an adjective",
    "animal": "an animal",
    "verb": "a verb (past tense)",
    "place": "a place"
}

user_inputs = {}
for key, prompt in word_types.items():
    user_inputs[key] = input(f"Enter {prompt}: ")

completed_madlib = template.format(**user_inputs)
print("\nYour completed Mad Lib:")
print(completed_madlib)
