'''
13. Get the Unicode code point before a given index
'''
# a = input("enter the string: ")
# ind = int(input("Enter the index number: "))
# if ind<len(a):
#     print("Unicode is : ", ord(a[ind])-1)
# else:
#     print("Ivalid Indez")
a = input("Enter a string: ")
ind = int(input("Enter index: "))
if  ind < len(a):
    ch = a[ind - 1]
    print(ord(ch))
else:
    print("No character before this index")