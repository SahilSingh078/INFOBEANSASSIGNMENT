'''
s = input("enter string")
sub = input("enter sub string")
if sub in s:
	print("found")
else:
	print("Not found") 
'''
'''
s = input("enter string : ")
l = s.lower()
#print(s.title())
result = ""
i=0
while i<len(s):
     if i==0 or l[i-1] ==" ":
         result = result + (chr(ord(l[i])-32))
     else:
         result = result+l[i]
     i+=1
print(result)
'''
'''
s = input("enter string 1: ")
a = input("enter string 2: ")
if len(s) == len(a):
    x=1
    for ch in s:
       if s.count(ch) != a.count(ch):
                x = 0
                break
    if x == 1:
        print("Anagram")
    else:
        print("not anagram")
else:
    print("Not Anagrams")
'''
'''
#COUNTING THE CHARACTERS
s1 = input("enter string 1: ")
s2 = input("enter string 2: ")
ch  = input("Enter character: ")
count  =0 
for i in s:
	if i == ch:
		count+=1
print("count: ",count)

'''


s1 = input("enter string 1: ")
s2 = input("enter string 2: ")
if len