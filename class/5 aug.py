'''
peak element dhundho
'''
n =int(input("Enter size:"))
arr =[]
print("Enter Elements: ")
for i in range(n):
    arr.append(int(input()))
print(arr)
peakindex = -1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peakindex = i