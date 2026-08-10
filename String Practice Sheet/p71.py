'''
71
Print all substrings. 
S = "abc" "a, b, c, ab, bc, abc
'''
a = input("Enter the string: ")
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        print(a[i:j], end = " ")