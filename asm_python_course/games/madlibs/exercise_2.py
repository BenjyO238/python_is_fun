# Lists and random selection
# Exercise 2: Random word selector
import random

adjectives = ["funny", "silly", "purple", "fluffy", "noisy"]
nouns = ["cat", "banana", "computer", "hat", "bicycle"]
verbs = ["jumped", "danced", "sang", "flew", "exploded"]

print("Let's create a random funny sentence!")
random_adj = random.choice(adjectives)
random_noun = random.choice(nouns)
random_verb = random.choice(verbs)

sentence = f"The {random_adj} {random_noun} {random_verb} loudly."
print(sentence)