'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase
Input: Enter employee name: ajay singh thakur
Output: Employee Short ID: AST
'''

a = input("Enter Employee Name: ")
for i in range(len(a)):
    if i == 0 or a[i-1]== " ":
        if "a"<=a[i]<="z":
            print(chr(ord(a[i])-32), end="")
        elif"A"<=a[i]<="Z":
            print(chr(ord(a[i])), end="")
        else:
            print(" No digits Allowed")
            break
    
