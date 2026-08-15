'''
5Plus One
Input: digits = [1,2,3]
Output: [1,2,4]
'''

n = int(input("Enter the size of the array: "))
nums = ""
for i in range(n):
    x = input(f"Enter element {i+1}: ")
    nums+=x
print(list(nums))
b = str(int(nums) + 1)
result = []
for i in b:
    result.append(int(i))
print(result)