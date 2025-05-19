import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_property(self):
        with self.assertRaises(ValueError):
            Customer(123)  # Invalid type
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_orders(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(len(self.customer.orders()), 1)

    def test_coffees(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(self.customer.coffees(), [self.coffee])

    def test_most_aficionado(self):
        bob = Customer("Bob")
        carol = Customer("Carol")
        self.coffee.create_order(bob, 5.0)
        self.coffee.create_order(carol, 7.0)
        self.coffee.create_order(carol, 8.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), carol)

if __name__ == "__main__":
    unittest.main()