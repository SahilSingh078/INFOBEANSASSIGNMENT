a = int(input("Enter Your Experience : "))
b = int(input("Enter Your salary : "))
if a >=10 :
	bonus = b *0.20
	
elif 5<a<10:
	bonus  = b * 0.10
	
elif 2<=a<=5:
	bonus = b * 0.05
	
else:
	bonus = 0
	
print("Bonus Amount: ", int(bonus))