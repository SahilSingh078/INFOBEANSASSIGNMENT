salary = int(input("Enter Salary: "))
credit = int(input("Enter Credit Score: "))
loans = int(input("Enter Existing Loans: "))

if salary >= 30000:
    if credit >= 750:
        if loans == 0:
            risk = "Low Risk"
        else:
            if loans <= 2:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
    
    else:
        if salary >= 50000:
            if credit >= 650:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
        

else:
    risk = "Not Eligible"

print("Risk Level =", risk)