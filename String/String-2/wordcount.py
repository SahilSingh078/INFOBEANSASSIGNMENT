'''
3.
Word Counter in Complaint Message
A customer care system wants to count how many words are present in a complaint message.
Input:
Enter complaint: Delivery was delayed again today
Output:
Total words: 5
'''


a = input("Enter complaint: ")

count = 0

for i in range(len(a)):
    if a[i] != " " and (i == 0 or a[i-1] == " "):
        count += 1

print("Total words:", count)