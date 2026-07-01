a = int(input("Enter Your Number: "))
prod = 1
i = 1
while i<=a:
	if i %2 !=0:
		prod = prod *i
	i = i+1
print("Product: ",  prod)