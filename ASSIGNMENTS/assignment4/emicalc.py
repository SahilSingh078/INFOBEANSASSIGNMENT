a,b = map(int,input("Enter Mobile Price: And Down Payment Price [with space]: ").split())

remprice = (a-b)

c,d = map(int,input("Enter Your Interest rate: and NUmber of months ").split())

interestamount = (c/100)*remprice

totalamnt = interestamount + remprice

monthlyEmi = totalamnt/d

#print(f"Remaning amount: {remprice} Total with Interest = {totalamnt} Your MOnthly Emi : {monthlyEmi} " )
#print("Remaining amount: ", remprice , "Total with Interest: ", totalamnt, "Your Monthly Emi: ", monthlyEmi)
print("Remaining Amount: {} Total With Interest: {} Your Monthly EMI: {}".format(remprice, totalamnt, monthlyEmi))

