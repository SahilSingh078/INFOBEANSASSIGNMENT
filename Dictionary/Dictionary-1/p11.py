'''
11.
=========================================
PRODUCT SALES ANALYSIS
======================
sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
Write a program to:
* Count sales of each product.
* Display products in sorted order.
Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''
a = input("Enter your issued books[using space]: ").split()
d = {}
for i in a:
    d[i]= d.get(i,0)+1
print(d)
for k,v in sorted(d.items()):
    print(k,":", v)