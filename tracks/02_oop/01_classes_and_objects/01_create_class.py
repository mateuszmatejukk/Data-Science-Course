class Employee:
    name = 'John'
    age = 25

john = Employee()
print(type(john))
print(isinstance(john, Employee))
print(isinstance(john, int))
print(isinstance(john, object))

print(john is Employee)
# print(type(Employee))

mark = Employee()
print(john)
print(john.name, john.age)
mark.name = 'Mark'
mark.age = 30
print(mark.name, mark.age)

print(john.__dict__)  # atrybuty instancji - brak
print(mark.__dict__)  # atrybuty instancji - są

print(dir(john))
print(dir(mark))


Employee.name = "Bob"
print(john.name)  # Bob
print(mark.name)  # Mark