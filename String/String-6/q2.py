'''
# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started
'''
{1}



n=input("Enter string")
word=n.split()
res=""
i=0
while i<len(word):
    ch=word[i]
    chp=word[i-1]
    chp1=word[i-2]
    if ch==chp==chp1:
        pass
    elif ch==chp:
        pass
    else:
        res=res+ch+" "
    i+=1
'''



{2}



n=input("Enter string")
word=n.split()
res=""
temp=""
i=0
while i<len(word):
    ch=word[i]
    if ch not in temp:
        temp+=ch
        cp=word[i-1]
        cp1=word[i-2]
        if ch==cp==cp1:
            res=res+ch+" "
        elif ch==cp:
            res=res+ch+" "
        else:
            res=res+ch+" "
    i+=1

print(res)
'''



{3}

n=input("Enter string")
word=n.split()
temp=""
i=0
while i<len(word):
    ch=word[i]
    if ch not in temp:
        temp+=ch+" "
    else:
        pass
    i+=1

print(temp)
''