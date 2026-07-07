a = int(input("Enter your Number: "))
temp = a	
rev = 0
while a>0 :
   rev = rev*10 + a%10
   a = a//10
if rev == temp:
   print("Plaindrome: yes")
else: 
   print(" Not Plaindrome")
