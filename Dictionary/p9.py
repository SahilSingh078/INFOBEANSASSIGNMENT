'''
9.
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================
Store product stock in a dictionary.
stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}
Write a program to:
* Display products having stock less than 30.
Sample Output:
Eraser
Marker
'''
n = int(input("Enter number of products: "))
article= []
stock = []
for i in range(n):
    article.append(input("Enter article name: "))
    stock.append(int(input("Enter stock amount: ")))
d= {}
for i in range(len(article)):
    d[article[i]]=stock[i]
print(d)
for k,v in d.items():
    if v<30:
        name = k
        print(name)