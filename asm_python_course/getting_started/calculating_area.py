def get_area_of_shape(shape, **kwargs):
    if shape == "circle":
        return 3.14 * kwargs["radius"] ** 2
    if shape == "rectangle":
        return kwargs["length"] * kwargs["width"]


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_shape_parameters(shape):
    parameters = {}
    if shape == "circle":
        parameters["radius"] = get_float_input("Enter the radius of the circle: ")
    elif shape == "rectangle":
        parameters["length"] = get_float_input("Enter the length of the rectangle: ")
        parameters["width"] = get_float_input("Enter the width of the rectangle: ")
    return parameters


while True:
    print("\nCalculate area of a shape")
    shape = input("Enter the shape (circle/rectangle) or 'quit' to exit: ").lower()

    if shape == 'quit':
        print("Thank you for using the shape area calculator!")
        break

    if shape in ["circle", "rectangle"]:
        parameters = get_shape_parameters(shape)
        area = get_area_of_shape(shape, **parameters)
        print(f"The area of the {shape} is: {area:.2f}")
    else:
        print("Invalid shape. Please enter 'circle' or 'rectangle'.")