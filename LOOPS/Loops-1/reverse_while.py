a = int(input("Enter your Number: "))
rev = 0
while a>0 :
   rev = rev*10 + a%10
   a = a//10
print("Reverse Number : ", rev)