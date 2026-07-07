

a = int(input("Enter Your Number: "))
len = len(str(a))
count = 1
while count>0:
	d = a//10**(len-1)
	print("First Digit: ", d)
	count = count-1

'''
#for loop

a = int(input("Enter Your Number: "))
len = len(str(a))
for i in range(1,len+1):
	r =a %10
	a = a//10
print(r)
'''