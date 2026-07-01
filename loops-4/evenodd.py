'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
a = int(input("Enter Your Number: "))

temp = a
even = 0
odd = 0
while temp > 0:
    digit = temp % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    temp = temp // 10

difference = even - odd

if difference < 0:
    difference = -difference

print("Even Count =", even)
print("Odd Count =", odd)
print("Difference =", difference)

count = 0

if difference <= 1:
    print("Not Prime")
else:
    for i in range(1, difference + 1):
        if difference % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")