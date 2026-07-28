'''
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d
'''
n=input("Enter the string")
temp=""
lar=""
i=0
while i<len(n):
    temp=""
    ch=n[i]
    temp+=ch
    j=i+1
    while j<len(n):
        cj=n[j]
        if cj not in temp:
            temp+=cj
            j+=1
        else:
            break
        
    if len(temp)>len(lar):
        lar=temp
    i+=1

print(lar)
   
    
    

