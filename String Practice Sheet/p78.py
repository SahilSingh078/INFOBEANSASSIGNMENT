'''
78
Find the longest mirror-image substring at both ends. 
S = "aabccbaa" "aab"'''
s = input("Enter the string: ")
res = ""
for i in range(len(s)//2):
    if s[i] == s[len(s) - 1 - i]:
        res += s[i]
    else:
        break
print(res)