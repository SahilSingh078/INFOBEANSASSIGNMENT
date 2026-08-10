'''
59
Rotate characters by 3 positions to the right. 
S = "abcde" 
"cdeab"
'''
a = input("Enter the string: ")
b = a[-3:]
result = a[:-3]
print(b + result)