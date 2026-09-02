'''
79
Divide a string into n equal parts. S = "abcdef", 
n = 3 "ab", "cd", "ef"'''
s = input("Enter your string: ")
n = int(input("Enter no. of parts: "))
parts = len(s) // n
k = 0
for i in range(n):
    print(s[k:k+ parts], end=" ")
    k= k + parts