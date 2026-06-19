a,b = map(int,input("Enter Cost price and Selling Price [with space]: ").split())
profit = b-a
profitpercentage = (profit/a)*100
print("NOTE: +VE =PROFIT , -VE= LOSS, +VE%= PROFIT% ")
print("Profit is: " , profit,"profit%: ", profitpercentage,sep="\n")
