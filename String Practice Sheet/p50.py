'''
50
Remove all digits.
S = "a1b2c3" 
"abc"
'''
a = input("Enter the string: ")
result= ""
for i in a:
    if "0"<=i<="9":
        pass
    else:
        result+=i
print(result)