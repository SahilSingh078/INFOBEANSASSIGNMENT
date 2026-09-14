def is_prime(x):
    count = 0
    if x<2:
        return "NOT PRIME"
    else:
        for i in range(2,(x//2)+1):
            if x%i==0:
                count+=1
        if count==0:
            return "PRIME"
        else:
            return "NOT PRIME"
