# String manipulation

secret_word = "python"
guess = input("Guess a 6-letter word: ")

if len(guess) != 6:
    print("Your guess should be 6 letters long!")
else:
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            print(f"The letter '{guess[i]}' is in the correct position!")
        elif guess[i] in secret_word:
            print(f"The letter '{guess[i]}' is in the word, but in the wrong position.")
        else:
            print(f"The letter '{guess[i]}' is not in the word.")