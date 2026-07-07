a,b = map(int,input("Enter Your Both Number [with spaces]: ").split())
'''
while a<b:
	if a %5  == 0:
		if a%10 != 0:
			print(a, end=" ")
		
	a +=1
'''

for i in range (a , b+1):
	if i % 10 !=5:
		continue
	print(i, end=" ")
		