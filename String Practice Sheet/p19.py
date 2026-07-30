'''
19Find the highest frequency character. 
S = "abracadabra"
 a
 '''
a = input("Enter the string: ")
highest = 0
char = ""
# for i in range(len(a)):
#     count = 0
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             count += 1
#     if count > highest:
#         highest = count
#         char = a[i]
# print("highest repeated character:", char)

for ch in a:
    count = a.count(ch)
    if count > highest:
        highest = count
        char = ch
print("highest repeated character:",char)