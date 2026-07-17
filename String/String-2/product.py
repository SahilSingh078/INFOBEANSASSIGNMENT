'''
6.
Product Code Verification System
An e-commerce company wants to verify whether two product codes are rearranged versions of each other.
Conditions:
- Ignore spaces
- Ignore case sensitivity
Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room
Output:
Both Product Codes are Matching
'''

s1=input("enter first string: ")
s2=input("enter second string: ")
for i in range (len(s1)):
    if s1[i]==" ":
        break
    else: 
                
        if len(s1)!=len(s2):
            print("Not Matching")
        else:
        
          x=1
          i=0
          while i<len(s1):
                     ch=s1[i]
                     c1=0
                     c2=0
                     j=0
                     while j<len(s1):
                        if s1[j]==ch:
                           c1=c1+1
                        j=j+1
                     j=0
                     while j<len(s2):
                         if s2[j]==ch:
                            c2=c2+1
                         j=j+1
                     if c1!=c2:
                         x=0
                         break
                     
                     i=i+1
          if x==1:
             print("Both Are Matching")
          else:
           print("Not Matching")