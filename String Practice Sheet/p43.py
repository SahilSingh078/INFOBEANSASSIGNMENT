'''
43Check if two strings are rotations of each other. 
S1 = "abcde",
 S2 = "cdeab" 
 TRUE
 '''
a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a) != len(b):
    print("FALSE")
else:
    if b in (2*a):
        print("TRUE")
    else:
        print("FALSE")