'''
12.
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
Write a program to:
* Count orders of each food item.
* Find the most ordered item.
Sample Output:
Pizza : 3
Burger : 2
Pasta : 2
Most Ordered : Pizza
'''
a = input("Enter your issued books[using space]: ").split()
d = {}
for i in a:
    d[i]= d.get(i,0)+1
print(d)
high = 0
for k,v in (d.items()):
    if v>high:
        high = v
        name = k 
print("Most Ordered: ",name)
    