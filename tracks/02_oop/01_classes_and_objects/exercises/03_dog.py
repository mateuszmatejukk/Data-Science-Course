"""
Task: Create a class called `Dog` with a class attribute `species` set to "Labrador".
Print the names and species of both dogs.
"""


class Dog:
    """
    >>> dog1 = Dog(name="Max")
    >>> dog1.name = "Azor"
    >>> print(dog1.name, dog1.species)
    Azor Labrador
    >>> dog2 = Dog()
    >>> print(dog2.name, dog2.species)
    no_name Labrador
    """
    species = "Labrador"

    def __init__(self, name="no_name"):
        self.name = name
