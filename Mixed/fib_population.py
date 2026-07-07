n =int(input("Enter Number Of months: "))
a = 0
b =1
total = 0
count =0
print("Population Growth ")
for i in range(n):
	print( a, end =" ")
	total = total + a
	if a>5:
		count += 1
	c = a+b
	a =b
	b =c
	
print("\n Total Population: ", total)
print("Months with Population > 5 =", count)