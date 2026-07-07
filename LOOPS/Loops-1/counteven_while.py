a = int(input("Enter Your Number : "))
count = 0

while a>0:
  digit = a%10
  if digit%2==0:
    count+=1
  a = a//10
if count>0: 
   print("EVEN NUMBERS: ",count)
else:
   print("No even digits ")