'''
40Search all occurrences of a word. S = "a b a b",
 Word='b' 
2, 6 (start indices)
'''
a = input("Enter the string: ")
b = input("Enter the word to find: ")
count= 0
for i in range(len(a)):
    if b==a[i]:
        print(i, end =" ")
