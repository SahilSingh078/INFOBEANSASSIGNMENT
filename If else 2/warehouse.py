'''
Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier


'''

stock = int(input("Enter Your Stock: "))
priority = input("Enter Your Priority: ").lower()
distance = int(input("Enter Your Distance: "))

if stock >100:
	if priority== "high":
		if distance <=200:
			print("Dispatch Status = Dispatch Immediately")
		else:
			print("Dispatch Status = Dispatch via Fast Courier")	
	else:
		if stock >=300:
			print("Dispatch Status : Bulk Dispatch ")
		else:
			print("Normal Dispatch")
		
elif  stock >=50:
	if priority =="high":
		print("DISPATCH STATUS : Partially Dispatch")
		 
	else:
		print("DISPATCH STATUS : HOLD ")	
else: 
	print("OUT OF STOCK!!!!!!!")