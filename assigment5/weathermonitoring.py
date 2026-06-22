a = int(input("Enter temperature: "))
b = int(input("Enter humidity: "))

if a >=30:
    print("Hot day")
else:
    print("Moderate day")

if b >= 70:
    print("High Humidity Alert")
else:
    print("Normal Humidity")