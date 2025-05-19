from coffee import Coffee  # Absolute import for Coffee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order  # Import for type checking only

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name  # uses setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order  # Local import to avoid circular dependency
        # Validate inputs
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a number between 1.0 and 10.0")

        # Create order and link it
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        all_orders = coffee.orders()
        if not all_orders:
            return None
        from collections import defaultdict
        spending = defaultdict(float)
        for order in all_orders:
            spending[order.customer] += order.price
        return max(spending, key=lambda c: spending[c])