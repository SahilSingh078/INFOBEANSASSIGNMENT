'''
1. Two Sum
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
n = int(input("Enter the Number of elements: "))
k = int(input("Enter the targeted sum:  "))
result=[]
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    result.append(x)
ans = []
for i in range(len(result)):
    for j in range(i+1, len(result)):
        if result[i]+ result[j] == k:
            ans.append(i)
            ans.append(j)
            print(ans)
