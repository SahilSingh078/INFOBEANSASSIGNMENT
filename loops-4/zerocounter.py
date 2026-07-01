'''
.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''

a = int(input("Enter Your Number: "))

temp = a
zero = 0
sum = 0
smallest = 9
while temp > 0:
    digit = temp % 10

    if digit == 0:
        zero+= 1

    sum += digit

    if digit < smallest:
        smallest = digit

    temp = temp // 10

final = (zero + sum) * smallest

print("Zero Count =", zero)
print("Sum =", sum)
print("Smallest Digit =", smallest)
print("Final Result =", final)

count = 0

if final <= 1:
    print("Not Prime")
else:
    for i in range(1, final + 1):
        if final % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")