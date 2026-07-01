'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''

a = int(input("Enter Your Number: "))
temp =a

while True:
    a = a + 1
    x = 0

    for i in range(1, a + 1):
        if a % i == 0:
            x += 1

    if x == 2:
        print("Next Prime =", a)
        break
gap = a - temp
print("GAP: ", gap)