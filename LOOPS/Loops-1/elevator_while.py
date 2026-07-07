a = int(input("Enter current Floor: "))
b = int(input("Enter destination floor: "))
if a<b:
	while (a<=b):
		print(a,end="")
		a+=1
		if a!=b+1:
			print(end="->")
elif a>b:
	while (a>=b):
		print(a,end=" ")
		a-=1
		if a!=b-1:
			print(end="->")	
else:
	print("Already On the Same Floor")