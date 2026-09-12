def is_fact(x):
    for ch in str(x):
        d = int(ch)
        fact = 1
        for j in range(1, d + 1):
            fact *= j
        return fact
