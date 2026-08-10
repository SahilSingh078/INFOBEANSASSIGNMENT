'''
47Check for substring using concatenation trick. 
S1="CDAB", 
S2="ABCD" 
True (S1 is in S2+S2)
'''
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if (s1 in s2 + s2) and (s2 in s1 + s1):
    print("True")
else:
    print("False")