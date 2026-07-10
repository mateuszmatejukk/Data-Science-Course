"""
Create an enum class `TicketType` that represents different ticket types:
`STANDARD`, `PREMIUM`, and `VIP`.
Each ticket type has a discount percentage associated with it.
Create a class `Ticket` that represents a ticket with a type and price.

>>> TicketType.STANDARD.get_discount()
0
>>> TicketType.PREMIUM.get_discount()
10
>>> TicketType.VIP.get_discount()
20
>>> ticket = Ticket(1, TicketType.VIP, 200.0)
>>> print(ticket)
Ticket ID: 1, Type: VIP, Price: $160.00
>>> ticket.get_final_price()
160.0
"""

from enum import Enum


class TicketType(Enum):
    """
    Enum representing different ticket types.
    """

    STANDARD = "Standard"
    PREMIUM = "Premium"
    VIP = "VIP"

    def get_discount(self):
        """
        Returns the discount percentage for the ticket type.
        """
        discounts = {
            TicketType.STANDARD: 0, TicketType.PREMIUM: 10, TicketType.VIP: 20}
        return discounts[self]


class Ticket:
    """
    Represents a ticket with a type and price.
    """

    def __init__(self, ticket_id, ticket_type: TicketType, price):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price

    def get_final_price(self):
        """
        Returns the final price after applying discount.
        """
        discount = self.ticket_type.get_discount()
        return self.price * (1 - discount / 100)

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Type: {self.ticket_type.value}, Price: ${self.get_final_price():.2f}"
