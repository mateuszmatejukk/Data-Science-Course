class Duck:
    def __init__(self):
        print("quack")
        self.has_bill = True

    def print_name(self):
        return "Duck"


class Beaver:
    def __init__(self):
        print("pip")
        self.has_tail = True

    def print_name(self):
        return "Beaver"


class Platypus(Duck, Beaver):
    def __init__(self):
        # super().__init__()  # super odnosi się jedynie do pierwszej klasy w MRO
        Duck.__init__(self)
        Beaver.__init__(self)

    def print_name(self):
        return "pepe"


pepe = Platypus()
print(pepe.__dict__)
print(pepe.print_name())

# print(Platypus.mro()) # [Platypus, Duck, Beaver, object] MRO - Method Resolution Order

"""
We think it is
   Parent
   /    \\
Left    Right
   \\    /
   Child

The MRO is:
Child -> Left -> Right -> Parent

https://python-history.blogspot.com/2010/06/method-resolution-order.html
Method Resolution Order - Guido van Rossum
"""
