# Simple Calculator

def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides two numbers."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def mod(x, y):
    """This function divides two numbers."""
    if y == 0:
        return "Error! Division by zero."
    return x % y


def main():
    print("Welcome to the Simple Calculator!")
    print("Enter your calculation in the form: number operation number")
    print("For example: 2 + 3 or 5 * 6")
    print("Available operations: +, -, *, /, %")

    while True:
        # Take input from the user
        calculation = input("Enter calculation: ").strip()

        # Split the input into parts
        parts = calculation.split()
        if len(parts) != 3:
            print("Invalid format. Please enter in the form: number operation number")
            continue

        num1, operation, num2 = parts

        # Convert numbers to float
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid numbers. Please enter valid numbers.")
            continue

        # Perform the operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '%':
            result = mod(num1, num2)
        else:
            print("Invalid operation. Please use +, -, *, / or %.")
            continue

        # Print the result
        print(f"The result is: {result}")

        # Ask if the user wants to do another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if not next_calculation.lower().startswith('y'):
            break

    print("Thank you for using the Simple Calculator!")

if __name__ == "__main__":
    main()
