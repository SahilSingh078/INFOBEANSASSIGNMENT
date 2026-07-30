'''
. Compare two strings (case-sensitive).
'''
a = input("Enter the 1st string: ")
b = input("Enter the 2nd string: ")
if len(a) != len(b):
    print("Strings are not same")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print("Strings are not same")
            break
    else:
        print("Strings are same")