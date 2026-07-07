
n = int(input("Enter a number: "))

small = 9

while n> 0:
    d = n % 10
    if d < small:
        small = d
    n = n // 10

print("Smallest Digit =", small)

#for loops
'''
n = int(input("Enter a number: "))
len = len(str(n))
small = 9
for i in range (0,len):
	digit = n % 10
	if digit < small:
       		 small = digit
	i = n // 10
	n = n // 10
print("Smallest Digit =", small)
'''