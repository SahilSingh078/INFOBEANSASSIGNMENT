def is_perfect(x):
    sum=0
    temp = x
    for i in range(1, (x//2)+1):
        if x%i==0:
            sum+=i
    if temp ==sum:
        return True
    else:
        return False