'''
18
Shortest Unsorted Continuous Subarray
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0
 '''
arr = int(input("enter the size of array: "))
ar = []
for i in range((arr)):
    x = int(input(f"enter elements {i+1}: "))
    ar.append(x)
print(ar)
res = []
for i in range(len(ar)):
    for j in range(i+1, len(ar)+1):
        d = ar[i:j]
        res.append(d)
b = sorted(arr)


