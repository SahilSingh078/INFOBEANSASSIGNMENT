'''
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''


a = int(input("Enter Your Number: "))
sum = 0
while a>0:
	digit = a%10
	sum = sum+ digit
	a=a//10
print("SUM IS : ", sum)
temp = sum
count = 0
for i in range (1 , sum +1):
	if temp%i==0:
		count +=1
'''	
else:
	if count ==2:
		print("PRIME NUMBER")
	else:
		print("NON PRIME  NUMBER")
'''		

if sum == temp:
	print("LUCKY NUMBER")
else:
	print("NON LUCKY NUMBER")