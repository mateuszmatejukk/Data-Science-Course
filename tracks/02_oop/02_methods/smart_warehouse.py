# done: use __getitem__, __setitem__ and __delitem__ to solve that exercise,
#  no LLM

# class SmartWarehouse:
    """
    A warehouse that enforces stock limits and automatically removes items when stock reaches zero.

    >>> warehouse = SmartWarehouse(max_stock=100)
    >>> warehouse['laptops'] = 50   # same as warehouse.__setitem__("laptops",50)
    >>> warehouse['laptops']  # same as warehouse.__getitem__("laptops")
    50
    >>> warehouse['laptops'] += 40   # same as warehouse.__setitem__("laptops", (warehouse.__getitem__("laptops") + 40))
    >>> warehouse['laptops']
    90
    >>> 'laptops' in warehouse
    True
    >>> warehouse['laptops'] -= 90  # Remove all stock - item should be automatically removed
    >>> 'laptops' in warehouse  # same as warehouse.__contains__("laptops")
    False
    >>> warehouse['phones'] += 10   # Cannot add stock to non-existent item
    Traceback (most recent call last):
        ...
    KeyError: 'phones not found in the warehouse'
    >>> warehouse['phones'] = 110   # Cannot exceed max stock limit
    Traceback (most recent call last):
        ...
    ValueError: Cannot exceed max stock limit of 100 for phones
    >>> warehouse['phones'] = 10
    >>> warehouse['phones']
    10
    >>> del warehouse['phones']  # Remove item manually
    >>> warehouse['phones'] += 10
    Traceback (most recent call last):
        ...
    KeyError: 'phones not found in the warehouse'
    >>> del warehouse['phones']  # Cannot remove non-existent item
    Traceback (most recent call last):
        ...
    KeyError: 'phones not found in the warehouse'
    """
    ...


class SmartWarehouse:
    """
    A warehouse that enforces stock limits and automatically removes items when stock reaches zero.
    """

    def __init__(self, max_stock):
        self.max_stock = max_stock
        self.items = {}

    def __getitem__(self, item):
        if item not in self.items:
            raise KeyError(f"{item} not found in the warehouse")
        return self.items[item]

    def __setitem__(self, item, amount):
        if amount > self.max_stock:
            raise ValueError(
                f"Cannot exceed max stock limit of {self.max_stock} for {item}"
            )

        if amount == 0:
            if item in self.items:
                del self.items[item]
        else:
            self.items[item] = amount

    def __delitem__(self, item):
        if item not in self.items:
            raise KeyError(f"{item} not found in the warehouse")
        del self.items[item]

    def __contains__(self, item):
        return item in self.items


warehouse = SmartWarehouse(max_stock=100)

warehouse["laptops"] = 50
print(warehouse["laptops"])

warehouse["laptops"] += 40
print(warehouse["laptops"])

print("laptops" in warehouse)

warehouse["laptops"] -= 90
print("laptops" in warehouse)

warehouse["phones"] = 10
print(warehouse["phones"])

del warehouse["phones"]
print("phones" in warehouse)
