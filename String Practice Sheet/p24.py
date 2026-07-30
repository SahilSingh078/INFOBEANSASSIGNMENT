'''
24. Check if all characters are unique
'''
a = input("Enter the string: ")
x= 0
for i in a:
    if a.count(i)>1:
        x =1
        break
if x==0:
    print("true")
else:
    print("false")