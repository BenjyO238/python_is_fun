# Define a simple class called Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

# Create an instance of the Calculator class
calc = Calculator()

# Get user input
while True:
    operation = input("Enter the operation (add, subtract, multiply, divide) or 'quit' to exit: ").lower()
    if operation == 'quit':
        break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "add":
        print(f"The result is: {calc.add(num1, num2)}")
    elif operation == "subtract":
        print(f"The result is: {calc.subtract(num1, num2)}")
    elif operation == "multiply":
        print(f"The result is: {calc.multiply(num1, num2)}")
    elif operation == "divide":
        print(f"The result is: {calc.divide(num1, num2)}")
    else:
        print("Invalid operation")
