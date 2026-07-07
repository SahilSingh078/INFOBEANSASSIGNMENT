n = int(input("Enter The Number: "))
sq = n*n
rev = 0
rev2 = 0
while n>0:
	d = n%10
	rev = rev*10 + d
	n = n//10
sq2 = rev *rev
while sq>0:
	c = sq%10
	rev2 = rev2*10 + c
	sq = sq//10
if rev2 ==sq2:
	print("adam number")
else:
	print("No adam number")