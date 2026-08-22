'''
    12
    Maximum Subarray
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6
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
su=[]
for i in res:
    su.append(sum(i))
print("The subarray sum is: " , max(su))