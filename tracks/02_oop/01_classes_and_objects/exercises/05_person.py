"""
Task: Create a class called `Person` with a class attribute `species` set to "Homo Sapiens".
Explain why the outputs are different.
"""


class Person:
    """
    >>> alice = Person()
    >>> bob = Person()
    >>> alice.species = "Cyborg"
    >>> print(alice.species)
    Cyborg
    >>> print(bob.species)
    Homo Sapiens
    """
    species = "Homo Sapiens"
