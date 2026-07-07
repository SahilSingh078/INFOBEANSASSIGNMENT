n = int(input("Enter a number: "))

temp = n
digits = len(str(n))  
sum = 0

for i in str(n):
    sum += int(i) ** digits

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")