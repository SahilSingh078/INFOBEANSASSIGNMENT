'''
20Find the lowest frequency character.
 S = "aabbcde" 
 c', 'd', 'e' (any one or all)
 '''

a = input("Enter the string: ")
lowest = len(a)
for ch in a:
    count = a.count(ch)
    if count < lowest:
        lowest = count
print("lowest characters are: ", end="")
result = ""
for ch in a:
    if a.count(ch) == lowest and ch not in result:
        print(ch, end=" ")
        result+=ch