'''
36Reverse order of words.
one two three  ->  three two one'''

a = input("Enter the String: ")
word = a.split()
for i in range(len(word)-1,-1,-1):
    print("Reversed Order ->",word[i], end = " ")