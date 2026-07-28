'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
'''

a = input("Enter The String: ").split()
highest = 0
word = ""
for i in range(len(a)):
    count= 0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count>highest:
        highest=count
        word = a[i]
print("Most frequent word: ", word)