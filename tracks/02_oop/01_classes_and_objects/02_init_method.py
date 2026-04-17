class Employee:
    """
    Class documentation
    """
    company = "Google"  # class attribute
    def __init__(self, emp_name, emp_age):
        print('inside __init__ method')
        self.name = emp_name
        self.age = emp_age

john = Employee(emp_name='john', emp_age=25)  # runs __init__ method
print(john.__dict__)
print(Employee.__dict__)
print(john.name)
print(john.__class__.__name__)
print(Employee.__doc__)
print(dir(john))


# w3schools.com


