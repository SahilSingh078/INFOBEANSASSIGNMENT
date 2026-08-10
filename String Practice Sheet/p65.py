'''
65
Count palindromic substrings. 
S = "aaa" 
6 (a, a, a, aa, aa, aaa)
'''
a = input("Enter the string: ")
count = 0
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        b = a[i:j]
        if b == b[::-1]:
            print(b)
            count += 1
print("count:", count)