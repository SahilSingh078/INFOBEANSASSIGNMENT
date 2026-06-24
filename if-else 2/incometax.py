a  = int(input("Enter Your annual income : "))
if a <=250000:
	tax =0
elif a<=500000:
	moneytaxable = a -250000
	tax = moneytaxable *0.05
elif a<=1000000:
	moneytaxable = a -250000
	tax = moneytaxable * 0.20
else: 
	moneytaxable = a -250000
	tax  = moneytaxable * 0.30

print("Tax Payable: ", tax )