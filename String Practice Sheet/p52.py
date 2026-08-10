'''
52Remove all special characters. 
S = "a!@b#c" 
"abc"
'''
a = input("Enter the string: ")
result= ""
for i in a:
    if i.isalnum () :
        result+=i
    else:
        pass
print(result)