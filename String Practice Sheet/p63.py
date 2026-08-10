'''
63
Count frequency of each character. 
S = "aabcc" 
a: 2, 
b: 1, 
c: 2
'''
a = input("Enter the string: ")
count=0
if a.isalpha():
    result = ""
    for i in a:
        if i not in result:
            print(i, ":", a.count(i))
            result+=i
else:
    print("Only alphabets allowed!!!!!")