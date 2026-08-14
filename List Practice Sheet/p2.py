'''
2. Remove Duplicates from Sorted Array

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]'''

n = int(input("Enter the size of the array: "))
nums = []
for i in range(n):
    x = int(input(f"enter element {i+1}: "))
    nums.append(x)

for i in nums:
    if nums.count(i)>1:
        nums.insert(i, "_")