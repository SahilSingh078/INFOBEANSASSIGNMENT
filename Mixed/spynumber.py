a = int(input("ENTER YOUR NUMBER: "))
sum = 0
prod = 1
while a> 0:
	d = a%10
	sum = sum + d
	prod = prod * d
	a = a//10
if sum == prod:
	print("Spy Number")
else:
	print("Not a spy number")