'''
85
Convert string into a char array without built-in functions. 
S = "test" ['t', 'e', 's', 't']
'''
s = input("Enter the string: ")
res = []
for i in s:
    res = res+[i]
print(res)