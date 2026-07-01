'''
a = int(input("Enter Your Number: "))

i = 1
count = 0

while i <= a:
    if a % i == 0:
        count += 1
        
    i += 1

print("Total factors =", count)
'''
#for loop

a = int(input("Enter Your Number: "))
count =0
for i in range(1,a+1):
	if a % i == 0:
        	count += 1
print("Total factors =", count)