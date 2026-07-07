 '''
Unique Digit Security Scanner
A smart locker accepts only numbers whose all digits are unique.
Write a program using for-else loop to:
- Check every digit
- If any repeated digit found reject
- Else accept
Input:
57294
Output:
Valid Unique Code
'''

a = input("Enter the code: ")

for d in a:
    count = 0

    for digit in a:
        if d == digit:
            count += 1

    if count > 1:
        print("Rejected Code")
        break
else:
    print("Valid Unique Code")