'''
3
Remove Element
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
'''
n = int(input("Enter the size of the array: "))
nums = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    nums.append(x)
ele = int(input("Enter element to remove: "))
result = []
for i in nums:
    if i != ele:
        result.append(i)
for i in range(n-len(result)):
    result.append("_")
print(result)