import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_init(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_customer_property(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(ValueError):
            Order(123, self.coffee, 5.0)  # Invalid customer type

    def test_coffee_property(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(ValueError):
            Order(self.customer, 123, 5.0)  # Invalid coffee type

    def test_price_property(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Price out of range
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Price out of range

if __name__ == "__main__":
    unittest.main()