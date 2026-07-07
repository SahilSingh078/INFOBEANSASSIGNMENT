'''
a =int(input("enter starting year: "))
b = int(input("Enter ending year: "))
count = 0
for i in range (a,b+1):
		
	if (i%400==0) or ( i%4 == 0 and i%100!=0) :  
		count+=1
		print( "Event Scheduled",i)		
	else:
		print(i, "Not scheduled ")
print("Total Leap year ", count)
print("Total Events scheduled ", count)
'''
a =int(input("enter starting year: "))
b = int(input("Enter ending year: "))
count =0
for i in range (a,b+1):
	
	for j in range(i,i+1):
		if i%400==0:
			count+=1
			print(i, "-> Event Scheduled")
		elif i%4 == 0:
			count+=1
			print(i, "-> Event Scheduled")
		elif i%100==0:
			print(i, "-> No event Scheduled")
		else: 
			print(i, "-> No event")
print("total leap year :", count)
print("Total Events scheduled", count)
	'''
	galat h
'''

		