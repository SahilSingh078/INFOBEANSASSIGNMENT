'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''
a = input("Enter the String: ")
count = 0
current = 0
for i in range(len(a)):
    j = 0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
