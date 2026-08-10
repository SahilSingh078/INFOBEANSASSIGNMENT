"""
31
Remove duplicate words.
 S = "the cat and the dog"
 "the cat and dog"
"""
a = input("Enter the string: ")
word = a.split()
result=[]
for i in word:
	if i not in result:
		result.append(i)
print("Resultant string:", " ".join(result))