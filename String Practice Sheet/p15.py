'''
15. Find the last occurrence of a character in a string
'''
# a = input("Enter a string: ")
# ch = input("Enter character: ")
# print(a.rfind(ch))
a = input("Enter a string: ")
ch = input("Enter character: ")
for i in range(len(a) - 1, -1, -1):
    if a[i] == ch:
        print("Last occurrence at index:", i)
        break
else:
    print("Character not found")