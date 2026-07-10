"""
Create an enum class `OrderStatus` that represents different order statuses:
`PENDING`, `PROCESSING`, `SHIPPED`, `DELIVERED`, and `CANCELLED`.

Implement a method in `OrderStatus` to check if a status is final (DELIVERED or CANCELLED).
Create an `Order` class that:
- Stores an **incremental** order ID as a class variable.
- Stores the order status.
- Allows updating the status unless it is final.

>>> OrderStatus.PENDING.is_final_status()
False
>>> OrderStatus.DELIVERED.is_final_status()
True

>>> order1 = Order(OrderStatus.PENDING)
>>> order2 = Order(OrderStatus.SHIPPED)
>>> order3 = Order(OrderStatus.CANCELLED)
>>> order1.order_id, order2.order_id, order3.order_id
(1, 2, 3)

>>> str(order1)
'Order 1 - Status: Pending'
>>> order1.update_status(OrderStatus.SHIPPED)
>>> order1.status
<OrderStatus.SHIPPED: 'Shipped'>
>>> order1.update_status(OrderStatus.DELIVERED)
>>> order1.update_status(OrderStatus.CANCELLED)
Cannot update order 1, it's already DELIVERED.
"""

from enum import Enum


class OrderStatus(Enum):
    """
    Enum representing order statuses.
    """

    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

    def is_final_status(self):
        """
        Checks if the order status is final.
        """
        return self in {OrderStatus.DELIVERED, OrderStatus.CANCELLED}


class Order:
    """
    Represents an order with a status and an incremental order ID.
    """

    _order_counter = 0  # Class variable to track order count

    def __init__(self, status: OrderStatus):
        Order._order_counter += 1
        self.order_id = Order._order_counter
        self.status = status

    def update_status(self, new_status: OrderStatus):
        """
        Updates the status of the order if it's not in a final state.
        """
        if self.status.is_final_status():
            print(f"Cannot update order {self.order_id}, it's already {self.status.name}.")
        else:
            self.status = new_status

    def __str__(self):
        return f"Order {self.order_id} - Status: {self.status.value}"
