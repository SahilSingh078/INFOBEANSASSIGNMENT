a  = int(input("Enter Your Account balance: "))
if a<1000:
	print("Withdrawal not allowed ")
elif 5000>=a>=1000:
	print("Maximum withdrawal Limit : ₹1000")
else:
	print("Maximum withdrawal Limit: ₹5000")
