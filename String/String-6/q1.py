'''
1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc
'''

n=input("Enter string")
lar=""
i=0
while i<len(n):
    temp=""
    ch=n[i]
    temp+=ch
    
    j=i+1
    while j<len(n):
        if n[j] not in temp:
            temp+=n[j]
            j+=1
        else:
            break
    
    i+=1
    if len(temp)>len(lar):
        lar=temp
        

print(lar)   