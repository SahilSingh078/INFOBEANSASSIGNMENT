'''
74
Find the longest substring without repeating characters. S = "abcabcbb" "abc
'''
a = input("Enter the string: ")
lar = 0
result = ""
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        b = a[i:j]
        repeat = False
        for k in range(len(b)):
            if b.count(b[k])>1:
                repeat = True
                break
        if repeat== False:
            if len(b)>lar:
                lar=len(b)
                result= b
print(result)

# s = input("Enter a string: ")
# longest = ""
# current = ""
# for ch in s:
#     if ch in current:
#         current = current[current.index(ch) + 1:]
#     current += ch
#     if len(current) > len(longest):
#         longest = current
# print("Longest substring without repeating characters:", longest)