'''

a = int(input("Enter Your Number: "))
x= 0
for i in range(1,a+1):
	if a%i==0:
		x= x+1
	
else:
	if x !=2:
		print("Composite Number")
	else:
		print("Not Composite")
'''
import math
n = int(input("Enter Your Number: "))
if n <=1:
	print("NON COMPOSITE")
else:
	i =2
	while i<=int(math.sqrt(n)):
		if n%i ==0:
			print(" Composite")
			break
		i = i+1

	else:
		print("NON COmposite")