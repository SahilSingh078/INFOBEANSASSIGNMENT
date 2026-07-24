'''
6.
Product Code Verification System
An e-commerce company wants to verify whether two product codes are rearranged versions of each other.
Conditions:
- Ignore spaces
- Ignore case sensitivity
Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room
Output:
Both Product Codes are Matching
'''
s1=input("Enter the string: ")
s2=input("Enter the second String: ")
a=""
b=""
for i in s1:
    if i!=" ":
        a=a+i.lower()
for i in s2:
    if i!=" ":
        b=b+i.lower()

if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("Both Product Codes are Matching")
    else:
        print("Not Matching")
else:
    print("Not Matching")