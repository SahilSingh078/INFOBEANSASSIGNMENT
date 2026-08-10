'''
61
Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, 
Digits: 2, 
Special: 1
'''
a = input("Enter the String: ")
count1 = 0
count2 = 0
count3 = 0
for i in a:
    if i.isalpha():
        count1+=1 
    elif i.isdigit():
        count2+=1
    else:
        count3+=1
print("Alphabet: ", count1)
print("Digit: ", count2)
print("Special: ", count3)