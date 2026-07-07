'''
 ATM Note Counter
A bank ATM dispenses ₹100 notes.
Write a program to:
- Read withdrawal amount
- Count how many ₹100 notes needed using loop
Input:
700
Output:
Notes = 7
'''

a = int(input("Enter withdrawal amount: "))

count = 0

while a >= 100:
    a = a- 100
    count += 1

print("Notes =", count)
print("Remaining Amount =", a)