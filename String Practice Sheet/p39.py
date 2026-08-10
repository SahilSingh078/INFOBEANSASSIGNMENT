'''
39Search all occurrences of a character. S = "banana",
Char='a' 
1, 3, 5 (indices)'''
a = input("Enter the string: ")
b = input("Enter the character to find: ")
for i in range(len(a)):
    if b==a[i]:
        print(i, end =" ")
