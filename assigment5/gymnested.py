a = int(input("Enter your age "))
b = float(input("enter your weight "))
c = input("Enter Your goal (Weight loss/ muscle gain)").lower()
if a >=18:
    if b >=80:
       if c =="weightloss":
          print("plan =  cardio Plan ")
       else:
          print("plan = strength plan ")
    else:
       print("GENERAL fitness Plan assigned ")
else:
    print("not allowed")