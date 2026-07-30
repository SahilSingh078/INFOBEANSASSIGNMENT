'''
23. Print all characters occurring exactly twice
'''
a = input("Enter the string: ")
result= ""
# for i in a:
#     if a.count(i) == 2 and i not in result:
#         result+=i+ " "
# print("character are : " ,result)

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 2 and a[i] not in result:
        print(a[i], end=" ")
        printed += a[i]