'''
33
Find the longest word.
S = "find the longest word"
longest
'''
a = input("Enter the string: ")
word = a.split()
long = word[0]
for i in word:
        if len(i)>len(long):
            long = i
print("LONGEST WORD : ", long)