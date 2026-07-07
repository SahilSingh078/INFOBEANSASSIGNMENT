a = int(input("Enter Your Number : "))
b = int(input("Enter the Digit:"))
count=0
while a>0:
   x = a%10
   a= a//10
   if x == b:
      count+=1
     
 
print(count)