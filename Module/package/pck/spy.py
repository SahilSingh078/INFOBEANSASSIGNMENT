def is_spy(x):
    sum = 0
    prod = 1
    for i in str(x):
        sum+=int(i)
        prod*=int(i)
    if sum==prod:
        return "SPY Number"
    else:
        return "Non Spy Number"