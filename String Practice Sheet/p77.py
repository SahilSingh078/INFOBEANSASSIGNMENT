'''
77
Find the longest substring that appears at both ends. 
S = "abracadabra" 
"abra"
'''
# a = input("Enter your string: ")
# for i in range(len(a)-1, 0, -1):
#     for j in range(i+1, len(a)+1):
#         if a[0:i] == a[j-i:j]:
#             print(a[0:i])
#             break
#     else:
#         continue
#     break

s=input("Enter string :")
for i in range(len(s)-1):
     check=s[:len(s)-i-1]
     if s.startswith(check) and s.endswith(check):
          print(check)
          break
else:
   print("NOt found :")