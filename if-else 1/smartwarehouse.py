stock = int(input("Enter Stock: "))
priority = input("Enter Priority (high/low): ").lower()
distance = int(input("Enter Distance: "))

if stock >= 100:
    if priority == "high":
        if distance <= 200:
            status = "Dispatch Immediately"
        else:
            status = "Dispatch via Fast Courier"
    
    else:
        if stock >= 300:
            status = "Bulk Dispatch"
        else:
            status = "Normal Dispatch"

else:
    if stock >= 50:
        if priority == "high":
            status = "Partially Dispatch"
        else:
            status = "Hold"
    else:
        status = "Out of Stock"

print("Dispatch Status =", status)