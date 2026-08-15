'''
4
Search Insert Position
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
n = int(input("Enter the size of the array: "))
nums = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    nums.append(x)
ele = int(input("Enter element to search: "))
for i in range(len(nums)):
    if nums[i]==ele:
        print("Your number is at: ", i)