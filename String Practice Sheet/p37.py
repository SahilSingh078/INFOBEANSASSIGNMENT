'''
37 Reverse each of words.
S = "cat dog" 
"tac god"
'''
a = input("Enter the String: ").split()
result=""
for i in a:
    result+= i[::-1]+" "
print("resultant: ", result)