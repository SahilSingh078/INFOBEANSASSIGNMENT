'''
12. Get the Unicode code point of a character at an index.
'''
a = input("enter the string: ")
ind = int(input("Enter the index number: "))
if ind<len(a):
    print("Unicode is : ", ord(a[ind]))
else:
    print("Ivalid Indez")