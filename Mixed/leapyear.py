a = int(input("Enter Starting Year: "))
b = int(input("Enter Ending Year: "))
count =0
for i in range(a,b+1):
	if i%400 == 0:
		print(i," Event Scheduled ")
		count +=1
	elif i%100==0:
		print(i," No Event scheduled")
		
	elif i%4 == 0:
		print(i, "Event Scheduled")
		count+=1
	else:
   		print(i, "No Event scheduled")
print("Total Leap Years: ", count)
print("Total Events Scheduled", count)