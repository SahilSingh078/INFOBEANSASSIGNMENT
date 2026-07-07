n = int(input("enter Your Number: " ))
temp = n
sum =0 
while n>0:
	a = n%10
	fact =1
	for i in range(1,a+1):
		fact = fact *i
	
	sum = sum + fact
	n =n//10	
	
if sum == temp:
	print("Strong Number")
else:
	print("Not Strong Number")