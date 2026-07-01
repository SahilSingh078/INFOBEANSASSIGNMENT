'''
a,b =map(int,input("Enter Your Number [with Spaces]: ").split())
count  = 0 
while a<=b:
	if a %5 == 0:
		count+=1
	
	a+=1
print( "total count: ", count)
'''
#for loop

a,b =map(int,input("Enter Your Number [with Spaces]: ").split())
count  = 0 
for i in range(a,b+1):
	if a%5 ==0:
		count+=1
	
print("total count: ", count)