'''
12
Maximum Subarray
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6
'''
a = list(map(int,input("Enter elements: ").split()))
for i in range(len(a)):
    for j in range(i+1, len(a)):
        d = a[i]+ a[j]
