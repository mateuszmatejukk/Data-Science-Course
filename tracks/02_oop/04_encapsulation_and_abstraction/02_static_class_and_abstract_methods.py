from abc import abstractmethod, ABC


class Employee(ABC):
    # zmienny klasowe - class variables
    division = 'IT'
    __salary = 5000

    def __init__(self, name):
        self.name = name

    def display_badge(self):
        return f"{self.get_company_name()} | {self.name}"

    @staticmethod  # to jest metoda która moze byc wywalana na klasie, lub instancji i nie zalezy od instancji, zwracana wartosc (albo to co robi ta metoda) nie zalezy od atrybutow instancji.
    def get_company_name():
        return "XYZ"

    @abstractmethod  # sposób na wymuszanie implementacji u klas dziecziczących.
    # to nie jest metoda którą da się odzedziczyć, ją trzeba zawsze "nadpisać"
    def get_responsibilities(self):
        pass

    @classmethod  # dzięki temu moemy odnosić się do zmiennych klasowych które mamy zdefiniowane pod nagłówkiem klasy
    def get_salary(cls):
        return cls.__salary


class DataScientist(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def get_responsibilities(self):
        return "AI", "ML"


print(Employee.get_salary())
print(DataScientist.get_company_name())

ann = DataScientist("ann", 'python')
print(ann.get_company_name())

print(Employee.__dict__)
print(DataScientist.__dict__)
print(ann.__dict__)
print(dir(ann))
