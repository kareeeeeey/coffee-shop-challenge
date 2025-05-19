import sys
import os

# Ensure the script runs in the correct package context
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from customer import Customer
from coffee import Coffee
from order import Order

def debug():
    print("☕ Starting Debug Session...\n")

    try:
        # Create customers
        alice = Customer("Alice")
        bob = Customer("Bob")
        print(f"✅ Created customers: {alice.name}, {bob.name}")

        # Create coffees
        espresso = Coffee("Espresso")
        latte = Coffee("Latte")
        print(f"✅ Created coffees: {espresso.name}, {latte.name}")

        # Place orders
        order1 = alice.create_order(espresso, 5.0)   # ✅ Correct usage
        order2 = alice.create_order(latte, 4.5)      # ✅ Correct usage
        order3 = bob.create_order(espresso, 5.5)     # ✅ Correct usage
        print("\n✅ Orders created successfully.")

        # Test Order properties
        print("\n🔍 Inspecting Order Properties:")
        print(f"Order1 price: ${order1.price}")
        print(f"Order1 customer: {order1.customer.name}")
        print(f"Order1 coffee: {order1.coffee.name}")

        # Test Customer methods
        print("\n👥 Customer Methods:")
        print(f"{alice.name}'s orders: {[o.coffee.name for o in alice.orders()]}")
        print(f"{alice.name}'s coffees: {[c.name for c in alice.coffees()]}")

        # Test Coffee methods
        print("\n☕ Coffee Methods:")
        print(f"{espresso.name} orders count: {espresso.num_orders()}")
        print(f"{espresso.name} average price: ${espresso.average_price():.2f}")
        print(f"{espresso.name} customers: {[c.name for c in espresso.customers()]}")

        # Bonus: Most Aficionado
        print("\n🏆 Most Aficionado (Espresso):")
        top_customer = Customer.most_aficionado(espresso)
        if top_customer:
            total_spent = sum(order.price for order in top_customer.orders() if order.coffee == espresso)
            print(f"{top_customer.name} spent a total of ${total_spent:.2f} on Espresso.")
        else:
            print("No orders yet.")

    except Exception as e:
        print("❌ Error during debug session:", str(e))

if __name__ == "__main__":
    debug()