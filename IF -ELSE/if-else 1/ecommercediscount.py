a = int(input("Enter Your Total Purchase Amount: "))
if a >=5000:
	disc = a *0.20
	price = a - disc
elif 2000<=a<=5000:
	disc  = a * 0.10
	price = a -disc
	
else:
	disc = a * 0.05
	price = (a - disc)
print("Final Amount: ", price)