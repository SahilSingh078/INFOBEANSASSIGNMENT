'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found
'''

n=input("Enter string")
i=0
while i<len(n):
    ch=n[i]
    cp=n[i-1]
    cp1=n[i-2]
    if ch==cp==cp1:
        print("spam pattern found")
        break
    else:
        pass
    i+=1
else:
    print("clean message")
    