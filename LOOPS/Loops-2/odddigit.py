'''
a = int(input("enter Your Number: "))
count = 0
while a>0:
	d = a%10
	if d%2!=0:
		count = count+1
	a  = a//10
	
print("odd digit count : ",count)
'''
	
#for loop
a = int(input("enter Your Number: "))
count = 0
for i in range(1,a+1):
	d = a%10
	if d%2!=0:
		count = count+1
	a  = a//10

print("odd digit count : ",count)