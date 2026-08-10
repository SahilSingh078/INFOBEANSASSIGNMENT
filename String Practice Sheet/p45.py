'''
45
  Check whether a string starts/ends with another string.
S = "apple pie", Prefix = "apple", Suffix = "pie" 
Start: True,
End: True
'''

a = input("Enter the string: ")
b = input("Enter the starting string: ")
c = input("Enter the ending string: ")
# if a.startswith(b):
#     print("Start: True")
# else:
#     print("False")
# if a.endswith(c):
#     print("End: True")
# else:
#     print("False")

if a[:len(b)] == b:
    print("Start: True")
else:
    print("Start: False")
if a[-len(c):] == c:
    print("End: True")
else:
    print("End: False")        