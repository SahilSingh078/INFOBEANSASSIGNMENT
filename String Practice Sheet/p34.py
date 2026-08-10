'''
Find the shortest word.
'''
a = input("Enter the string: ")
word = a.split()
short = word[0]
for i in word:
        if len(i)<len(short):
            short = i
print("Shortest word: ", short)