"""
Multiple Inheritance

Create a class `Warehouse` and a class `RetailSystem` and derive a class `InventoryManagementSystem` from both of them.
"""


# Base class 1: Warehouse
class Warehouse:
    def __init__(self):
        """
        Initialize the warehouse with an inventory.
        """
        pass

    def add_stock(self, item, quantity):
        """
        Add stock to the warehouse.
        """
        pass

    def check_stock(self, item):
        """
        Check the stock of an item in the warehouse.
        """
        pass


# Base class 2: RetailSystem
class RetailSystem:
    def __init__(self):
        """
        Initialize the retail system with sales results.
        """
        pass

    def record_sale(self, item, quantity):
        """
        Record a sale in the retail system.
        """
        pass

    def get_sales_data(self, item):
        """
        Get sales results for an item.
        """
        pass


# Derived class: InventoryManagementSystem
class InventoryManagementSystem(Warehouse, RetailSystem):
    def __init__(self):
        """
        Initialize the inventory management system with inventory and sales results.
        """
        pass

    def fulfill_order(self, item, quantity):
        """
        Fulfill an order by updating the inventory and sales results.
        """
        pass


# Example usage
inventory_system = InventoryManagementSystem()

inventory_system.add_stock('Laptop', 50)
inventory_system.fulfill_order('Laptop', 10)
inventory_system.fulfill_order('Laptop', 35)
inventory_system.check_stock('Laptop')
inventory_system.fulfill_order('Laptop', 100)  # Should display an error message
inventory_system.get_sales_data('Laptop')
