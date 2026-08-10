'''
42Check if two strings are equal without equals().
S1 = "abc",
S2 = "abc"
TRUE
'''
a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a) != len(b):
    print("FALSE")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print("FALSE")
            break
    else:
        print("TRUE")
