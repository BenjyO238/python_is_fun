# Define the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model} engine is now running."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model} engine is now off."

# Function to create a car based on user input
def create_car():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = int(input("Enter the year of the car: "))
    return Car(make, model, year)

# Function to interact with a car
def interact_with_car(car):
    while True:
        action = input("Do you want to 'start' or 'stop' the engine? (or 'quit' to exit): ").lower()
        if action == 'quit':
            break
        elif action == 'start':
            print(car.start_engine())
        elif action == 'stop':
            print(car.stop_engine())
        else:
            print("Invalid action")

# Main function to run the program
def main():
    print("Let's create your first car!")
    car1 = create_car()
    interact_with_car(car1)

    print("\nLet's create your second car!")
    car2 = create_car()
    interact_with_car(car2)

# Run the main function
if __name__ == "__main__":
    main()
