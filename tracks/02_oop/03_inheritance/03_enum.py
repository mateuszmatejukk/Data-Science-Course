print("Example 0 - categories example")


class SIZE:
    """
    Enum representing different sizes

    >>> SIZE.S
    'Small'
    >>> SIZE.M
    'Medium'
    >>> SIZE.L
    'Large'
    """
    S = 'Small'
    M = 'Medium'
    L = 'Large'


# 'Small', 'Medium'
#
# if size == SIZE.S:
#     print_size *= 0.8
# #

print(SIZE.S)
sizes = SIZE()
size_l = sizes.L
print(size_l is SIZE.L)  # True
# print(size_l in SIZE) # ERROR
# print(size_l in sizes) # ERROR
print(type(size_l))  # <class 'str'>
print(repr(size_l))  # Large
# print(list(SIZE)) # ERROR
SIZE.XS = 'Extra Small'
print(SIZE.XS)  # Works but shouldn't

print('-' * 20, 'Example 1 - working with Enum', '-' * 20)
from enum import Enum


class SEASON(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    AUTUMN = 4


print(SEASON.AUTUMN)
# season = SEASON()
# print(season.FALL)
autumn = SEASON.AUTUMN
print(autumn is SEASON.AUTUMN)  # True
print(autumn in SEASON)  # True
print(type(autumn))  # <enum 'SEASON'>
print(repr(autumn))  # <SEASON.FALL: 4>
# ANSII vs UTF-8
print(list(SEASON))  # [<SEASON.WINTER: 1>, <SEASON.SPRING: 2>, <SEASON.SUMMER: 3>, <SEASON.FALL: 4>]
print(autumn.name)  # FALL
print(autumn.value)  # 4

# Dot notation
print(SEASON.WINTER)
# Call notation - not recommended
print(SEASON(1))
# subscript notation - not recommended
print(SEASON["WINTER"])

# SEASON.FALL = "Autumn"  # AttributeError: cannot reassign member 'FALL'

print("-" * 20 + "Example 2 - Enum in a class with logic" + '-' * 20)


class STATUS(Enum):
    """
    >>> STATUS.PENDING
    <STATUS.PENDING: 0>
    >>> STATUS.IN_PROGRESS
    <STATUS.IN_PROGRESS: 1>
    """
    PENDING, IN_PROGRESS, COMPLETED = range(3)


class Task:
    """
    Represents a task with a title and status.

    >>> task = Task("Write report")
    >>> str(task)
    'Write report | Status: PENDING'

    >>> task = Task("Example task", STATUS.IN_PROGRESS)
    >>> print(task.status)
    STATUS.IN_PROGRESS

    >>> task.update_status(STATUS.COMPLETED)
    >>> print(task.status)
    STATUS.COMPLETED

    >>> task.update_status("Completed")
    Traceback (most recent call last):
    ...
    ValueError: Invalid status
    """

    def __init__(self, title, status=STATUS.PENDING):
        if not isinstance(status, STATUS):
            raise ValueError("Invalid status")

        self.title = title
        self.status = status

    def update_status(self, new_status):
        if not isinstance(new_status, STATUS):
            raise ValueError("Invalid status")

        self.status = new_status

    def __str__(self):
        return f"{self.title} | Status: {self.status.name}"
