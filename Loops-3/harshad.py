a =int(input("Enter Your Number : "))
sum = 0
temp = a
while 	a>0:
	n = a%10
	sum = sum +n	
	a = a//10
	
if temp % sum == 0:
	print("HARSHAD NUMBER")
else:
	print("Not  a Harshad Number ")