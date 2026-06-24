a = float(input("Enter Daily Data Usage[IN GB]: "))
if a<1:
	print("Recommended Plan: Basic Plan")
elif 1<=a<=3:
	print("Recommended Plan: Standard plan")
else:
	print("Recommended plan: premium Plan")