from typing import TYPE_CHECKING
from coffee import Coffee

if TYPE_CHECKING:
    from customer import Customer  # Import for type checking only

class Order:
    def __init__(self, customer: 'Customer', coffee: Coffee, price: float):
        # Validate inputs
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a number between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price