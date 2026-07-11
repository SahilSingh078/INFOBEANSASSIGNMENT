'''
QUE- 1 

*****

a = int(input("enter number of stars : "))
for i in range(1, (a+1)):
	print("*",end = " ")
'''

'''
QUE -2

*
*
*
*
*

a = int(input("enter number of stars : "))
for i in range(1, (a+1)):
	print("*")
'''
'''
QUE -3

*
 *
  *
   *
    *

a = int(input("Enter the Number of stars: "))
i = 1
while i <=a:
	j = 1
	while j<i:
		print(" ",end="")
		j+=1
	k = 1
	while k<=i:
		if k==i:
			print("*",end="")
		k+=1
	print()
	i+=1
'''

'''
QUE -4

*****
*****
*****
*****
*****
'''
'''
a = int(input("enter number of stars : "))

for i in range(1, (a+1)):
	print("*"*a)
'''
'''
i =1
while i<=a:
	j = 1
	while j <=a:
		print("*",end="")
		j+=1
	print()
	i+=1
'''
'''
QUE -5

12345
12345
12345
12345
12345
'''
'''
a = int(input("enter number : "))
i =1
while i<=a:
	j = 1
	while j <=a:
		print(j,end="")
		j+=1
	print()
	i+=1
'''

'''
QUE -6

11111
22222
33333
44444
55555
'''
'''
a = int(input("enter number of stars : "))
i =1
while i<=a:
	j = 1
	while j <=a:
		print(i,end="")
		j+=1
	print()
	i+=1

'''
'''
QUE -7

1
00
111
0000
11111
'''
'''
a = int(input("Enter the Number: "))
i =1
while i<=a:
	j = 1
	while j<=i:
		if i%2==0:
			print("0", end="")
		else:
			print("1", end="")
		j+=1
	print()
	i+=1
'''
'''
QUE -8 

*
**
***
****
*****
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		print("*", end ="")
		j+=1
	print()
	i+=1
'''

'''
QUE - 9

1
12
123
1234
12345
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		print(j, end ="")
		j+=1
	print()
	i+=1
'''

'''
QUE -10

1
22
333
4444
55555
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		print(i, end ="")
		j+=1
	print()
	i+=1
'''
'''
QUE -11
A
AB
ABC
ABCD
ABCDE
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j = 1
	while j<=i:
		print(chr(64+j), end ="")
		j+=1
	print()
	i+=1

'''
'''
QUE -12

a
ab
abc
abcd
abcde

'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j = 1
	while j<=i:
		print(chr(96+j), end ="")
		j+=1
	print()
	i+=1
'''
'''
QUE -13
1
01
101
0101
10101
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j = 1
	while j<=i:
		if i%2==0:
			if j%2==0:
				print("1", end ="")
			else:
				print("0", end ="")
		else:
			if j%2==0:
				print("0", end ="")
			else:
				print("1", end ="")
		j+=1
	print()
	i+=1
'''

'''
QUE -14
1
23
456
78910
'''
'''
a = int(input("Enter The Number: "))
i = 1
no=1
while i<=a:
	j =1
	while j <=i:
		print(no,end="")
		no= no+1
		j+=1
	
	print()
	i +=1
'''
'''
QUE-15
A
BB
CCC
DDDD
EEEEE
'''
'''
a =int(input("Enter The Number: "))
i = 1
while i <=a:
	j = 1
	while j <=i:
		print(chr(i+64), end="")
		j+=1
	print()
	i+=1
	
'''