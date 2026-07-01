'''1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number


a = int(input("Enter Your Number: "))
x= 0
for i in range(1,a+1):
	if a%i==0:
		x= x+1
	
else:
	if x ==2:
		print("Prime Number")
	else:
		print("non prime")
'''
import math
n = int(input("Enter Your Number: "))
if n <=1:
	print("NON PRIME")
else:
	i =2
	while i<=int(math.sqrt(n)):
		if n%i ==0:
			print("Non Prime")
			break
		i = i+1

	else:
		print("Prime")