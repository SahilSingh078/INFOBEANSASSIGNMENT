a,b,c=map(float,input("Enter Distance(in km), Mileage(in KM/L) and Petrol Price:  separated by(,):  ").split(","))
cost = (c/b)*a
print(f"Your Cost is: {cost}")