'''
# 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1
'''

n=input("Enter the string").lower()
res=temp=t=""
c=0
for x in sorted(n):
    t+=x
i=0
while i<len(t):
     ch=t[i]
     if ch==" ":
          pass
     elif ch not in temp:
          temp+=ch
          res=res+ch
          c=t.count(ch)
          res=res+str(c)
     i+=1
print(res)