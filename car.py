class Car:
    def __init__(self, make, model, year=2020):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic")

# Accessing attributes and methods
print(car1.info())  # Output: This car is a 2022 Toyota Camry.
print(car2.info())  # Output: This car is a 2020 Honda Civic.
