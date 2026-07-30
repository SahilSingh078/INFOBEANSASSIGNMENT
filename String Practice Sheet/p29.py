'''
29. Remove all occurrences of a word
'''
a = input("Entet the string: ")
b = input("Enter what to remove: ")
# result = a.replace(b, "")
# print(result)
word = a.split()
result = ""
for i in word:
    if i!=b:
        result+= i + " "
print(result)
