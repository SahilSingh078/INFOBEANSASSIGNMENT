a =int(input("Enter your number: "))
sum = 0
for i in range(1,(a//2)+1):
	if a%i == 0:
		sum += i
print("sum = ",sum)
if sum >a:
	print("abundant number")
	
else:
	print("No abundant numbers")