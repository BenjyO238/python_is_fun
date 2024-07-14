# While loops are different from for loops in that they execute a block of code
# as long as a certain condition is true.




# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment the value of i by 1

# Output:
# 1
# 2
# 3
# 4
# 5

# Counts from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1, 2, 3, 4, 5

# Continuously asks for input until the user types 'quit'. This is a very common pattern in games.
while True:
    user_input = input("Enter a command (type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break
    print(f"You entered: {user_input}")

# Output:
# Enter a command (type 'quit' to exit): hi
# You entered: hi
# Enter a command (type 'quit' to exit): hello
# You entered: hello
# Enter a command (type 'quit' to exit): quit
# Exiting the program.

# While with multiple conditions. Generates random numbers until getting one between 1 and 10.
import random

number = 0
attempts = 0
while number < 1 or number > 10:
    number = random.randint(0, 20)
    attempts += 1
    print(f"Generated: {number}")

print(f"Found a number between 1 and 10 in {attempts} attempts.")

# Calculates the sum of numbers until the user enters 0
sum = 0
while True:
    num = int(input("Enter a number (0 to finish): "))
    if num == 0:
        break
    sum += num

print(f"The sum of the numbers is: {sum}")


# Searches for a number in a list
numbers = [1, 3, 5, 7, 9]
search = 5
index = 0

while index < len(numbers):
    if numbers[index] == search:
        print(f"Found {search} at index {index}")
        break
    index += 1
else:
    print(f"{search} not found in the list")

# Output:
# Found 5 at index 2

