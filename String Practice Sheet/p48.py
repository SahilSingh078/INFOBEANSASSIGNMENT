'''
48Remove all vowels. 
S = "aeiou XYZ" 
" XYZ"
'''
a = input("Enter the string: ")
# vowel = "aeiouAEIOU"
# # for i in vowel:
# #     a=a.replace(i," ")
# # print(a)
result = ""
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i== "U" or i=="I":
        pass
    else:
        result+=i
print(result) 