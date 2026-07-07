'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

a = int(input("Enter Your Number: "))

temp = a
largest = 0
smallest = 9
while temp > 0:
    digit = temp % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    temp = temp // 10

sum = largest + smallest

print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", sum)

count = 0

for i in range(1, sum + 1):
    if sum % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")