'''

Bike Service Kilometer Checker
A bike needs service every 3000 km.
Write a program to:
- Read travelled kilometers
- Print every service checkpoint till entered km
Input:
10000
Output:
3000 6000 9000

'''
'''
a = int(input("Enterr Your travelled Distance(IN Kms): "))
for i in range(3000,a+1, 3000):
	print(i, end = " ")
'''

n =int(input("Enter Your Number: "))
i =1
while n>=1:
	p= 3000*i
	if p>n:
		break
	print(p,end=" ")
	i = i+1