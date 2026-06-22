#a = int(input("Enter Your total bill: "))
#b = int(input("Enter Number of Friends: "))
#c= a/b
#print("Each Should pay : " ,c)



a, b = map(int, input("Enter total bill and number of friends: ").split(","))

c = a / b

print("Each should pay:", c)