'''
Number Stability Analyzer
A science lab studies whether digits are in increasing order.
Write a program using for-else loop:
- If every next digit is greater than previous print Stable Number
- Else Unstable Number
Input:
12359
Output:
Stable Number
'''
'''

a = int(input("Enter Your Number: "))
l = len(str(a))
for i in range (l):
	n1=a%10
	a = a//10
	n2 = a %10
	if n1<n2:
		print("NON STABLE NUMBER")
		break
else:
	print("Stable Number")
'''
a =int(input("enter your number: "))
while a>0:
	n1=a%10
	a = a//10
	n2 = a %10
	if n1<n2:
		print("NON STABLE NUMBER")
		break
else:
	print("Stable Number")