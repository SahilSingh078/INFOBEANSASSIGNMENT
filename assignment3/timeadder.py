a,b,c=map(float,input("Enter Hours, Minutes and Seconds separated by(,):  ").split(","))
total = (a*3600) +(b*60)+ c 
print(f"Your Total Seconds: {total}")