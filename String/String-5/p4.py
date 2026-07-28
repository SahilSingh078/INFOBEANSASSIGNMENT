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
a = input("enteer thhe string: ")
highest = 0
for i in a:
    if a.count(i)>highest:
        highest = a.count(i)
char= "" 
for i in a:
    if a.count(i)== highest and  i not in char:
        char+=i
print(char, end=" ")
