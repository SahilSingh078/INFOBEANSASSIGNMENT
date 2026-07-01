'''
6. Next Prime Cabin Number Generator
A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin number.
System must find the next available prime cabin number.
Write a program using loops.
Input:
24
Output:
Next Prime Cabin = 29
'''

a = int(input("Enter Your Number: "))

while True:
    a += 1
    x = 0

    for i in range(1, a + 1):
        if a % i == 0:
            x += 1

    if x == 2:
        print("Next Prime Cabin =", a)
        break