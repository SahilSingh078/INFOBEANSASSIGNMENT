'''
3.  Smart Chat Message Cleaner
A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.
Input: Enter message: Java is easy
Output: Cleaned Message: Java is easy
'''
# s = input("Enter the string: ")
# result =""

# for i in range(len(s)):
#     ch=s[i]
#     if s[i-1] == " " and s[i]==" ":
#             pass
#     else:
#           result=result+ch
#     if result[0]==" ":
#       pass
#     else:
#          result=result+ch      
# print(result)

s = input("Enter the string: ")
result = ""
for i in range(len(s)):
    if s[i] == " ":
        if i==0 or s[i-1]==" ":
            continue
    result+=s[i]
print(result)