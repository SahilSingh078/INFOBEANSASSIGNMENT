p,r,t = map(int,input("Enter Your Principle, Rate and Time [with space]: ").split())
amount =( p * (1 + r/100)**t)
print("Amount After Interest : ",amount)