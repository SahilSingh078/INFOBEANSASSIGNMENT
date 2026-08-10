'''
68
Count the sum of digits present in a string. 
S = "a1b2c3" 
6 (1+2+3)
'''
a = input("Enter the string: ")
sum =0
for i in a:
    if i.isdigit():
        sum+= int(i)
print("Sum: ", sum)