a = int(input("Enter The Distance : "))
b = input("Enter Class (AC/Sleeper) : ").lower()
if a <=100:
    if b=="sleeper":
       Fare = 100
    else:
       Fare = 200
elif 101<=a<=500:
    if b=="sleeper":
       Fare = 300
    else:
       Fare = 600
else:
    if b=="sleeper":
       Fare = 500
    else:
       Fare = 1000
print("Total Fare: ", Fare)
