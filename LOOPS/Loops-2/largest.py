n = int(input("Enter a number: "))

large = 0

while n > 0:
    digit = n % 10
    if digit > large:
        large = digit
    n = n // 10

print("Largest Digit =", large)


#for loop
'''

n = int(input("Enter a number: "))

large = 0
for i in range (0,n+1):
	digit = n % 10
	if digit > large:
       		 large = digit
	i = n // 10
print("Largest Digit =", large)
'''