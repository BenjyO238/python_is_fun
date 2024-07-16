# Functions
# Exercise 4: Mad Lib function
def create_madlib(adj, noun, verb):
    template = "The {adjective} {noun} {verb} over the rainbow."
    return template.format(adjective=adj, noun=noun, verb=verb)

def get_input(prompt):
    return input(f"Enter {prompt}: ")

print("Let's create a Mad Lib!")
user_adj = get_input("an adjective")
user_noun = get_input("a noun")
user_verb = get_input("a verb")

result = create_madlib(user_adj, user_noun, user_verb)
print("\nYour Mad Lib:")
print(result)