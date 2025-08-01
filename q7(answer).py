class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Task 2
# Create an instance of the Car class and call describe_car

my_car = Car("Tesla", "Model3", 2024)
my_car.describe_car()  # Expected output: "2024 Tesla Model3"
