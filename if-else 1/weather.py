a = int(input("Enter the Temperature: "))
if a <0:
	print("Weather Condition: Freezing")
elif 0<=a<=20:
	print("Weather Condition: Cold")
elif 21<=a<=35:
	print("Weather Condition: warm")
else:
	print("Weather Condition: Hot")

