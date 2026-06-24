sub = input("Enter Subscription (premium/basic): ").lower()
progress = int(input("Enter Progress: "))
score = int(input("Enter Test Score: "))

if sub == "premium":
    if progress >= 80:
        if score >= 70:
            status = "Unlock Certificate"
        else:
            status = "Retry Test"
    else:
        status = "Complete Course"

else:
    if sub == "basic":
        if progress >= 50:
            status = "Limited Access"
        else:
            status = "Content Locked"
    else:
        status = "Access Denied"

print("Access Status =", status)