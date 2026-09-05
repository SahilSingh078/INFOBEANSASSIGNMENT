'''
83
Create a string from a byte array. Byte[] = {72, 101, 108} 
(ASCII for H, e, l) "
Hel"
'''
s = list(map(int,input("Enter character array using space: ").split()))
c = ""
for i in s:
    c = c+(chr(i))
print(c)