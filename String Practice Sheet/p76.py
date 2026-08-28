'''
76
Find the longest common suffix among strings. 
Strings = ["baking", "making", "taking"] "king"
'''
n = list(map(str,input("enter the values: ").split()))
res = []
for i in range(len(n)):
   b = n[i][::-1]
   res.append(b)
suffix = res[0]
for i in range(1, len(res)):
    for j in range(len(suffix), -1, -1):
       if res[i].find(suffix)!= 0:
        suffix = suffix[:-1]
print("Suffix is : ",suffix[::-1])