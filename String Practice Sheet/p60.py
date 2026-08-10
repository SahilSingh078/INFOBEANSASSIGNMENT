'''
60
Append two strings but remove duplicate adjacent characters. 
S1 = "miss", 
S2 = "issippi" 
"misisipi"
'''
a = input("Enter the first string: ")
b = input("enter the second string :")
c =a+b
result = ""
for i in range(len(c)):
    if c[i-1] != c[i]:
        result+=c[i]
print(result)