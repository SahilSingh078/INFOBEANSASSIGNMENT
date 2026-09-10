'''
86
Print all permutations of a string without repetition. 
S = "ab"-> "ab", "ba"
'''

text = input("Enter the string: ")
perms = [""]
for char in text:
    new_perms = []
    for p in perms:
        for i in range(len(p) + 1):
            candidate = p[:i] + char + p[i:]
            if candidate not in new_perms:
                new_perms.append(candidate)
    perms = new_perms
print(", ".join(f'"{item}"' for item in perms))