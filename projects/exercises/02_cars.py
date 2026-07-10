"""
Write a Python class Vehicle with attributes make, model, year, fuel_capacity, and fuel_level and methods:

- `ride` - print the distance the vehicle is driving.
- `__repr__` - return a string representation of the vehicle.
"""


class Vehicle:
    def __init__(self, make, model, year, fuel_capacity):
        """
        Initialize a Vehicle object with make, model, year, and fuel capacity.

        Parameters:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        year (int): The year the vehicle was manufactured.
        fuel_capacity (float): The fuel capacity of the vehicle in liters.
        """
        pass

    def __repr__(self):
        """
        Return a string representation of the Vehicle object.

        Returns:
        str: A string representation of the vehicle in the format 'Vehicle(year, make, model)'.
        """
        pass

    def ride(self, distance):
        """
        Print the distance the vehicle is driving.

        Parameters:
        distance (float): The distance the vehicle is driving in kilometers.
        """
        pass


# Example usage:
v1 = Vehicle("Toyota", "Corolla", 2020, 50)
print(v1)
v1.ride(100)

"""
Create a class ElectricCar that inherits from Vehicle with additional attributes battery_capacity, battery_level and
electricity_consumption, and methods:

- `charge` - print a message indicating the car is charging.
- `ride` - reduce the battery level based on the distance and print a message about the ride.
- `check_battery_status` - print a message about the current battery level and advise to charge if low.
- `__repr__` - return a string representation of the electric car.
"""


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity, electricity_consumption):
        """
        Initialize an ElectricCar object with make, model, year, battery capacity, and electricity consumption.

        Parameters:
        make (str): The make of the electric car.
        model (str): The model of the electric car.
        year (int): The year the electric car was manufactured.
        battery_capacity (float): The battery capacity of the electric car in kWh.
        electricity_consumption (float): The electricity consumption of the electric car in kWh per km.
        """
        super().__init__(make, model, year, 0)  # Electric cars have no fuel tank
        pass

    def __repr__(self):
        """
        Return a string representation of the ElectricCar object.

        Returns:
        str: A string representation of the electric car in the format 'ElectricCar(year, make, model, battery_capacity kWh)'.
        """
        pass

    def charge(self):
        """
        Print a message indicating the car is charging and set the battery level to full.
        """
        pass

    def ride(self, distance):
        """
        Reduce the battery level based on the distance and print a message about the ride.

        Parameters:
        distance (float): The distance the electric car is driving in kilometers.
        """
        pass

    def check_battery_status(self):
        """
        Print a message about the current battery level and advise to charge if low.
        """
        pass


# Example usage:
ec1 = ElectricCar("Tesla", "Model 3", 2022, 75, 0.2)
print(ec1)
ec1.ride(100)
ec1.check_battery_status()
ec1.charge()
ec1.check_battery_status()
