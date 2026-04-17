"""
Task: Create a class `Animal` with a class attribute `kingdom` set to "Animalia".
"""


class Animal:
    """
    Class to represent an animal
    >>> cat = Animal("Whiskers")
    >>> dog = Animal("Rover")
    >>> print(cat.kingdom)
    Animalia
    >>> print(cat.__dict__)
    {'name': 'Whiskers'}
    >>> print(dog.__dict__)
    {'name': 'Rover'}
    """

    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name
