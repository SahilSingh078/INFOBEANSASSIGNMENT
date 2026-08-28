'''
8.
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================
A library records issued books.
books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]
Write a program to:
* Count how many times each book was issued.
Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}
'''
a = input("Enter your issued books: ").split()
d = {}
for i in a:
    d[i]= d.get(i,0)+1
print(d)