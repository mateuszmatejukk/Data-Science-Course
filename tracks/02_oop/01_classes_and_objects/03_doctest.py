"""
Doctest demo

>>> c = 7
>>> 'a' * c
'aaaaaaa'

>>> print('a'*c)
aaaaaaa

>>> for i in range(3):
...     print('a'*i)
<BLANKLINE>
a
aa

>>> d = 5
>>> d
5

>>> d*5
25
"""

def add(a,b):
    """
    This function adds two numbers

    >>> 2+2
    4

    >>> add(2,2)
    4

    >>> add('Hello', 'Alice')
    Traceback (most recent call last):
    ...
    ValueError: Invalid type
    """
    if type(a) == type(b) == str:
        raise ValueError('Invalid type')
    return a+b

class Employee:
    """
    Part of documentation blablabla
    >>> john = Employee(emp_name="JOHN", emp_age=30.5)
    >>> print(john.name)
    John
    >>> print(john.__dict__)
    {'name': 'John', 'age': 30}
    """

    def __init__(self, emp_name, emp_age):
        """
        >>> john = Employee(emp_name="John", emp_age=30)
        >>> print(john.name)
        John
        """
        self.name = emp_name.title()
        self.age = int(emp_age)


