'''
73
Find the longest palindromic substring. 
S = "babad" 
"bab" (or "aba")
'''
a = input("Enter the string: ")
lar = 0
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        b = a[i:j]
        if b == b[::-1]:
            if len(b)>lar:
                lar =len(b)
                ans = b
print(ans)
        
