a = input("Enter Your membership Status(yes/no) : ").lower()
b = int(input("Enter books issued : " ))
if a == "yes":
    print("Entry Allowed")
    if b<3:
      print("Can issue more books ")
    else:
      print("Not eligible for issuing books ")
else:
    print("ENTRY DENIED")