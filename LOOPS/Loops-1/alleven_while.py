n = int(input("Enter Your Number : "))
x = len(str(n))
count =0
while n>0:
	rem=n%10
	if rem%2==0:
		count+=1
	n//=10
if x==count:
	print("All Even")
else:
	print("Not All Even")