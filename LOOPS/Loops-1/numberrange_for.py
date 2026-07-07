a = int(input("enter first number:"))
b = int(input("enter second number: "))
if a<b:
   for i in range(a,b+1,1):
       print(i, end=" ")
elif a==b:
   print("Both are Same")
else: 
   for i in range(a,b-1,-1):
       print(i, end = " " )

   
  
