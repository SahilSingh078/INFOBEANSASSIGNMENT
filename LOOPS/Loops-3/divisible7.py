a,b = map(int,input("Enter Your Both Number [with spaces]: ").split())
count = 0
while a<=b:
	if a %7 == 0:
		count = count +1
	a = a+1
print(" Count is: ", count)