'''
23
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 '''
a = list(map(int,input("Ente the vakues: ").split()))
tar = int(input("Enter target value: "))
res =[]
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        # print(a[i:j])
        if sum(a[i:j])==tar:
            res.append(a[i:j])
print(len(res))