# List operations

def create_clue_list(guess, secret):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Correct")
        elif guess[i] in secret:
            clues.append("Close")
        else:
            clues.append("Wrong")
    return clues

secret = "cat"
guess = input("Guess a 3-letter word: ")
clue_list = create_clue_list(guess, secret)

print("Here are your clues:")
for clue in clue_list:
    print(clue)