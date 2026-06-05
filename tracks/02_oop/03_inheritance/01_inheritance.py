class Employee:
    """
    >>> john = Employee("John", 30, "IT")
    >>> print(john)
    John | Department: IT
    """

    def __init__(self, name, age, dep):
        self.name = name
        self.age = age
        self.dep = dep

    def __str__(self):
        return f"{self.name} | Department: {self.dep}"


# without inheritance
class DataScientistWO:
    """
    >>> ds = DataScientistWO("Bob", 25, ["Python", "R"])
    >>> print(ds)
    Bob | Department: R&D | Programming languages: Python, R
    """

    def __init__(self, name, age, lan):
        self.name = name
        self.age = age
        self.dep = "R&D"
        self.lan = lan

    def __str__(self):
        return f"{self.name} | Department: {self.dep} | Programming languages: {', '.join(self.lan)}"


# with inheritance
class DataScientist(Employee):
    """
    >>> ds = DataScientist("Bob", 25, ["Python", "R"])
    >>> print(ds)
    Bob | Department: R&D | Programming languages: Python, R
    """

    def __init__(self, name, age, lan):
        super().__init__(name, age, dep='R&D')
        self.lan = lan

    def __str__(self):
        return f"{super().__str__()} | Programming languages: {', '.join(self.lan)}"


ds = DataScientist("Bob", 25, ["Python", "R"])

print(isinstance(ds, object))  # True
print(isinstance(ds, Employee))  # TRUE
print(isinstance(ds, DataScientist))  # True

print(issubclass(DataScientist, Employee))  # True
print(issubclass(Employee, DataScientist))  # False
