'''
49
Replace all consonants with '*' (Example suggests replacing non-vowels). 
S = "apple" "ap*le" 
(or similar output depending on implementation)
'''
a = input("Enter the string: ")
# vowel = "aeiouAEIOU"
# b=""
# for i in a:
#     if i not in vowel:
#         a = a.replace(i, "*")
# print(a)
  
result = ""
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i== "U" or i=="I":
        result+=i
    else:
        result+="*"
print(result) 