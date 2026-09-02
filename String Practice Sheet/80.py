'''
80
Print list items containing all characters of a given word
List = ["apple", "plea"], 
Word = "pal" 
"apple", "plea"
'''
a = input("Enter list items using space: ").split()
word = input("Enter word to find: ")
for j in a:
    count = 0
    for i in word:
        if i in j:
            count += 1
    if count == len(word):
        print(j)