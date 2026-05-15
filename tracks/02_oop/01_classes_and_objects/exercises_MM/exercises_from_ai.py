'''1. Klasa Dog
Utwórz klasę z atrybutami: name i age.
Dodaj metodę bark(), która wypisze: "Hau, jestem Burek".
'''
class Dog:
    def __init__(self,dog_name,dog_age):
        self.name = dog_name
        self.age = dog_age

    def bark(self):
        print(f"Hau, jestem {self.name}")

burek = Dog(dog_name ='burek',dog_age=10)

burek.bark()

"""4. Klasa BankAccount
Ustaw początkowe saldo na 0.
Dodaj metody deposit(amount) i withdraw(amount).
Jeśli brakuje pieniędzy, metoda withdraw() ma zwrócić komunikat, że operacja się nie udała."""
class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f'Twoje saldo wynosi{self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Operacja się nie udała, za niski stan konta")
        else:
            self.balance - amount

"""2. Klasa Student
Dodaj atrybuty: name, index_number, subjects.
Napisz metodę show_info(), która zwróci pełne informacje o studencie."""
class Student:
    def __init__(self, name, index_number, subjects):
        self.name = name
        self.index_number = index_number
        self.subjects = subjects

    def show_info(self):
        return f"Jestem {self.name},moje id to {self.index_number} a moje subjects to {self.subjects}"

    def add_subject(self, subject):
        self.subjects.append(subject)

class Subject:
    def __init__(self, name, grades, mean):
        self.name= name
        self.grades = grades
        self.mean = mean

ania = Student(
    name='Ania',
    index_number=234515,
    subjects=[
        Subject(name='Biology', grades=[5, 2], mean=3.5),
        Subject(name='Math', grades=[4,2],mean =3)
    ]
)

subject = Subject(name='Art', grades=[], mean=None)
ania.add_subject(subject)
# print(ania.show_info())
print(ania)


# IDIOTOODPORNY KOD