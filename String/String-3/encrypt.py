'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''

a =input("Enter Message: ").split()
for i in range(len(a)):
    ch =a[i]
    b=ch[::-1]
    print(b, end=" ")
