class Employee:
    """
    >>> john = Employee(emp_name="John", emp_age=25, salary=5_000)
    >>> john.is_employed
    True
    >>> john.give_raise(raise_value=1_000)
    >>> john.salary
    6000
    >>> john.happy_birthday()
    >>> john.age
    26
    >>> john.change_name(new_name="Mark")
    >>> john.name
    'Mark'
    >>> john.you_fired()
    >>> john.is_employed
    False
    """
    def __init__(self, emp_name, emp_age, salary):
        self.name = emp_name
        self.age = emp_age
        self.salary = salary
        self.is_employed = True

    def give_raise(self, raise_value):
        self.salary += raise_value

    def happy_birthday(self):
        self.age += 1

    def change_name(self, new_name):
        """
        Change the value of name attribute to new_name
        """
        self.name = new_name

    def you_fired(self):
        self.is_employed = False