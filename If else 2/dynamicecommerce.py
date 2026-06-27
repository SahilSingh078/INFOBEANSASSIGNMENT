demand = int(input("Enter Demand: "))
stock = int(input("Enter Stock: "))
usertype = input("Enter User Type (premium/normal): ").lower()
festival = input("Is it Festival? (yes/no): ").lower()

if demand >= 80:
    if stock < 50:
        if usertype == "premium":
            if festival == "yes":
                print("Discount = 20%")
            else:
                print("Discount = 10%")
        else:
            print("Discount = 0%")
    else:
        print("Discount = 5%")

elif 40 <= demand <= 79:
    if festival == "yes":
        print("Discount = 10%")
    else:
        print("Discount = 0%")

else:   # demand < 40
    if stock > 200:
        print("Discount = 15%")
    else:
        print("Discount = 0%")