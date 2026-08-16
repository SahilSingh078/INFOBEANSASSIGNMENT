'''
8
Contains Duplicate
Input: nums = [1,2,3,1]

Output: true
'''
a = input("enter element using space: ").split()
for i in a:
    if a.count(i)>1:
        print("true")
        break
else: 
      print("false")
    