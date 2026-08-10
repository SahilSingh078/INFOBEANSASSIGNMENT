'''
54
Replace all duplicate characters with '$'. 
S = "hello" 
"he$lo"
'''
a = input("Enter the String: ")
result =""
for i in range(len(a)):
    if a[i] in a[:i]:
        result+=a[i]
    elif a[i] in a[i+1: ]:
        result+="$"
    else:
        result+=a[i]
print(result)
  