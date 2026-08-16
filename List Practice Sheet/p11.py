'''
11
Best Time to Buy and Sell Stock
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
a = list(map(int, input("Enter values [using space]: ").split()))
max = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        d = int(a[j]-a[i])
        if d>max:
            max = d
print(max)