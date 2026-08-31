'''
QUESTION 4: ONLINE SHOPPING ORDERS
==================================
An online shopping company stores customer orders using NamedTuple.
Fields:
order_id, customer_name, product_name, amount
Requirements:
1. Read N order records from the user and store them in a list of NamedTuples.
---
2. Display all order details.
---
3. Find and display the order having the highest amount.
---
4. Calculate and display total sales.
---
5. Count the number of orders whose amount is greater than ₹10,000.
---
Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''
from collections import namedtuple
Order = namedtuple("Order", ["order_id", "customer_name", "product_name", "amount"])
n = int(input("Enter number of orders: "))
orders = []
for i in range(n):
    print("Enter Details:")
    order_id = input("Enter Order ID: ")
    customer_name = input("Enter Customer Name: ")
    product_name = input("Enter Product Name: ")
    amount = int(input("Enter Amount: "))
    order = Order(order_id, customer_name, product_name, amount)
    orders.append(order)
print("\nAll Order Details:")
for x in orders:
    print(x.order_id, x.customer_name, x.product_name, x.amount)
highest = orders[0]
for x in orders:
    if x.amount > highest.amount:
        highest = x
print("\nHighest Value Order:")
print(highest.order_id, highest.customer_name, highest.product_name, highest.amount)
total = 0
for x in orders:
    total += x.amount
print("\nTotal Sales:")
print(total)
count = 0
for x in orders:
    if x.amount > 10000:
        count += 1
print("\nOrders Above ₹10,000:")
print(count)