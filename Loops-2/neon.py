
a = int(input("Enter Your Number "))
sum = 0
temp = a
square = a*a
len = len(str(square))
while square>0:
	b = square%10
	sum = sum + b
	square //= 10 
	len+=1
print("sum: ", sum)
if temp == sum:
	print("its a neon number ")
else:
	print("not a neon number")


'''
a = int(input("Enter Your Number "))
sum = 0
temp = a
square = a*a
len = len(str(square))
print("square is: ",square)
for i in range(1,len+1):
	b = square%10
	sum = sum + b
	square //= 10 
	
print("sum: ", sum)
if temp == sum:
	print("its a neon number ")
else:
	print("not a neon number")
'''