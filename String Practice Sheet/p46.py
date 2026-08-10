'''
46Check if a substring appears at both the start and end. 
S = "abcabca", 
Sub="abca" 
TRUE
'''
a = input("Enter the string: ")
b = input("Enter the substring: ")
if (a[:len(b)] == b) and ( a[-len(b):] == b):
    print("True")
else:
    print("False")