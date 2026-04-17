"""
Task: Create a class called `Laptop` with the following attributes:
1. model
2. hdd
3. ssd
4. total_storage (sum of hdd and ssd)
"""


class Laptop:
    """
    >>> laptop = Laptop(model="Dell", hdd=256, ssd=128)
    >>> print(laptop.model)
    Dell
    >>> print(laptop.hdd)
    256
    >>> print(laptop.ssd)
    128
    >>> print(laptop.total_storage)
    384
    """

    def __init__(self, model, hdd, ssd):
        self.model = model
        self.hdd = hdd
        self.ssd = ssd
        self.total_storage = hdd + ssd
