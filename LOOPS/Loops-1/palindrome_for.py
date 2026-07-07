a = int(input("Enter your Number: "))
temp = a
rev = 0
for i in range (len(str(a))):
   rev = rev*10 + a%10
   a = a//10
if rev == temp:
   print("Palindrome: yes ")
else:
   print("not Palindrome")
