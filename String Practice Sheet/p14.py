'''
4. Find the first occurrence of a character in a string.
# '''
# a = input("Enter a string: ")
# ch = input("Enter character: ")
# print(a.find(ch))

a = input("Enter a string: ")
ch = input("Enter character: ")
for i in range(len(a)):
    if a[i] == ch:
        print("First occurrence at index:", i)
        break
else:
    print("Character not found")