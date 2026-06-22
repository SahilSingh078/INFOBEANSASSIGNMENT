a = int(input("Enter your age: "))
b = input("enter your Show time(morning/evening) : ").lower()
c = input("Enter day type (weekday/weekend)").lower()
if a >=18:
    if b =="evening":
       if c =="weekend":
          print("price = 300")
       else:
          print("price = 250 ")
    else:
       print("price = 200 ")
else:
    print("not allowed")