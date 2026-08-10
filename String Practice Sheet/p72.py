'''
72
Print all substrings of length n. 
S = "abc", 
n = 2 "ab, bc"
'''
a = input("Enter the string: ")
n = int(input("enter the length of substring: "))
count = 0
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        b = a[i:j]
        if len(b)==n:
            print(b, end = " ")
            count+=1        
print(count)