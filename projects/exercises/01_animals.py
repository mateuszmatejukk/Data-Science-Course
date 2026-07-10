"""
Create a class `Animal` with method `make_sound`. Add:
- `Dog` class that will make a sound 'Woof'
- `Cat` class that will make a sound 'Meow'

>>> dog = Dog()
>>> cat = Cat()
>>> dog.make_sound()
'Woof'
>>> cat.make_sound()
'Meow'
"""


class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement make_sound")


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
