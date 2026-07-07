a = int(input("Enter current Floor: "))
b = int(input("Enter destination floor: "))
if a<b:
	for i in range (a,b+1):
		print(i,end="")
		if i!=b:
			print(end="->")
elif a>b:
	for i in range(a,b-1,-1):
		print(i,end=" ")
		if i!=b:
			print(end="->")	
else:
	print("Already On the Same Floor")