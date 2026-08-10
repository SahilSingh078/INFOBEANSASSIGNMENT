'''
57
Merge two strings alternatively (char by char). 
S1 = "ABC", 
S2 = "def" 
"AdBeCf"
'''
a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a)==len(b):
    for i in range(len(a)):
        print(a[i]+b[i], end= "")
else: 
    n = min(len(a), len(b))
    for i in range(n):
        print(a[i]+b[i], end= "")
    if len(a)>len(b):
        print(a[n:], end = "")
    else:
        print(b[n:],  end ="")
    