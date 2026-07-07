'''
a = int(input("Enter Your Number: "))

i = 1
sum = 0

while i <= a:
    if a % i == 0:
        sum += i
        
    i += 1

print("sum of factors =", sum )
'''
#for loops

a = int(input("Enter Your Number: "))

sum = 0
for i in range(1,a+1):
	if a % i == 0:
        	sum += i



print("sum of factors =", sum )