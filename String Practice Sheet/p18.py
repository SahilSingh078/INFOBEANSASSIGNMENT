'''
18Replace occurrences of a character. 
S = "apple", Old='p', 
New='x' "axxle"
'''
a = input("Enter the string: ")
b = input("Enter the old character: ")
c = input("Enter the new character: ")
# a = a.replace(b, c)
# print("Updated string:", a)

result = ""
for ch in a:
    if ch ==b:
        result = result + c
    else:
        result = result + ch
print("Updated string:", result)