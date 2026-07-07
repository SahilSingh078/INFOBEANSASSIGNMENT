salary = int(input("Enter Salary: "))
cs = int(input("enter credit score: "))
loan = int(input("Enter existing no. of Loans: "))

if salary >= 30000:
    
    if cs >= 750:
        print("Loan Status = Approved")
        
    else:
        if loan < 2:
            print("Loan Status = Conditional Approval")
        else:
            print("Loan Status = Rejected")

else:
    print("Loan Status = Rejected")