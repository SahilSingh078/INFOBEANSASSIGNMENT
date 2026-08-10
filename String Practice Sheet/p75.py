'''
75
Find the longest common prefix among strings. 
Strings = ["flower", "flow", "flight"] 
"fl"
'''
n = int(input("Enter the number of string: "))
string = []
for i in range(n):
    x = input("Enter the string: ")
    string.append(x)
print(string)
prefix = string[0]
for i in range(1, len(string)):
    for j in range(len(prefix), -1, -1):
       if string[i].find(prefix)!= 0:
        prefix = prefix[:-1]
print(prefix)
                   
'''
str = input("Enter the string:").split()
s = str[0]
flag = 1
for i in range(1,len(str)):
    curr = str[i]
    j = 0
    while j < len(curr) and j < len(s):
        if s[0] == curr[0]:
            if s[j] == curr[j]:
                j+=1
            else:
                s = curr[:j]
                break
        else:
            print("nothing common")
            flag = 0
            break
if flag == 1:
    print(s)
'''