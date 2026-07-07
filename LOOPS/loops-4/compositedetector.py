a = int(input("Enter Your Number: "))
x= 0
for i in range(1,a+1):
	if a%i==0:
		x= x+1
		
else:
	if x !=2:
		print("Composite Number")
	else:
		print("Not Composite")
print("FACTOR COUNT: ", x)
for i in range(2, a):
    if a % i == 0:
        print("Smallest Factor =", i)
        break