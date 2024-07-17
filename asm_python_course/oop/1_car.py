# Define a simple class called Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model} engine is now running."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model} engine is now off."

# Create instances (objects) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Interact with the objects
print(car1.start_engine())
print(car1.stop_engine())

print(car2.start_engine())
print(car2.stop_engine())
