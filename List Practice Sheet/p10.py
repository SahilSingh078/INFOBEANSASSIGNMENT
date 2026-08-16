'''
10
Move Zeroes
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

a = input("Enter the elements of array with space: ").split()
count = a.count("0")
while "0" in a:
    a.remove("0")
for i in range(count):
    a.append("0")
print(a)