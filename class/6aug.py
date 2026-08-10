n =int(input("Enter size:"))
arr =[]
print("Enter Elements: ")
for i in range(n):
    arr.append(int(input()))
print(arr)
#cyclic 
# last = arr[n-1]
# for i in range(n-1,-1,-1):
#     arr[i]=arr[i-1]
# arr[0]=last5
# print(arr)

#sum barabr k ke
k = int(input("Enter the Desired number: "))
count = 0
for i in range(n):
    for j in range(i+1, n):7
        if arr[i]+arr[j]==k:
            count+=1
print("no. of pairs are: ", count)