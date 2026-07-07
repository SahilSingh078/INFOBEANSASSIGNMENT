a = int(input("Enter Your Number : "))
b = int(input("Enter the Digit:"))
count = 0
for  i in str(a):
   if i==b:
     count+=1
print(count)
   else:
     print("try again")