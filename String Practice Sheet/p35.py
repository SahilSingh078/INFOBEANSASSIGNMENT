'''
Find the first palindrome word.
'''
a = input("Enter the string: ")
word = a.split()
for i in word:
    b =i[::-1]
    if i==b:
        print("First Pallindrome Word: ",i)
        break
else:
        print("No Pallidrome Word Found")