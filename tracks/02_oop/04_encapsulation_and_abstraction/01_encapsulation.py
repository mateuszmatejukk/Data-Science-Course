class Employee:
    def __init__(self, name):
        self.name = name
        self._is_part_time = False
        self.__salary = 5000
        self.__currency = "$"

    def get_salary(self):
        return f"{self.__salary}{self.__currency}"

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("salary cannot be lower than 0")
        self.__salary = new_salary


john = Employee(name='john')
print(john._is_part_time)
john._is_part_time = True
print(john._is_part_time)

# didn't work
# print(john.__salary)
# john.__salary = 8000
# print(john.__salary)

print(john.get_salary())
john.set_salary(-8000)
print(john.get_salary())
