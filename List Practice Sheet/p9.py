'''
9 Intersection of Two Arrays II
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''
a = input("Enter elements of 1st Array using space: ").split()
b = input("Enter elements of 2nd Array using space: ").split()
result = []
for i in a:
    for j in range(len(b)):
        if i == b[j]:
            result.append(i)
            break
print(result)