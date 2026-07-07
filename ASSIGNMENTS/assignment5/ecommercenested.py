a = int(input("Enter Cart Value: "))
b = input("Enter User Type (premium/regular): ").lower()

if a  >= 5000:
    
    if b == "premium":
        discount = a * 0.20
    else:
        discount = a * 0.10

else:
    
    if a >= 2000:
        discount = cart * 0.05
    else:
        discount = 0

finalamount = a - discount
print("Final Amount =", (finalamount))