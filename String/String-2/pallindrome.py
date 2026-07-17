'''
5.
Palindrome Product Code Checker
A factory wants to identify whether a product code reads the same forward and backward.
Input:
Enter product code: MADAM
Output:
Palindrome Code
Input:
Enter product code: PRODUCT
Output:
Not a Palindrome Code
'''
a = input("Enter The String: ")
c = a
rev = ""
for i in range (len(c)-1,-1,-1):
    rev = rev + a[i]
if c==rev:
    print("Palindrome ")
else:
    print("not Palindrome")
    
# if a==a[::-1]:
#     print("Palindrome ")
# else:
#     print("not Palindrome")