'''
Check if a string contains a substring (without using built-in method).
 S1 = "Hello",
 Sub="ell"
TRUE'''

a = input("Enter the string: ")
b = input("Enter to check: ")
if b in a:
    print("True")
else:
    print("False")
