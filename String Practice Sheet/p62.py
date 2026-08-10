'''
62
Count vowels and consonants. 
S = "apple" 
Vowels: 2, 
Consonants: 3
'''
a = input("enter the string: ")
vowel = "aeiouAEIOU"
count =0
count1 =0
if a.isalpha():
    for i in a:
        if i not in vowel:
            count1+=1
        else:
            count+=1
    print("Vowels: ", count)
    print("Consonants : ", count1)
else:
    print("Only Alphabets allowed!!!!!!") 