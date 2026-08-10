'''
58Rotate characters by 2 positions to the left. 
S = "abcde" 
"cdeab"
'''
a = input("Enter the string: ")
b = a[:2]
result = a[2:]
print(result + b)