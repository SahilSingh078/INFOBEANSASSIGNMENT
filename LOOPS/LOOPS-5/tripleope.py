'''
1. Triple Operation Prime Verification System
A cybersecurity company generates a security score from entered access code.
Write a program to:
- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime
Input:
4215
Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime

'''

import math
a = int(input("Enter Your Number: "))
temp = a
temp2 = a
sum =0
count = 0
l = len(str(a))
for i in range(l):
	digit = a%10
	sum = sum + digit
	a = a//10
print("SUM = ",sum)
rev = 0
for i in range(l):
	digit2 = temp%10
	rev = rev*10 + temp%10
	temp =temp//10
print("REVERSE= ", rev)

diff = abs(temp2-rev)
print("DIFFERENCE= ", diff)

sum2 = sum + diff
print("SUM OF DIGIT AND DIFFERENCE: ", sum2)

'''
if sum2 <=1:
	print("NON PRIME")
else:
	i =2
	while i<=int(math.sqrt(sum2)):
		if sum2%i ==0:
			print("Non Prime")
			break
		i = i+1

	else:
		print("Prime")
'''

for i in range(1, int(math.sqrt(sum2))):
	if sum2%i!=0:
		count+=1
else:
	if count==2:
		print("Prime Number")
	else:
		print("Non prime")