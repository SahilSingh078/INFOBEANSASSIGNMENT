'''
2. Multi Stage Prime Lock System
A smart locker opens only if final derived number is prime.
Write a program to:
- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not
Input:
234
Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''

import math
a = int(input("Enter Your Number: "))
temp = a
sum =0
count = 0
l = len(str(a))
for i in range(l):
	digit = a%10
	sum = sum + digit
	a = a//10
print("SUM = ",sum)
prod =1
for i in range(l):
	digit2 = temp%10
	prod = prod *digit2
	temp = temp//10
print("PRODUCt = ", prod)

diff = (prod - sum)
print("DIFFERENCE= ", diff)

l2= len(str(diff))
print("DIGITS = ", l2)

final = (diff+l2)
print("FINAL RESULT: ", final)

for i in range (1, int(math.sqrt(final))):
	if final%i !=0:
		count+=1
else:
	if count == 2:
		print("PRIME NUMBER")
	else:
		print("NON PRIME NUMBER")
