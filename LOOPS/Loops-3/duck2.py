a = int(input("Enter Your number: "))
count = 0
while a>0:
	b = a%10
	if b == 0:
		count +=1
	a =a//10
if count>=1:
	print("duck number")
else:
	print("not a duck number")