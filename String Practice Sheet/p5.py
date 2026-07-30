'''
5. Compare two strings ignoring case.
'''
'''
. Compare two strings (case-sensitive).
'''
a = input("Enter the 1st string: ").lower()
b = input("Enter the 2nd string: ").lower()
if len(a) != len(b):
    print("Strings are not same")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print("Strings are not same")
            break
    else:
        print("Strings are same")