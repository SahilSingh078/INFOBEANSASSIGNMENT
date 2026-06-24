age = int(input("Enter Policy Age: "))
amnt = int(input("Enter Claim Amount: "))
accident = input("Enter Accident Type (minor/major): ").lower()

if age >= 2:
    if amnt <= 50000:
        if accident == "minor":
            status = "Approved"
        else:
            status = "Approved with Inspection"
    
    else:
        if amnt <= 200000:
            if accident == "major":
                status = "Approved with Investigation"
            else:
                status = "Rejected"
        else:
            status = "Rejected"

else:
    if accident == "minor":
        status = "Rejected"
    else:
        status = "Pending Review"

print("Claim Status =", status)