age = int(input("enter your age : "))
b = input("Do Your have ID (yes/No): ").lower()
if age>=18:
    if b=="yes":
        print("Your are eligible")
    else:
        print("You are not eligible")

else:
    print("you are under age")