'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17

'''

a = int(input("Enter Your Number: "))

while True:
    a += 1
    x = 0

    for i in range(1, a + 1):
        if a % i == 0:
            x += 1

    if x == 2:
        print("Next Prime Number =", a)
        break