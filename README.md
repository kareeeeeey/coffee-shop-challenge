# ☕ Coffee Orders – Python OOP Mini Project

Hey there! 👋 This is a simple but fun little Python project where we model how coffee orders work using **Object-Oriented Programming (OOP)**.

You’ll find classes for **customers**, **coffees**, and **orders**, and everything ties together just like a real-world coffee shop. The goal? To get comfy with writing classes, using relationships between objects, and handling data responsibly (with validation and all that good stuff).

---

## 🧠 What This Project Teaches

This challenge is great if you’re learning Python and want to understand how real systems are built with OOP. Here's what you'll get better at:

- Writing Python classes with initializers (`__init__`)
- Using **getters and setters** to control and validate data
- Creating relationships between objects (like who ordered what)
- Doing calculations across objects (like averages or totals)
- Using class methods for logic that works across all instances

---

## 📘 The Backstory

Think of this like a small app behind the counter at your favorite coffee shop. A customer comes in, orders a drink, and we record:

- Who the customer is
- What coffee they ordered
- How much it cost

We’re going to model that using three classes: `Customer`, `Coffee`, and `Order`.

---

## 👩‍💻 How It Works (Classes & Behavior)

### 🧍‍♀️ Customer

Represents someone who can order coffee.

#### What’s stored:
- `name` – must be a string and between **1 and 15 characters**

#### What you can do:
- `orders()` → get all the orders this customer has made
- `coffees()` → get a list of different coffees they've ordered
- `create_order(coffee, price)` → create a new order for a specific coffee

---

### ☕ Coffee

Represents a coffee item you can order.

#### What’s stored:
- `name` – must be a string, **at least 3 characters**
- You can’t change the coffee’s name after it's created (it’s **immutable**)

#### What you can do:
- `orders()` → all orders of this coffee
- `customers()` → list of all customers who’ve ordered it
- `num_orders()` → total number of times this coffee was ordered
- `average_price()` → average price of all orders for this coffee

---

### 🧾 Order

This is the actual purchase. Every order ties a customer to a coffee and includes a price.

#### What’s stored:
- `customer` – must be a `Customer` instance
- `coffee` – must be a `Coffee` instance
- `price` – must be a float between **1.0 and 10.0**

Once created, you can’t change these – they’re **locked in**.

---

