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

'''
QUE -16
a
bc
def
ghij
klmno
'''
'''
a = int(input("Enter the Numbeer: "))
i =1
no = 1
while i<=a:
	j =1
	while j <=i:
		print(chr(no+96),end="")
		no+=1
		j+=1
	print()
	i+=1
'''



'''
QUE -17
*
##
***
####
*****
'''
'''
a =int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i%2==0:
			print("#", end="")
		else:
			print("*", end="")
		j+=1
	print()
	i+=1
'''


'''
QUE -18
1
10
101
1010
10101
'''
'''
a = int(input("Enter The Number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		if j%2==0:
			print("0",end ="")
		else:
			print("1",end="")
		j+=1
	print()
	i+=1
'''

'''
QUE-19
*
* *
*  *
*   *
* * * * *
'''
'''
a =int(input("Enter The Number : "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print("*", end="")
		else:
			print(" ",end = "")
		j+=1
	print()
	i+=1
'''

'''
QUE 20
1
12
1 3
1  4
12345
'''
'''
a= int(input("Enter the number= "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i==a or j==1 or i==j:
			print(j,end="")
		else:
			print(" ", end="")
		j+=1
	print()
	i+=1 
'''
'''
QUE -21
1
22
3 3
4  4
55555
'''
'''
a = int(input("Enter Your Number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print(i,end="")
		else:
			print(" ", end="")
		j+=1
	print()
	i+=1
'''



'''
QUE -22
A
AB
A C
A  D
ABCDE
'''
'''
a = int(input("Enter Your Number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print(chr(64+j),end="")
		else:
			print(" ", end="")
		j+=1
	print()
	i+=1

'''

'''
QUE -23
a
bc
d f
g  j
klmno
'''
'''
a = int(input("Enter Your Number: "))
i =1
n =1
while i<=a:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print(chr(96+n),end="")
		else:
			print(" ", end="")
		n+=1
		j+=1
	print()
	i+=1
'''

'''
QUE -24
*
**
*@*
*@@*
* * * * *
'''
'''
a = int(input("Enter Your Number: "))
i =1
while i<=a:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print("*",end="")
		else:
			print("@", end="")
		j+=1
	print()
	i+=1
'''



'''
QUE -42
54321
5432
543
54
5



a = int(input("Enter Your Number: "))
i =1
while i<=a:
	j =5
	while j>=i:
		print(j,end="")
		j-=1
	print()
	i+=1
	
'''
'''
Que 25
5
54
543
5432
54321
'''
'''
a = int(input("Enter Your Number: "))
i =a
while i>=1:
	j = a
	while j>=i:
		print(j,end="")
		j-=1
	print()
	i-=1
'''

'''
Que 26
*
*#
*#*
*#*#
*#*#*

'''
'''
a = int(input("Enter The Number: "))
i  = a
while i>=1:
	j=a
	while j>=i:
			if j%2==0:
				print("#", end="")
			else:
				print("*", end="")
			j-=1
	print()
	i-=1
'''
'''
QUE- 27

1
10
1 1
1  0
10101
'''
'''
a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or i==a:
			if j%2==0:
				print("0",end=" ")
			else:
				print("1",end=" ")
		elif j==1:
			print("1",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1
'''

'''QUE 28
1
123
12345
1234567
123456789
'''
'''
a = int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=2*i-1:
		print(j, end="")
		j+=1
	print()
	i+=1
			
'''

'''
QUE 29
1
222
33333
4444444
555555555
'''
'''
a = int(input("Enter the number: "))
i =1
while i<=a:
	j =1
	while j<=2*i-1:
		print(i, end="")
		j+=1
	print()
	i+=1
'''

'''
que -30
*****
****
***
**
*
'''
'''

a =int(input("Enter the number: "))
i =1
while i<=a:
	j =a
	while j>=i:
		print("*", end="")
		j-=1
	print()
	i+=1
'''

'''
QUE -31
12345
1234
123
12
1
'''
'''
a =int(input("Enter the number: "))
i =a
while i>=1:
	j =1
	while j<=i:
		print(j, end="")
		j+=1
	print()
	i-=1
	'''

'''
QUE - 32
55555
4444
333
22
1
'''
'''
a =int(input("Enter the number: "))
i =5
while i<=1:
	j =1
	while j>=i:
		print(i, end="")
		j+=1
	print()
	i-=1
'''

'''
QUE 33
ABCDE
ABCD
ABC
AB
A
'''
'''
a =int(input("Enter the number: "))
i =a
while i>=1:
	j =1
	while j<=i:
		print(chr(64+j), end="")
		j+=1
	print()
	i-=1
'''

'''
QUE 34
EEEEE
DDDD
CCC
BB
A

'''
'''
a =int(input("Enter the number: "))
i =a
while i>=1:
	j =1
	while j<=i:
		print(chr(64+i), end="")
		j+=1
	print()
	i-=1
    
'''

'''
QUE 35
*****
*  *
* *
**
*

'''
'''
a =int(input("Enter The Number : "))
i =a
while i>=1:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print("*", end="")
		else:
			print(" ",end = "")
		j+=1
	print()
	i-=1
'''
'''
QUE 36 
ABCDE
A  D
A C
AB
A

'''
'''
a =int(input("Enter The Number : "))
i =a
while i>=1:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print(chr(64+j), end="")
		else:
			print(" ",end = "")
		j+=1
	print()
	i-=1
    '''

'''
QUE 37
*****
####
***
##
*

'''
'''
a =int(input("Enter the Number: "))
i =a
while i>=1:
	j=1
	while j<=i:
		if i%2==0:
			print("#", end="")
		else:
			print("*", end="")
		j+=1
	print()
	i-=1
'''
'''
QUE 38
55555
4  4
3 3
22
1

'''
'''
a =int(input("Enter The Number : "))
i =a
while i>=1:
	j =1
	while j<=i:
		if i==j or j==1 or i==a:
			print(i, end="")
		else:
			print(" ",end = "")
		j+=1
	print()
	i-=1
    '''
'''
QUE 39
123456
54321
1234
321
12
1

'''
n = int(input("ENter the number: "))
# for i in range(n,0,-1):
#     if i%2!=0:
#         for j in range(i,0,-1):
#             print(j,end="")
#     else:
#         for n in range(1,i+1):
#             print(n,end="")
#     print()

'''
i =n
while i>=1:
    if i%2!=0:
        j=i
        while j>=1:
                print(j, end ="")
                j-=1
    else:
           j =1
           while j<=i:
                  print(j, end = "")
                  j+=1
    print()
    i-=1        
    '''