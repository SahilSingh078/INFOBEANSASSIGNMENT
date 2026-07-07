a = int(input("Enter Your 1st Number: "))
b = int(input("Enter Your 2nd Number: "))

for i in range(a, b + 1):
	sq = i*i
	sum =0
	while sq>0:
		d  =sq%10
		sum += d
		sq //= 10
	if sum == i:
		print(i)