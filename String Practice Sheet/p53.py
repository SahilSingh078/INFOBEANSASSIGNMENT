'''
53Remove punctuation. 
S = "Hello, world!" 
"Hello world"
'''
a = input("Enter the string: ")
result = ""
punc = ",.!?:;'\""

for ch in a:
    if ch not in punc:
        result+= ch
print(result)