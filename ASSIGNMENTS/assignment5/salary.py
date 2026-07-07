a = int(input("Enteer Your Salary: "))

if a >= 30000:
    print("Eligible for PF")
    
    if a >= 50000:
        print("Eligible for bonus")
    else:
        print("Not eligible for bonus")

else:
    print("Not eligible for anything")
    
