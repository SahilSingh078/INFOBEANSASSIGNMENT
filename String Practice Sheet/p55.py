'''
55
Reverse only vowels. 
S = "hello" 
"holle"
'''
a = input("Enter the string: ")
vowel = "aeiouAEIOU"
result = ""
for i in a:
    if i in vowel:
        result += i
result = result[::-1]
j = 0
for i in a:
    if i in vowel:
        print(result[j], end="")
        j += 1
    else:
        print(i, end="")