'''
56Reverse only consonants. S = "apple" "eplpa"
'''
a = input("Enter the string: ")
vowel = "aeiouAEIOU"
result = ""
for i in a:
    if i not in vowel:
        result += i
result = result[::-1]
j = 0
for i in a:
    if i not in vowel:
        print(result[j], end="")
        j += 1
    else:
        print(i, end="")