'''
6. Find Occurrence of a Word in a String
Product Review Analysis System
An e-commerce company wants to analyze customer reviews.
The company wants a Python program to count how many times a particular word appears in a review.
Input Sentence:
```
iphone is good and iphone battery is strong
```
Word:
```
iphone
```
Output:
```
2
```
---
'''
a = input("Enter the sentence: ")
word = input("Enter the word: ")
temp = ""
count = 0
for i in range(len(a)):
    if a[i] != " ":
        temp += a[i]
    else:
        if temp == word:
            count += 1
        temp = ""
if temp == word:
    count += 1
print(count)