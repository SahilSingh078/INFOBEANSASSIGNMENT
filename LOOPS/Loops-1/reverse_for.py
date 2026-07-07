a = int(input("Enter your Number: "))
rev = 0
for i in range (len(str(a))):
   rev = rev*10 + a%10
   a = a//10
print("Reverse Number : ", rev)