class Pizza:
    """
    >>> pizza = Pizza("Margherita")
    >>> pizza.__str__()
    'Margherita'
    >>> str(pizza)
    'Margherita'
    >>> print(pizza)
    Margherita

    >>> pizza = Pizza("Margherita", 'cheese', 'tomato')
    >>> print(pizza)
    Margherita
    - cheese
    - tomato
    """

    def __init__(self, pizza_name, *toppings):
        self.pizza_name = pizza_name
        self.toppings = toppings

    # dunder method
    def __str__(self):
        display_str = f'{self.pizza_name}'
        for topping in self.toppings:
            display_str += f'\n- {topping}'
        return display_str
