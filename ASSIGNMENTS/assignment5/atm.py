a = int(input("Enter Your balance: "))
b = int(input("enter your withdrawal amount: "))
c = input("Enter Your Pin status(Correct/Incorrect: )").lower()
if a >=b:
    if b <=10000:
       if c =="correct":
          print("Transaction Succesfull ")
       else:
          print("Invalid Pin ")
    else:
       print("Limit Exceeded ")
else:
    print("Insufficient balance")