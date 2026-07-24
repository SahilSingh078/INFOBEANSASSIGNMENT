'''
5. Find the Number of Unique Characters in a String
Password Strength Analyze
A cybersecurity company checks password strength based on the number of unique characters present.
Passwords containing more unique characters are considered more secure.
Write a Python program to count the number of unique characters in a string.
Input:
```
aabbccdde
```
Output:
```
5
```
'''


a = input("Enter the string: ")
count = 0

for i in range(len(a)):
    again = 0

    for j in range(i):
        if a[i] == a[j]:
            again += 1

    if again == 0:
        count += 1

print(count)