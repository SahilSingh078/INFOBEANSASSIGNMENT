'''
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
'''

n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
positive = []
negative = []
for i in range(n):
    if arr[i] >= 0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])
result = []
p = 0
q = 0
for i in range(n):
    if p<len(positive):
        result.append(positive[p])
        p+=1
    if q<len(negative):
        result.append(negative[q])
        q+=1
print("Result:", result)