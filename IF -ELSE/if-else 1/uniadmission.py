marks = int(input("Enter Your Marks: "))
entrance = int(input("Enter Your Entrance Score: "))
category = input("Enter Category (general/other): ").lower()

if marks >= 70:
    if entrance >= 80:
        if category == "general":
            status = "Admitted"
        else:
            status = "Admitted with Scholarship"
    else:
        if marks >= 85:
            status = "Admitted under Management Quota"
        else:
            status = "Rejected"

else:
    if category != "general" and marks >= 60:
        if entrance >= 70:
            status = "Waitlisted"		
        else:
            status = "Rejected"
    else:
        status = "Rejected"

print("Admission Status =", status)