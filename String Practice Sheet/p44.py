'''
44Check if two strings are anagrams. 
S1 = "listen",
 S2 = "silent"
   TRUE
'''
# a = input("Enter first string: ")
# b = input("Enter second string: ")
# if len(a) != len(b):
#     print("FALSE")
# # else:
# #     if sorted(a) == sorted(b):
# #         print("TRUE")
# #     else:
# #         print("FALSE")

a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a) != len(b):
    print("FALSE")
else:
    for i in a:
        count1 = 0
        count2 = 0
        for j in a:
            if i == j:
                count1 += 1
        for k in b:
            if i == k:
                count2 += 1
        if count1 != count2:
            print("FALSE")
            break
    else:
        print("TRUE")