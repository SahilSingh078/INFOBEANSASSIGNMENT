n=int(input("Enter Number: "))
x=len(str(n))
count=0
for i in range(x):
	rem=n%10
	if rem%2==0:
		count+=1
	n//=10
if count == x:
    print("All even number" )
else: 
    print("NOT all even")