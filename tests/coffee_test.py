import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Espresso")
        self.customer = Customer("Alice")

    def test_name_property(self):
        with self.assertRaises(ValueError):
            Coffee(123)  # Invalid type
        with self.assertRaises(ValueError):
            Coffee("A")  # Too short

    def test_orders(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(len(self.coffee.orders()), 1)

    def test_customers(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 7.0)
        self.assertEqual(self.coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()