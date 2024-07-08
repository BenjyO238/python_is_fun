
# Remember the temperature conversion formula: (C * 9/5) + 32. Here's a function that does it.
# Temperature conversion formula: (F - 32) * 5/9 = C. Here's a function that does it.
def temperature_converter(temperature, unit):
    if unit.lower() == 'c':
        # Convert Celsius to Fahrenheit
        converted = (temperature * 9/5) + 32
        return f"{temperature}°C is equal to {converted:.2f}°F"
    elif unit.lower() == 'f':
        # Convert Fahrenheit to Celsius
        converted = (temperature - 32) * 5/9
        return f"{temperature}°F is equal to {converted:.2f}°C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

# To run this let's get input from the user:
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert and display the result
result = temperature_converter(temp, unit)
print(result)

# Optional: Add some example conversions
print("\nSome common temperature conversions:")
examples = [(0, 'C'), (32, 'F'), (100, 'C'), (98.6, 'F')]
for temp, unit in examples:
    print(temperature_converter(temp, unit))







# Now to show you what a "main" method is.
# def some_function():
#     print("This function can be imported and used in other modules.")
#
# if __name__ == "__main__":
#     print("This code only runs when example.py is executed directly.")
#     some_function()
