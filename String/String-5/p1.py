'''
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System
A cybersecurity company monitors user session IDs generated during secure login sessions.
To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.
Input:
abcabcbb
Output:
abc
'''

a = input("Enter the String: ")
long = ""
for i in range(len(a)):
    rn = ""
    for j in range(i, len(a)):
        if a[j] not in rn:
            rn +=  a[j]
        else:
            break

    if len(long)<len(rn):
        long = rn

print(long)