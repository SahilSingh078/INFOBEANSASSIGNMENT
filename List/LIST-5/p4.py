'''
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''
n1 = int(input("Enter size of A: "))
A = []
for i in range(n1):
    A.append(int(input("Enter element: ")))
n2 = int(input("Enter size of B: "))
B = []
for i in range(n2):
    B.append(int(input("Enter element: ")))
n3 = int(input("Enter size of C: "))
C = []
for i in range(n3):
    C.append(int(input("Enter element: ")))
common = []
for i in range(n1):
    for j in range(n2):
        if A[i] == B[j]:
            if A[i] not in common:
                common.append(A[i])
for i in range(len(common)):
    for j in range(n3):
        if common[i] == C[j]:
            print("Common elements are: ",common[i], end=" ")
            break