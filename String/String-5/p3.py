'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''

# a = input("Enter the String: ")
# result = " "
# for i in a:
#     if result==" " or i != result[-1]:
#         result+=i
# print(result) 

a= input("Enter the string: ")
word = ""
for i in range(len(a)):
    if i ==0 or a[i] !=a[i-1]:
        word+=a[i]
print(word)