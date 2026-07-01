a =int(input("Enter the number"))
temp = a
square = a*a
while  temp >0:
	if square%10 != temp %10:
		print("Not an automorphic Number")
		break
	temp = temp//10
	square = square//10
else:
	print("Automorphic number")