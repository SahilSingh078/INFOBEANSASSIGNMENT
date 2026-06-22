a,b,c = map(int,input("Enter Your distance, mileage and Petrol Price [with space]: ").split())
petrol = a/b
totalcost = petrol*c
print("Petrol used: {}Litres  Total cost {}".format(petrol,totalcost))