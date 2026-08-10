'''
32
Count frequency of each word.
 S = "apple banana apple"
 apple: 2, banana: 1
'''

a = input("Enter the string: ")
word = a.split()
printed = ""
for i in word:
    if i not in printed:
        printed +=i+" "
        print(i, ":",a.count(i))