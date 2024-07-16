print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number. Can you guess if it's high, low, or in the middle?")

secret_number = 5

guess = input("Enter a number between 1 and 10: ")
guess = int(guess)  # Convert the input string to an integer

if guess == secret_number:
    print("You guessed it exactly right!")
elif guess < secret_number:
    print("Your guess is too low!")
elif guess > secret_number:
    print("Your guess is too high!")

print("\nNow, let's check if your number is odd or even.")
if guess % 2 == 0:
    print(f"{guess} is an even number!")
else:
    print(f"{guess} is an odd number!")

print("\nLet's compare your guess to some other numbers.")
if guess != 3:
    print(f"Your guess ({guess}) is not equal to 3.")
if guess >= 7:
    print(f"Your guess ({guess}) is greater than or equal to 7.")
if guess <= 4:
    print(f"Your guess ({guess}) is less than or equal to 4.")

print("\nThanks for playing!")