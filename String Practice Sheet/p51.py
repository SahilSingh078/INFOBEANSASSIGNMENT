'''
51
Extract only digits. 
S = "a1b2c3" 
"123"
'''
a = input("Enter the string: ")
result= ""
for i in a:
    if "0"<=i<="9":
        result+=i
    else:
        pass
print(result)