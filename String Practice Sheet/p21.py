'''
21Find the first non-repeating character.
 S = "aabbcde"
   c
'''
a = input("Enter the string: ")
# for ch in a:
#     if a.count(ch) == 1:
#         print("1st non repeating :", ch)
#         break
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        print("F1st non repeating :", a[i])
        break