'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8

'''
n=input("Enter string")
i=0
c=0
x=""
while i<len(n):
    ch=n[i]
    if 'a'<=ch>='z' or 'A'<=ch>='Z':
        pass
    elif ch in '0123456789':
        c=n.count(ch)
        if c>1:
            pass
        else:
            x=ch
            break

    i+=1

if x=="":
    print("no unique digit found")
else:
    print(x)
    