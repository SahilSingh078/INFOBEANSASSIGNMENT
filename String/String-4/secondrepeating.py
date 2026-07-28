'''
8.
Find the Second Highest Repeating Character in a String
Social Media Trend Analysis System
A social media company analyzes hashtags and user comments to identify trending character patterns.
The analytics team wants a Python program to find the character with the second highest frequency in a given string.
This helps detect secondary trending patterns in user activity.
Input:
aaabbbbccddeee
Output:
e
Explanation:
b occurs 4 times → highest
e occurs 3 times → second highest
Condition:
Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''

a = input("Enter the string: ")
highest = 0
second = 0
highest_char = ""
second_char = ""
checked = ""
for ch in a:
    if ch == " ":
        continue
    if ch in checked:
        continue
    checked += ch
    count = a.count(ch)
    if count > highest:
        second = highest
        second_char = highest_char
        highest = count
        highest_char = ch
    elif count > second and count < highest:
        second = count
        second_char = ch
if second == 0:
    print("Second highest repeating character not found")
else:
    print(second_char)