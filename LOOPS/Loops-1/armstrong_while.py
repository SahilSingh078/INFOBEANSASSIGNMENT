a = int(input("Enter Your Number: "))
temp = a
sum = 0
count = len(str(a))

while a>0:
   digits = a%10
   sum += digits ** count
   a = a//10
if sum == temp:
   print("Armstrong Number ")
else: 
   print("Not armstrong Number ")
   