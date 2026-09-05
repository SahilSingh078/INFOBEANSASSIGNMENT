'''
82
Create a string from a character array. 
Char[] = {'h', 'i'} "
hi"
'''
s = input("Enter character array using space: ").split()
for i in s:
    c = "".join(s)
print(c)