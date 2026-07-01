'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
a = int(input("Enter Your Number: "))
count = 0

for i in range(1, a + 1):
    if a % i == 0:
        count += 1

if count == 2:
    print("Prime Number")

    n = a
    while True:
        n += 1
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            print("Next Prime =", n)
            break

else:
    print("Non Prime Number")

    n = a
    while n > 1:
        n -= 1
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            print("Previous Prime =", n)
            break