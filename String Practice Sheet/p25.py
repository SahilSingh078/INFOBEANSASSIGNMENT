'''
25. Count total words in a string
'''
a = input("Enter the string: ")
# count = 1
# for ch in a:
#     if ch == " ":
#         count += 1
# print("Total words:", count)

a = input("Enter the string: ")
words = a.split()
print("Total words:", len(words))