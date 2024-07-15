# Input validation

def is_valid_guess(guess):
    if len(guess) != 3:
        return False
    return guess.isdigit()

while True:
    user_guess = input("Enter a 3-digit number: ")
    if is_valid_guess(user_guess):
        print(f"Valid guess: {user_guess}")
        break
    else:
        print("Invalid guess. Please enter exactly 3 digits.")
