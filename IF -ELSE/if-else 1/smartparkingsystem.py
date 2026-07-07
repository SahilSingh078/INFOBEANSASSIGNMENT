a = input("Enter vehicle type(bike/car/bus): ").lower()
b = int(input("Enter hours Parked: "))

if a == "bike":
    rate = 10
elif a  == "car":
    rate = 20
elif a == "bus":
    rate = 50
else:
    print("Invalid vehicle type")

total = rate * b

if b > 5:
    total += 100

print("Total Parking Fee: ₹", total)