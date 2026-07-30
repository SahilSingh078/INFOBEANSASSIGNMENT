'''
22Find the last repeating character. 
S = "abracadabra"
 r'
 '''
a = input("Enter the string: ")
for i in range(len(a)-1, -1, -1):
    # count = 0
    # for j in range(len(a)):
    #     if a[i] == a[j]:
    #         count += 1
    # if count > 1:
    #     print("Last repeating character:", a[i])
    #     break
    
    if a.count(a[i]) > 1:
        print("Last repeating character:", a[i])
        break