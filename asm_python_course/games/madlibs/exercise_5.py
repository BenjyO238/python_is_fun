# Error handling
# Exercise 5: Mad Lib with error handling
def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print("Let's create a numbered Mad Lib!")
number = get_number_input("Enter a number: ")
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")

try:
    result = f"The {adj} {noun} counted to {number}."
    print("\nYour Mad Lib:")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")