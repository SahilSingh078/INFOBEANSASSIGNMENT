'''
Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.
Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''
amount = float(input("Enter Transaction Amount: "))
location = input("Enter Location (international/domestic): ").lower()
age = int(input("Enter Account Age (in years): "))

if amount >= 10000:
    if location == "international":
        otp = input("Is OTP Verified? (yes/no): ").lower()

        if otp == "yes":
            print("Transaction = Allowed")
        else:
            print("Transaction = Blocked")

    elif location == "domestic":
        if amount >= 50000:
            
            if age >= 2:
                print("Transaction = Allowed")
            else:
                print("Transaction = Flagged")
        else:
            print("Transaction = Allowed")

    else:
        print("Invalid Location")

else:
    unusual_activity = input("Is there Unusual Activity? (yes/no): ").lower()

    if unusual_activity == "yes":
        print("Transaction = Flagged")
    else:
        print("Transaction = Allowed")