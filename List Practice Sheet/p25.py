'''
25
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:x
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]'''

a = list(map(int, input("Enter the values: ").split()))
tar = int(input("Enter Your Target: "))
pos = []
for i, value in enumerate(a):
    if value == tar:
        pos.append(i)
if pos:
    print([pos[0], pos[-1]])
else:
    print([-1, -1])

    