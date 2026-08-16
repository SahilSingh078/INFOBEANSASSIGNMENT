'''
7
Single Number
Input: nums = [2,2,1]

Output: 1
'''
a = input("Enter elements with space: ").split()
for i in a:
    if a.count(i)==1:
        print(i)