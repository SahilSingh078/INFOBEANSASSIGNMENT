'''
66
Count number of sentences in a paragraph. 
P = "This. Is. Test." 
3
'''
# a = input("enter the string: ")
# count = 0
# for i in range(len(a)):
#     if a[i]== " " and a[i-1] == "."   or (i==len(a)-1 and a[i]=="."):
#         count+=1
# print("Number of words: ", count)

a = input("Enter the paragraph: ")

count = 0

for i in range(len(a)):
    if a[i] == ".":
        if i == 0 or a[i-1] != ".":
            count += 1

print("Number of sentences:", count)