'''
8. Toggle the Case of Each Character
'''

a = input("Enter a string: ")
# result = ""
# for ch in a:
#     if 'A' <= ch <= 'Z':
#         result += chr(ord(ch) + 32)
#     elif 'a' <= ch <= 'z':
#         result += chr(ord(ch) - 32)
#     else:
#         result += ch
# print("Toggled String:", result)
print("Toggled String:", a.swapcase())
