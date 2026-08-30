'''
22
3 Sum Closest
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 '''
a = list(map(int, input("Enter the values: ").split()))
tar = int(input("Enter target: "))
clo = a[0]+a[1]+a[2]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            total = a[i]+a[j]+ a[k]
            if abs(total - tar) < abs(clo - tar):
                clo = total
print("Closest sum:", clo)